import os
import shutil
import pytest
from lico_lint_empty_dir.main import EmptyDirLinter

@pytest.fixture
def test_env(tmp_path):
    """Set up a temporary directory structure for testing."""
    root = tmp_path / "test_root"
    root.mkdir()
    
    # Truly empty
    (root / "empty_dir").mkdir()
    
    # Non-empty (file)
    (root / "non_empty_file").mkdir()
    (root / "non_empty_file" / "file.txt").write_text("content")
    
    # Non-empty (subdir)
    (root / "non_empty_subdir").mkdir()
    (root / "non_empty_subdir" / "subdir").mkdir()
    
    # Ignored dir (should be ignored by scanner)
    (root / ".git").mkdir()
    
    return root

def test_is_empty_dir_logic(test_env):
    """Test the core empty check logic."""
    linter = EmptyDirLinter()
    assert linter.is_empty_dir(str(test_env / "empty_dir")) is True
    assert linter.is_empty_dir(str(test_env / "non_empty_file")) is False
    assert linter.is_empty_dir(str(test_env / "non_empty_subdir")) is False

def test_scanner_reports_correctly(test_env, capsys):
    """Test the full scanner reporting."""
    linter = EmptyDirLinter(root_dir=str(test_env))
    linter.scan()
    
    captured = capsys.readouterr()
    assert "[Warning] Empty directory detected: empty_dir" in captured.out
    assert "non_empty_file" not in captured.out
    assert ".git" not in captured.out
    assert "Scan Complete: Issues found" in captured.out
