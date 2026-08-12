"""
Constitution Graph Builder for LawScape

Converts structured Constitution data into a legal knowledge graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.data_ingestion.data_models import (
    LegalArticle,
    LegalPart,
)
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.ontology.entity_types import LegalEntityType


class ConstitutionGraphBuilder:
    """
    Builds a graph representation of the Constitution.
    """

    def __init__(self, graph_builder: LawGraphBuilder):
        self.graph_builder = graph_builder

    # ---------------------------------------------------------
    # Constitution Operations
    # ---------------------------------------------------------

    def add_constitution(self) -> str:
        """
        Add the Constitution as the root graph node.
        """

        node_id = "CONSTITUTION"

        self.graph_builder.add_node(
            node_id=node_id,
            entity_type=LegalEntityType.CONSTITUTION.value,
            title="Constitution of India",
        )

        return node_id

    # ---------------------------------------------------------
    # Part Operations
    # ---------------------------------------------------------

    def add_part(self, part: LegalPart) -> str:
        """
        Add a Constitution Part as a graph node.
        """

        node_id = f"PART_{part.part_number}"

        self.graph_builder.add_node(
            node_id=node_id,
            entity_type=LegalEntityType.PART.value,
            title=part.title,
            part_number=part.part_number,
        )

        return node_id

    # ---------------------------------------------------------
    # Article Operations
    # ---------------------------------------------------------

    def add_article(
        self,
        article: LegalArticle,
    ) -> str:
        """
        Add an Article as a graph node.
        """

        node_id = f"ARTICLE_{article.article_number}"

        self.graph_builder.add_node(
            node_id=node_id,
            entity_type=LegalEntityType.ARTICLE.value,
            title=f"Article {article.article_number}",
            article_number=article.article_number,
            content=article.content,
            part_number=article.part_number,
        )

        return node_id

    # ---------------------------------------------------------
    # Relationship Operations
    # ---------------------------------------------------------

    def connect_constitution_part(
        self,
        part: LegalPart,
    ) -> None:
        """
        Create a contains relationship between
        Constitution and Part.
        """

        self.graph_builder.add_edge(
            source="CONSTITUTION",
            target=f"PART_{part.part_number}",
            relationship="contains",
        )

    def connect_part_article(
        self,
        part: LegalPart,
        article: LegalArticle,
    ) -> None:
        """
        Create a contains relationship between
        Part and Article.
        """

        part_id = f"PART_{part.part_number}"
        article_id = f"ARTICLE_{article.article_number}"

        self.graph_builder.add_edge(
            source=part_id,
            target=article_id,
            relationship="contains",
        )

    # ---------------------------------------------------------
    # Graph Construction
    # ---------------------------------------------------------

    def build(
        self,
        parts: list[LegalPart],
        articles: list[LegalArticle],
    ) -> LawGraphBuilder:
        """
        Build the Constitution graph from structured data.
        """

        # Add Constitution root node
        self.add_constitution()

        # Add all Parts
        for part in parts:
            self.add_part(part)

        # Connect Constitution to Parts
        for part in parts:
            self.connect_constitution_part(part)

        # Add all Articles
        for article in articles:
            self.add_article(article)

        # Connect Articles to their corresponding Parts
        for article in articles:

            if article.part_number is None:
                continue

            part = next(
                (
                    item
                    for item in parts
                    if item.part_number == article.part_number
                ),
                None,
            )

            if part is None:
                continue

            self.connect_part_article(
                part,
                article,
            )

        return self.graph_builder