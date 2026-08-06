"""
Base Loader for LawScape

Defines the common interface for all legal dataset loaders.

Author: Rushikesh Jagtap
Project: LawScape
"""

from abc import ABC, abstractmethod


class BaseLoader(ABC):
    """
    Abstract base class for all legal dataset loaders.
    """

    @abstractmethod
    def load(self, source: str):
        """
        Load raw legal data.
        """
        pass

    @abstractmethod
    def parse(self, raw_data):
        """
        Parse raw data into structured entities.
        """
        pass

    @abstractmethod
    def validate(self, parsed_data):
        """
        Validate parsed legal data.
        """
        pass