"""Tests for the ConfigManager."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from lico_config.main import ConfigManager

# Expected values from test_project.json
EXPECTED_SLEEP = 10
EXPECTED_H_BRANCH = "test-trunk"
EXPECTED_W_BRANCH = "test-windows"
EXPECTED_TARGETS = ["src", "tests"]
EXPECTED_APP_CMD = ["test_app.exe", "--arg"]
EXPECTED_LABEL = "TestApp.exe"
EXPECTED_TITLE = "TestApp"


@pytest.fixture
def test_config_path() -> Path:
    """Path to the test project.json.

    Returns:
        Path: Path.
    """
    return Path(__file__).parent / "test_project.json"


@pytest.fixture
def config(test_config_path: Path) -> ConfigManager:
    """ConfigManager instance using test_project.json.

    Args:
        test_config_path (Path): Path to test_project.json.

    Returns:
        ConfigManager: instance.
    """
    return ConfigManager(config_path=test_config_path)


def test_app_properties(config: ConfigManager) -> None:
    """Test application-related properties.

    Args:
        config (ConfigManager): instance.
    """
    assert config.sleep_duration == EXPECTED_SLEEP
    assert config.sleep_start == EXPECTED_SLEEP
    assert config.sleep_end == EXPECTED_SLEEP
    assert config.app_start_command == EXPECTED_APP_CMD
    assert config.window_title == EXPECTED_TITLE
    assert config.running_app_name == EXPECTED_LABEL


def test_sync_properties(config: ConfigManager) -> None:
    """Test synchronization-related properties.

    Args:
        config (ConfigManager): instance.
    """
    assert config.hub_branch == EXPECTED_H_BRANCH
    assert config.dest_branch == EXPECTED_W_BRANCH
    assert config.sync_targets == EXPECTED_TARGETS


def test_system_paths(config: ConfigManager) -> None:
    """Test system-related path properties.

    Args:
        config (ConfigManager): instance.
    """
    assert config.system_root == Path("/mnt/c/sys")
    assert config.system_task_list == "tasklist.exe"
    assert config.system_task_kill == "taskkill.exe"
    assert config.shell_exe == "powershell.exe"
    assert config.shell_dir == Path("/mnt/c/sys/ps")


def test_tool_paths(config: ConfigManager) -> None:
    """Test tool-related path properties.

    Args:
        config (ConfigManager): instance.
    """
    assert config.uv_path == Path("/mnt/c/bin/uv.exe")
    assert config.git_exe == "/mnt/c/bin/git.exe"


def test_vision_paths(config: ConfigManager) -> None:
    """Test vision-related path properties.

    Args:
        config (ConfigManager): instance.
    """
    expected_capture = Path(
        "/mnt/d/test/root/pkg/vision/src/vision/capture.ps1"
    )
    expected_screen = Path("/mnt/d/test/root/screen.webp")

    assert config.capture_script_path == expected_capture
    assert config.output_image_path == expected_screen


def test_derived_roots(config: ConfigManager) -> None:
    """Test derived root properties.

    Args:
        config (ConfigManager): instance.
    """
    # project_root is derived from parents[4] of capture_script_path
    # /mnt/d/test/root/pkg/vision/src/vision/capture.ps1
    # 0: vision, 1: src, 2: vision, 3: pkg, 4: root
    expected_root = Path("/mnt/d/test/root")
    assert config.project_root == expected_root
    assert config.git_workspace_root == expected_root


def test_validation_missing_section(tmp_path: Path) -> None:
    """Test validation fails when a section is missing.

    Args:
        tmp_path (Path): pytest fixture.
    """
    config_file = tmp_path / "invalid.json"
    config_file.write_text(
        '{"app": {"sleep": 1, "label": "x", "commands": []}}'
    )

    with pytest.raises(TypeError, match="Missing or invalid 'sync' section"):
        ConfigManager(config_path=config_file)


def test_validation_wrong_type(tmp_path: Path) -> None:
    """Test validation fails when a value has the wrong type.

    Args:
        tmp_path (Path): pytest fixture.
    """
    config_file = tmp_path / "invalid.json"
    # commands should be a list, not a string
    content = {
        "app": {"sleep": 1, "label": "x", "commands": "not-a-list"},
        "sync": {"branch": {"hub": "x", "windows": "y"}, "target": []},
        "windows": {},
    }
    config_file.write_text(json.dumps(content))

    with pytest.raises(TypeError, match="'app.commands' must be a list"):
        ConfigManager(config_path=config_file)


def test_validation_non_absolute_path(tmp_path: Path) -> None:
    """Test validation fails when a Windows path is not absolute.

    Args:
        tmp_path (Path): pytest fixture.
    """
    config_file = tmp_path / "invalid.json"
    content = {
        "app": {"sleep": 1, "label": "x", "commands": []},
        "sync": {"branch": {"hub": "x", "windows": "y"}, "target": []},
        "windows": {"tools": {"uv": "relative/path/uv.exe"}},
    }
    config_file.write_text(json.dumps(content))

    with pytest.raises(TypeError, match="Path for 'uv' must be absolute"):
        ConfigManager(config_path=config_file)


def test_validation_windows_style_path(tmp_path: Path) -> None:
    """Test validation fails when a Windows-style (C:/) path is used.

    Args:
        tmp_path (Path): pytest fixture.
    """
    config_file = tmp_path / "invalid.json"
    content = {
        "app": {"sleep": 1, "label": "x", "commands": []},
        "sync": {"branch": {"hub": "x", "windows": "y"}, "target": []},
        "windows": {"tools": {"uv": "C:/bin/uv.exe"}},
    }
    config_file.write_text(json.dumps(content))

    with pytest.raises(TypeError, match="Path for 'uv' must be absolute"):
        ConfigManager(config_path=config_file)
