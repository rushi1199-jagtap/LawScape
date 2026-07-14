"""
LawScape Legal Relationship Definitions

This module defines all supported relationship types
between legal entities in the Living Legal Knowledge Graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from enum import Enum


class LegalRelationshipType(str, Enum):
    """
    Official relationship types used throughout LawScape.
    """

    CONTAINS = "contains"

    AMENDS = "amends"

    MODIFIES = "modifies"

    REPEALS = "repeals"

    REPLACES = "replaces"

    INTERPRETS = "interprets"

    CITES = "cites"

    REFERS_TO = "refers_to"

    DEPENDS_ON = "depends_on"

    CONFLICTS_WITH = "conflicts_with"

    GOVERNS = "governs"

    IMPLEMENTS = "implements"

    APPLICABLE_TO = "applicable_to"

    ENFORCED_BY = "enforced_by"

    AFFECTS = "affects"

    RELATED_TO = "related_to"

    PRECEDES = "precedes"

    SUCCEEDS = "succeeds"

    HAS_VERSION = "has_version"

    SUPERSEDES = "supersedes"