"""Capture labeled screenshots for training data."""

from __future__ import annotations

import time
import uuid

from mss import mss
from PIL import Image

from .config import DATA_DIR, RECORD_MONITOR


def save_capture(
    screen_capture,
    monitor: dict[str, int],
    label: str,
    record_id: uuid.UUID,
    index: int,
) -> None:
    screenshot = screen_capture.grab(monitor)
    image = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    image.save(DATA_DIR / f"{label}_{record_id}_{index}.png")


def main() -> None:
    import keyboard

    is_exit = False
    record_id = uuid.uuid4()
    counter = 0

    def request_exit() -> None:
        nonlocal is_exit
        is_exit = True

    keyboard.add_hotkey("esc", request_exit)

    with mss() as screen_capture:
        while not is_exit:
            try:
                if keyboard.is_pressed(keyboard.KEY_UP):
                    label = keyboard.KEY_UP
                elif keyboard.is_pressed(keyboard.KEY_DOWN):
                    label = keyboard.KEY_DOWN
                elif keyboard.is_pressed("right"):
                    label = "right"
                else:
                    continue

                counter += 1
                print(f"{label}: {counter}")
                save_capture(screen_capture, RECORD_MONITOR, label, record_id, counter)
                time.sleep(0.1)
            except RuntimeError:
                continue


if __name__ == "__main__":
    main()
