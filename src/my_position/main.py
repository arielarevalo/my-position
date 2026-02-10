"""Main entry point for my-position CLI."""


def main() -> None:
    """Display usage information for my-position CLI."""
    print("my-position - Synthesize positions from your conversations and notes")
    print()
    print("Usage: my-position [command] [options]")
    print()
    print("Commands:")
    print("  ingest     Ingest Markdown files and extract topics")
    print("  synthesize Generate position entries from topics")
    print("  export     Export positions to various formats")
    print()
    print("Run 'my-position [command] --help' for more information on a command.")
    print()
    print("Note: Full implementation coming soon. This is a work in progress.")


if __name__ == "__main__":
    main()
