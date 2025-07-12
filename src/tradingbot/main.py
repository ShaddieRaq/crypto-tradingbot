"""Command-line entry for trading bot."""

import argparse


def main(argv=None):
    """Simple CLI stub that prints a placeholder message."""
    parser = argparse.ArgumentParser(description="Trading bot CLI")
    parser.parse_args(argv)
    print("Trading bot initialized")


if __name__ == "__main__":
    main()
