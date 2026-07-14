"""
Common properties shared by all legal entities.

Author: Rushikesh Jagtap
Project: LawScape
"""

from enum import Enum


class CommonProperty(str, Enum):
    """
    Properties that every legal entity must have.
    """

    ID = "id"

    NAME = "name"

    TITLE = "title"

    DESCRIPTION = "description"

    JURISDICTION = "jurisdiction"

    VERSION = "version"

    STATUS = "status"

    EFFECTIVE_DATE = "effective_date"

    CREATED_AT = "created_at"

    UPDATED_AT = "updated_at"

    SOURCE = "source"

    CONFIDENCE = "confidence"