"""Image preprocessing and dataset loading helpers."""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

import numpy as np
from PIL import Image

from .config import IMAGE_HEIGHT, IMAGE_WIDTH, LABEL_ORDER, MODEL_INPUT_SHAPE


def normalize_label(label: str) -> str:
    return label.strip().lower()


def preprocess_image(image: Image.Image) -> np.ndarray:
    """Convert a screenshot into the tensor shape expected by the saved model."""
    grayscale = image.convert("L").resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    pixels = np.asarray(grayscale, dtype="float32") / 255.0
    return pixels.reshape(MODEL_INPUT_SHAPE)


def label_from_path(path: Path) -> str:
    return normalize_label(path.name.split("_", 1)[0])


def one_hot_encode(labels: Iterable[str]) -> np.ndarray:
    labels = [normalize_label(label) for label in labels]
    label_to_index = {label: index for index, label in enumerate(LABEL_ORDER)}

    unknown_labels = sorted(set(labels) - set(label_to_index))
    if unknown_labels:
        raise ValueError(f"Unknown labels found in dataset: {', '.join(unknown_labels)}")

    encoded = np.zeros((len(labels), len(LABEL_ORDER)), dtype="float32")
    for row, label in enumerate(labels):
        encoded[row, label_to_index[label]] = 1.0
    return encoded


def load_dataset(data_dir: Path) -> tuple[np.ndarray, np.ndarray]:
    image_paths = sorted(Path(data_dir).glob("*.png"))
    if not image_paths:
        raise FileNotFoundError(f"No PNG training images found in {data_dir}")

    images = []
    labels = []
    for image_path in image_paths:
        with Image.open(image_path) as image:
            images.append(preprocess_image(image))
        labels.append(label_from_path(image_path))

    return np.asarray(images, dtype="float32"), one_hot_encode(labels)
