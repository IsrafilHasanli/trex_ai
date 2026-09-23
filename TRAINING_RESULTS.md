# Training Results

The committed model weights in `models/trex.weights.h5` were regenerated from the curated screenshots in `data/training`.

## Latest Run

- Date: 2026-09-23
- Training command: `python train.py`
- Dataset: 146 labeled screenshots
- Labels: `down`, `right`, `up`
- Epochs: 35
- Batch size: 64
- Train/test split: 75% / 25%
- Random state: 2
- Training accuracy: 99.08%
- Test accuracy: 91.89%
- Output architecture: `models/model.json`
- Output weights: `models/trex.weights.h5`

## Notes

- The weights file is stored with Git LFS because it is larger than GitHub's normal 100 MB file limit.
- Small differences in accuracy can happen when retraining because TensorFlow/Keras operations and random initialization are not fully deterministic by default.
- The dataset is intentionally small, so the test accuracy should be treated as a quick validation signal rather than a broad benchmark.
