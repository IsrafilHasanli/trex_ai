"""Project configuration with environment-variable overrides."""

from __future__ import annotations

import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

if load_dotenv is not None:
    load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def project_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else PROJECT_ROOT / path


DATA_DIR = project_path(os.getenv("TREX_DATA_DIR", "img"))
MODEL_JSON_PATH = project_path(os.getenv("TREX_MODEL_JSON", "model.json"))
MODEL_WEIGHTS_PATH = project_path(os.getenv("TREX_MODEL_WEIGHTS", "trex.weights.h5"))

IMAGE_WIDTH = int(os.getenv("TREX_IMAGE_WIDTH", "125"))
IMAGE_HEIGHT = int(os.getenv("TREX_IMAGE_HEIGHT", "50"))
MODEL_INPUT_SHAPE = (IMAGE_WIDTH, IMAGE_HEIGHT, 1)

TRAIN_TEST_SIZE = float(os.getenv("TREX_TEST_SIZE", "0.25"))
TRAIN_RANDOM_STATE = int(os.getenv("TREX_RANDOM_STATE", "2"))
TRAIN_EPOCHS = int(os.getenv("TREX_EPOCHS", "35"))
TRAIN_BATCH_SIZE = int(os.getenv("TREX_BATCH_SIZE", "64"))

RECORD_MONITOR = {
    "top": int(os.getenv("TREX_RECORD_TOP", "466")),
    "left": int(os.getenv("TREX_RECORD_LEFT", "668")),
    "width": int(os.getenv("TREX_CAPTURE_WIDTH", "250")),
    "height": int(os.getenv("TREX_CAPTURE_HEIGHT", "150")),
}

PLAY_MONITOR = {
    "top": int(os.getenv("TREX_PLAY_TOP", "466")),
    "left": int(os.getenv("TREX_PLAY_LEFT", "650")),
    "width": int(os.getenv("TREX_CAPTURE_WIDTH", "250")),
    "height": int(os.getenv("TREX_CAPTURE_HEIGHT", "150")),
}

LABEL_ORDER = ("down", "right", "up")
