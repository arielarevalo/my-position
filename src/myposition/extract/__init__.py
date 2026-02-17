"""Extract layer of the ETL pipeline.

Scans input directories for markdown files, validates them, and produces
categorized file metadata.
"""

from myposition.extract.models import (
    CategorizationResult,
    FileCategory,
    FileMetadata,
    MisplacedFile,
)
from myposition.extract.scanner import Scanner

__all__ = [
    "CategorizationResult",
    "FileCategory",
    "FileMetadata",
    "MisplacedFile",
    "Scanner",
]
