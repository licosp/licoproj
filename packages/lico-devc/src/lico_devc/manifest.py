"""Habitat Manifest (habitat.json) type definitions and loader."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, TypedDict, cast

if TYPE_CHECKING:
    from pathlib import Path


class BootConfig(TypedDict, total=False):
    """Configuration for boot operations."""

    cwd: str


class AccountConfig(TypedDict, total=False):
    """Configuration for a resident's system account."""

    uid: int
    gid: int
    shell: str
    sudo: bool


class RepoSource(TypedDict, total=False):
    """Source configuration for a repository."""

    remote: str
    local: str


class RepoConfig(TypedDict):
    """Configuration for a managed repository."""

    name: str
    source_from: str
    source: RepoSource


class CrewMember(TypedDict, total=False):
    """Configuration for a village resident (crew member)."""

    name: str
    account: AccountConfig
    alias: list[str]
    worktree: list[str]


class EnvConfig(TypedDict, total=False):
    """Configuration for environment and secret loading."""

    name: str
    path: str
    # Key 'env-keys' in JSON is accessed via string due to dash.


class HabitatConfig(TypedDict, total=False):
    """Root configuration for the Lico habitat."""

    boot: BootConfig
    env: EnvConfig
    repos: list[RepoConfig]
    crew: list[CrewMember]
    site_config: dict[str, str]


def load_habitat_config(path: Path) -> HabitatConfig:
    """Load and cast the habitat configuration.

    Args:
        path: Path to habitat.json.

    Returns:
        The cast HabitatConfig object.
    """
    with path.open("r", encoding="utf-8") as f:
        return cast("HabitatConfig", json.load(f))
