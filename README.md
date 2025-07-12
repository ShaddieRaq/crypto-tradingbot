# Crypto Trading Bot

This repository contains a simple cryptocurrency trading bot. It is organized with separate folders for source code, unit tests, and documentation.

## Setup

1. Clone the repository.
2. Create a Python virtual environment and install required dependencies.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   This installs packages like `requests`, `pandas`, and `ccxt`.
3. Run the bot from the `src/` directory as needed.

## Development Guidelines

- Keep all source code inside the `src/` directory.
- Place unit tests under the `tests/` directory and use `pytest` for running them.
- Update documentation in the `docs/` directory when necessary.
- Follow standard Python coding practices and write clear commit messages.
