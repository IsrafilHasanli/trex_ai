# Contributing

Thanks for improving this project.

## Local setup

1. Create and activate a virtual environment.
2. Install dependencies with `pip install -r requirements-dev.txt`.
3. Run `pytest` before opening a pull request.
4. Run `ruff check .` for lint feedback.

## Repository hygiene

- Do not commit `.env` files, local credentials, or personal machine paths.
- Do not commit generated model weights such as `*.weights.h5`; publish large weights through GitHub Releases, cloud storage, or Git LFS instead.
- Keep training images intentional. Remove accidental screenshots before committing.
