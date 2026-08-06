"""
Constitution Loader for LawScape

Loads and parses the Constitution of India.

Author: Rushikesh Jagtap
Project: LawScape
"""

from pathlib import Path

from lawscape.data_ingestion.base_loader import BaseLoader
from lawscape.data_ingestion.parser import LegalDocumentParser


class ConstitutionLoader(BaseLoader):
    """
    Loader for Constitution of India datasets.
    """

    def __init__(self):
        self.parser = LegalDocumentParser()

    def load(self, source: str) -> str:
        """
        Load Constitution text from file.
        """

        path = Path(source)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {source}"
            )

        return path.read_text(encoding="utf-8")

    def parse(self, raw_data: str) -> dict:
        """
        Parse Constitution text into structured legal entities.
        """

        parts = self.parser.extract_parts(raw_data)

        articles = []

        for part in parts:
            part_pattern = f"PART {part.part_number}"

            part_start = raw_data.find(part_pattern)

            if part_start == -1:
                continue

            next_part_start = raw_data.find(
                "PART ",
                part_start + len(part_pattern),
            )

            if next_part_start == -1:
                part_text = raw_data[part_start:]
            else:
                part_text = raw_data[
                    part_start:next_part_start
                ]

            part_articles = self.parser.extract_articles(
                part_text,
                part_number=part.part_number,
            )

            articles.extend(part_articles)

        return {
            "parts": parts,
            "articles": articles,
        }

    def validate(self, parsed_data: dict) -> bool:
        """
        Validate parsed Constitution data.
        """

        if not parsed_data:
            return False

        if "parts" not in parsed_data:
            return False

        if "articles" not in parsed_data:
            return False

        if not isinstance(parsed_data["parts"], list):
            return False

        if not isinstance(parsed_data["articles"], list):
            return False

        return True