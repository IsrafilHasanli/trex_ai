from pathlib import Path

import numpy as np
import pytest
from PIL import Image

from trex_ai.config import LABEL_ORDER, MODEL_INPUT_SHAPE
from trex_ai.preprocessing import label_from_path, one_hot_encode, preprocess_image


def test_preprocess_image_returns_normalized_model_shape():
    image = Image.new("RGB", (250, 150), color=(128, 128, 128))

    result = preprocess_image(image)

    assert result.shape == MODEL_INPUT_SHAPE
    assert result.dtype == np.float32
    assert 0.0 <= float(result.min()) <= float(result.max()) <= 1.0


def test_one_hot_encode_uses_stable_label_order():
    result = one_hot_encode(["down", "right", "up"])

    assert result.tolist() == np.eye(len(LABEL_ORDER), dtype="float32").tolist()


def test_one_hot_encode_rejects_unknown_labels():
    with pytest.raises(ValueError, match="Unknown labels"):
        one_hot_encode(["jump"])


def test_label_from_path_reads_prefix_before_first_underscore():
    assert label_from_path(Path("up_example_1.png")) == "up"
