"""Run the trained model against the browser T-Rex game."""

from __future__ import annotations

import time

import numpy as np
from mss import mss
from PIL import Image

from .config import LABEL_ORDER, MODEL_JSON_PATH, MODEL_WEIGHTS_PATH, PLAY_MONITOR
from .model import load_model
from .preprocessing import preprocess_image


def main() -> None:
    import keyboard

    model = load_model(MODEL_JSON_PATH, MODEL_WEIGHTS_PATH)
    frame_time = time.time()
    tick = 0
    key_down_pressed = False

    with mss() as screen_capture:
        while True:
            screenshot = screen_capture.grab(PLAY_MONITOR)
            image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
            batch = np.asarray([preprocess_image(image)], dtype="float32")
            prediction = model.predict(batch, verbose=0)
            result = int(np.argmax(prediction))

            if LABEL_ORDER[result] == "down":
                keyboard.press(keyboard.KEY_DOWN)
                key_down_pressed = True
            elif LABEL_ORDER[result] == "up":
                if key_down_pressed:
                    keyboard.release(keyboard.KEY_DOWN)
                    key_down_pressed = False

                keyboard.press(keyboard.KEY_UP)
                if tick < 1500:
                    time.sleep(0.3)
                elif tick < 5000:
                    time.sleep(0.2)
                else:
                    time.sleep(0.17)
                keyboard.press(keyboard.KEY_DOWN)
                keyboard.release(keyboard.KEY_DOWN)

            if (time.time() - frame_time) > 1:
                frame_time = time.time()
                print("-------------------------")
                print(
                    f"Down: {prediction[0][0]:.4f}\n"
                    f"Right: {prediction[0][1]:.4f}\n"
                    f"Up: {prediction[0][2]:.4f}\n"
                )
                tick += 1


if __name__ == "__main__":
    main()
