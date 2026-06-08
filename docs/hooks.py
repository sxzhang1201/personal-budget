"""MkDocs hooks for the personal-budget documentation site."""

from __future__ import annotations

import shutil
from pathlib import Path


def on_post_build(*, config, **kwargs) -> None:
    """Use the interactive dashboard as the site home page."""
    site_dir = Path(config["site_dir"])
    dashboard = site_dir / "dashboard.html"
    if dashboard.exists():
        shutil.copy2(dashboard, site_dir / "index.html")
