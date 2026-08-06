"""
Legal Data Models for LawScape

Defines structured representations of legal entities
produced by the data ingestion pipeline.

Author: Rushikesh Jagtap
Project: LawScape
"""

from dataclasses import dataclass


@dataclass
class LegalPart:
    """
    Represents a Part of a legal document.
    """

    part_number: str
    title: str


@dataclass
class LegalArticle:
    """
    Represents an Article of a legal document.
    """

    article_number: str
    content: str
    part_number: str | None = None