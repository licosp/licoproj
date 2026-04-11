"""Tests for the EmptyDirLinter module."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


import pytest
from lico_lint_empty_dir.main import EmptyDirLinter


@pytest.fixture  # type: ignore[misc]
def test_env(tmp_path: Path) -> Path:
    """Set up a temporary directory structure for testing.

    Args:
        tmp_path (Path): pytest fixture.

    Returns:
        Path: The root path of the test environment.
    """
    root = tmp_path / "test_root"
    root.mkdir()

    # Truly empty
    (root / "empty_dir").mkdir()

    # Contains an empty file
    (root / "non_empty_file").mkdir()
    (root / "non_empty_file" / "dummy.txt").write_text("content")

    # Contains an empty subdirectory
    (root / "non_empty_subdir").mkdir()
    (root / "non_empty_subdir" / "inner_empty").mkdir()

    return root


def test_is_empty_dir_logic(test_env: Path) -> None:
    """Test the core empty check logic."""
    linter = EmptyDirLinter()

    assert linter.is_empty_dir(str(test_env / "empty_dir")) is True
    assert linter.is_empty_dir(str(test_env / "non_empty_file")) is False
    assert linter.is_empty_dir(str(test_env / "non_empty_subdir")) is False


def test_scanner_reports_correctly(
    test_env: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test the full scanner reporting.

    Args:
        test_env (Path): Path fixture.
        capsys (pytest.CaptureFixture[str]): System capture.
    """
    linter = EmptyDirLinter(root_dir=str(test_env))
    linter.scan()

    captured = capsys.readouterr()
    assert "[Warning] Empty directory detected: empty_dir" in captured.out
    assert "non_empty_file" not in captured.out
    assert "non_empty_subdir" not in captured.out
