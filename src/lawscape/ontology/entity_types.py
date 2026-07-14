"""
LawScape Legal Entity Definitions

This module defines all supported legal entity types used
throughout the LawScape platform.

Author: Rushikesh Jagtap
Project: LawScape
"""

from enum import Enum


class LegalEntityType(str, Enum):
    """
    Official legal entity types supported by LawScape.

    These values are used consistently across:
    - Knowledge Graph Construction
    - Neo4j
    - Graph Neural Networks
    - Explainability
    - Dashboard
    """

    CONSTITUTION = "Constitution"
    ARTICLE = "Article"
    ACT = "Act"
    CHAPTER = "Chapter"
    SECTION = "Section"
    SUBSECTION = "Subsection"
    RULE = "Rule"
    REGULATION = "Regulation"
    AMENDMENT = "Amendment"
    BILL = "Bill"
    NOTIFICATION = "Notification"
    CIRCULAR = "Circular"
    JUDGMENT = "Judgment"
    COURT = "Court"
    JUDGE = "Judge"
    MINISTRY = "Ministry"
    DEPARTMENT = "Department"
    LEGAL_CONCEPT = "LegalConcept"
    LEGAL_PRINCIPLE = "LegalPrinciple"
    INDUSTRY = "Industry"
    COMPANY = "Company"
    TREATY = "InternationalTreaty"
    