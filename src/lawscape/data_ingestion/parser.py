"""
Legal Document Parser for LawScape

Provides reusable parsing utilities for legal documents.

Author: Rushikesh Jagtap
Project: LawScape
"""

from __future__ import annotations

import re

from lawscape.data_ingestion.data_models import (
    LegalArticle,
    LegalPart,
)


class LegalDocumentParser:
    """
    Parses structured legal document text.
    """

    ARTICLE_PATTERN = re.compile(
        r"(?m)^Article\s+(\d+[A-Za-z]?)\s*$"
    )

    PART_PATTERN = re.compile(
        r"(?m)^PART\s+([IVXLCDM]+)\s*$"
    )

    def extract_parts(self, text: str) -> list[LegalPart]:
        """
        Extract legal parts from document text.
        """

        matches = list(self.PART_PATTERN.finditer(text))

        parts = []

        for match in matches:
            part_number = match.group(1)

            parts.append(
                LegalPart(
                    part_number=part_number,
                    title=f"Part {part_number}",
                )
            )

        return parts

    def extract_articles(
        self,
        text: str,
        part_number: str | None = None,
    ) -> list[LegalArticle]:
        """
        Extract legal articles from document text.
        """

        matches = list(self.ARTICLE_PATTERN.finditer(text))

        articles = []

        for index, match in enumerate(matches):

            article_number = match.group(1)

            start = match.end()

            if index + 1 < len(matches):
                end = matches[index + 1].start()
            else:
                end = len(text)

            content = text[start:end].strip()

            articles.append(
                LegalArticle(
                    article_number=article_number,
                    content=content,
                    part_number=part_number,
                )
            )

        return articles