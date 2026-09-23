"""Model creation, loading, and persistence."""

from __future__ import annotations

from pathlib import Path

from .config import MODEL_INPUT_SHAPE


def build_model(num_classes: int = 3):
    from keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPooling2D
    from keras.models import Sequential

    model = Sequential(
        [
            Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=MODEL_INPUT_SHAPE),
            Conv2D(64, kernel_size=(3, 3), activation="relu"),
            MaxPooling2D(pool_size=(2, 2)),
            Dropout(0.25),
            Flatten(),
            Dense(128, activation="relu"),
            Dropout(0.4),
            Dense(num_classes, activation="softmax"),
        ]
    )
    model.compile(loss="categorical_crossentropy", optimizer="Adam", metrics=["accuracy"])
    return model


def save_model(model, model_json_path: Path, weights_path: Path) -> None:
    model_json_path.write_text(model.to_json(), encoding="utf-8")
    model.save_weights(weights_path)


def load_model(model_json_path: Path, weights_path: Path):
    from keras.models import model_from_json

    if not model_json_path.exists():
        raise FileNotFoundError(f"Model architecture file not found: {model_json_path}")
    if not weights_path.exists():
        raise FileNotFoundError(
            f"Model weights file not found: {weights_path}. "
            "Train the model first or provide TREX_MODEL_WEIGHTS."
        )

    model = model_from_json(model_json_path.read_text(encoding="utf-8"))
    model.load_weights(weights_path)
    return model
