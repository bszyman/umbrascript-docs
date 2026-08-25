"""Build hooks for files consumed directly by external services."""

from pathlib import Path
from shutil import copyfile


def on_post_build(*, config, **kwargs):
    """Publish the Marketplace README as raw Markdown beside its JSON metadata."""
    source = Path(config["docs_dir"]) / "umbraco-marketplace-readme.md"
    destination = Path(config["site_dir"]) / source.name
    copyfile(source, destination)
