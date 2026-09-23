"""Train the T-Rex controller model from captured screenshots."""

from __future__ import annotations

import numpy as np
from sklearn.model_selection import train_test_split

from .config import (
    DATA_DIR,
    LABEL_ORDER,
    MODEL_JSON_PATH,
    MODEL_WEIGHTS_PATH,
    TRAIN_BATCH_SIZE,
    TRAIN_EPOCHS,
    TRAIN_RANDOM_STATE,
    TRAIN_TEST_SIZE,
)
from .model import build_model, save_model
from .preprocessing import load_dataset


def main() -> None:
    images, labels = load_dataset(DATA_DIR)
    label_indices = np.argmax(labels, axis=1)

    train_x, test_x, train_y, test_y = train_test_split(
        images,
        labels,
        test_size=TRAIN_TEST_SIZE,
        random_state=TRAIN_RANDOM_STATE,
        stratify=label_indices,
    )

    model = build_model(num_classes=len(LABEL_ORDER))
    model.fit(train_x, train_y, epochs=TRAIN_EPOCHS, batch_size=TRAIN_BATCH_SIZE)

    train_score = model.evaluate(train_x, train_y, verbose=0)
    test_score = model.evaluate(test_x, test_y, verbose=0)
    print(f"Training accuracy: {train_score[1] * 100:.2f}%")
    print(f"Test accuracy: {test_score[1] * 100:.2f}%")

    save_model(model, MODEL_JSON_PATH, MODEL_WEIGHTS_PATH)
    print(f"Saved model architecture to {MODEL_JSON_PATH}")
    print(f"Saved model weights to {MODEL_WEIGHTS_PATH}")


if __name__ == "__main__":
    main()
