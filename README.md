# Crypto Trading Bot

This repository contains a simple cryptocurrency trading bot that demonstrates a
moving average strategy. It is organized with separate folders for source code,
unit tests, and documentation.

## Setup

1. Clone the repository.
2. Create a Python virtual environment and install required dependencies.
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. Run the bot with `python src/trading_bot.py` to see the latest price and a
   naive trading signal based on a short moving average.
 
## Project Structure

- `src/` - source code for the trading bot
- `tests/` - unit tests for validating bot functionality
- `docs/` (optional) - additional project documentation

## Development Guidelines

- Keep all source code inside the `src/` directory.
- Place unit tests under the `tests/` directory and use `pytest` for running them.
- Update documentation in the `docs/` directory when necessary.
- Follow standard Python coding practices and write clear commit messages.
- Run tests with `pytest`.
