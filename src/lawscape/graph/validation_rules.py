"""
LawScape Graph Validation Rules

Defines valid relationships between legal entity types.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.ontology.entity_types import LegalEntityType
from lawscape.ontology.relationship_types import LegalRelationshipType


VALID_RELATIONSHIPS = {
    LegalEntityType.CONSTITUTION.value: {
        LegalRelationshipType.CONTAINS.value: {
            LegalEntityType.PART.value,
            LegalEntityType.ARTICLE.value,
            LegalEntityType.CHAPTER.value,
        },
    },

    LegalEntityType.PART.value: {
        LegalRelationshipType.CONTAINS.value: {
            LegalEntityType.ARTICLE.value,
            LegalEntityType.SECTION.value,
        },
    },

    LegalEntityType.CHAPTER.value: {
        LegalRelationshipType.CONTAINS.value: {
            LegalEntityType.SECTION.value,
            LegalEntityType.ARTICLE.value,
        },
    },

    LegalEntityType.ACT.value: {
        LegalRelationshipType.CONTAINS.value: {
            LegalEntityType.CHAPTER.value,
            LegalEntityType.SECTION.value,
        },

        LegalRelationshipType.AMENDS.value: {
            LegalEntityType.ACT.value,
            LegalEntityType.SECTION.value,
        },

        LegalRelationshipType.REPEALS.value: {
            LegalEntityType.ACT.value,
            LegalEntityType.SECTION.value,
        },
    },

    LegalEntityType.JUDGMENT.value: {
        LegalRelationshipType.INTERPRETS.value: {
            LegalEntityType.ACT.value,
            LegalEntityType.SECTION.value,
            LegalEntityType.ARTICLE.value,
        },

        LegalRelationshipType.CITES.value: {
            LegalEntityType.ACT.value,
            LegalEntityType.SECTION.value,
            LegalEntityType.ARTICLE.value,
            LegalEntityType.JUDGMENT.value,
        },
    },
}