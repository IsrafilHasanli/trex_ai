# T-Rex AI

T-Rex AI is a Python project that trains and runs a small convolutional neural network to play the Chrome offline T-Rex runner game. It captures labeled screenshots of the game area, trains a classifier for `down`, `right`, and `up` actions, then uses the trained model to press keyboard controls while the game is running.

## Features

- Capture game screenshots and label them from keyboard input.
- Train a Keras/TensorFlow CNN from local screenshot data.
- Run live inference against the browser game using screen capture.
- Configure capture regions, model paths, and training settings with environment variables.
- Keep large generated model weights out of the Git repository.

## Tech Stack

- Python 3.10+
- Keras and TensorFlow
- NumPy
- Pillow
- MSS for screen capture
- keyboard for key detection and key presses
- scikit-learn for train/test splitting
- pytest and Ruff for development checks

## Installation

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements-dev.txt
```

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```

## Environment Setup

Copy the example environment file if you need to customize paths or screen capture coordinates:

```bash
copy .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

The app does not require secrets. `.env` is ignored so local paths and machine-specific settings stay private.

Important settings:

- `TREX_DATA_DIR`: directory containing labeled training screenshots.
- `TREX_MODEL_JSON`: path to the model architecture JSON file.
- `TREX_MODEL_WEIGHTS`: path to the trained weights file.
- `TREX_RECORD_TOP`, `TREX_RECORD_LEFT`: screen region used while collecting data.
- `TREX_PLAY_TOP`, `TREX_PLAY_LEFT`: screen region used while playing.
- `TREX_CAPTURE_WIDTH`, `TREX_CAPTURE_HEIGHT`: capture region size.

## Model Weights

The local `trex.weights.h5` file is a generated artifact and is intentionally ignored by Git. It is also larger than GitHub's normal 100 MB file limit.

To use the project after cloning:

1. Train a new model with `python train.py`, or
2. Download a published weights file separately and set `TREX_MODEL_WEIGHTS` to its path.

The included `model.json` stores the model architecture, but live play requires a matching weights file.

## Usage

Open the Chrome T-Rex game at `chrome://dino` or disconnect from the internet and open Chrome.

Collect training screenshots:

```bash
python get_data.py
```

Press `up`, `down`, or `right` while the game is visible to save labeled screenshots. Press `esc` to stop collection.

Train the model:

```bash
python train.py
```

Run the bot:

```bash
python trex_play.py
```

If installed as a package, the same commands are available as:

```bash
trex-collect
trex-train
trex-play
```

## Testing and Quality Checks

Run tests:

```bash
pytest
```

Run lint checks:

```bash
ruff check .
```

Compile Python files as a quick syntax check:

```bash
python -m compileall .
```

## Project Structure

```text
.
├── img/                    # Curated training screenshots
├── tests/                  # Unit tests
├── trex_ai/                # Application package
│   ├── collect_data.py     # Screenshot collection workflow
│   ├── config.py           # Environment-driven configuration
│   ├── model.py            # Keras model build/load/save helpers
│   ├── play.py             # Live game automation
│   ├── preprocessing.py    # Image and label preprocessing
│   └── train.py            # Training workflow
├── get_data.py             # Backward-compatible collection entry point
├── train.py                # Backward-compatible training entry point
├── trex_play.py            # Backward-compatible play entry point
├── model.json              # Model architecture
└── .env.example            # Safe configuration template
```

## Troubleshooting

- `FileNotFoundError: Model weights file not found`: train the model first or point `TREX_MODEL_WEIGHTS` to a downloaded weights file.
- The bot presses keys at the wrong time: adjust `TREX_PLAY_TOP` and `TREX_PLAY_LEFT` so the capture region matches the game area on your screen.
- Data collection saves blank or wrong images: adjust the record capture settings and make sure the game window is visible.
- Keyboard input does not work: the `keyboard` package can require elevated permissions on some systems.
- TensorFlow install fails: verify that your Python version is compatible with the TensorFlow version being installed.

## Security

This repository does not need API keys, passwords, tokens, or private URLs. Keep `.env`, generated weights, and other local-only files out of commits.
