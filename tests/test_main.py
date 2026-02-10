"""Tests for main module."""

from typing import TYPE_CHECKING

import pytest

from my_position.main import main

if TYPE_CHECKING:
    pass


def test_main(capsys: "pytest.CaptureFixture[str]") -> None:
    """Test main function prints usage information."""
    main()
    captured = capsys.readouterr()
    assert "my-position - Synthesize positions" in captured.out
    assert "Usage:" in captured.out
    assert "Commands:" in captured.out
    assert "ingest" in captured.out
    assert "synthesize" in captured.out
    assert "export" in captured.out
