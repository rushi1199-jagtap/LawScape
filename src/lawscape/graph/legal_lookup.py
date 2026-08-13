"""
LawScape Legal Lookup

Combines graph search and graph query operations
into a single legal entity lookup interface.

Author: Rushikesh Jagtap
Project: LawScape
"""

from typing import Any, List

from lawscape.graph.graph_query import GraphQuery
from lawscape.graph.graph_search import GraphSearch


class LegalLookup:
    """
    High-level interface for searching and exploring
    legal entities in the LawScape graph.
    """

    def __init__(
        self,
        graph,
    ):
        self.query = GraphQuery(graph)
        self.search = GraphSearch(graph)

    # ---------------------------------------------------------
    # Search Entity
    # ---------------------------------------------------------

    def search_entity(
        self,
        text: str,
    ) -> List[str]:
        """
        Search the graph using general text search.
        """

        return self.search.search(text)

    # ---------------------------------------------------------
    # Get Entity
    # ---------------------------------------------------------

    def get_entity(
        self,
        node_id: str,
    ) -> dict:
        """
        Return complete data for a legal entity.
        """

        return self.query.get_node(node_id)

    # ---------------------------------------------------------
    # Get Parent
    # ---------------------------------------------------------

    def get_parent(
        self,
        node_id: str,
    ) -> str | None:
        """
        Return the direct legal parent of an entity.
        """

        return self.query.get_parent(node_id)

    # ---------------------------------------------------------
    # Get Children
    # ---------------------------------------------------------

    def get_children(
        self,
        node_id: str,
    ) -> List[str]:
        """
        Return entities directly contained by a node.
        """

        return self.query.get_children(
            node_id,
            "contains",
        )

    # ---------------------------------------------------------
    # Get Relationships
    # ---------------------------------------------------------

    def get_relationships(
        self,
        node_id: str,
    ) -> List[dict]:
        """
        Return all relationships associated with
        a legal entity.
        """

        return self.query.get_relationships(node_id)

    # ---------------------------------------------------------
    # Search and Get Entity
    # ---------------------------------------------------------

    def search_and_get(
        self,
        text: str,
    ) -> List[dict]:
        """
        Search for entities and return their node data.
        """

        node_ids = self.search_entity(text)

        results = []

        for node_id in node_ids:

            results.append(
                {
                    "node_id": node_id,
                    "data": self.get_entity(node_id),
                }
            )

        return results