"""Main entry point for myposition CLI."""

from myposition.cli import CLI


def main() -> None:
    """Run the CLI."""
    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()
