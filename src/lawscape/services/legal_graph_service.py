"""
LawScape Legal Graph Service

Provides a high-level service interface for interacting
with the LawScape legal knowledge graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from typing import Any, List

import networkx as nx

from lawscape.graph.legal_lookup import LegalLookup


class LegalGraphService:
    """
    High-level service layer for legal graph operations.

    This class acts as the main interface between the
    knowledge graph and future API, dashboard, or CLI layers.
    """

    def __init__(
        self,
        graph: nx.MultiDiGraph,
    ):
        self.graph = graph
        self.lookup = LegalLookup(graph)

    # ---------------------------------------------------------
    # Entity Search
    # ---------------------------------------------------------

    def search_entities(
        self,
        text: str,
    ) -> List[str]:
        """
        Search legal entities using text.
        """

        return self.lookup.search_entity(text)

    # ---------------------------------------------------------
    # Entity Details
    # ---------------------------------------------------------

    def get_entity(
        self,
        node_id: str,
    ) -> dict:
        """
        Return complete information about a legal entity.
        """

        return self.lookup.get_entity(node_id)

    # ---------------------------------------------------------
    # Entity Parent
    # ---------------------------------------------------------

    def get_parent(
        self,
        node_id: str,
    ) -> str | None:
        """
        Return the direct parent of a legal entity.
        """

        return self.lookup.get_parent(node_id)

    # ---------------------------------------------------------
    # Entity Children
    # ---------------------------------------------------------

    def get_children(
        self,
        node_id: str,
    ) -> List[str]:
        """
        Return direct child entities.
        """

        return self.lookup.get_children(node_id)

    # ---------------------------------------------------------
    # Entity Relationships
    # ---------------------------------------------------------

    def get_relationships(
        self,
        node_id: str,
    ) -> List[dict]:
        """
        Return all relationships associated with an entity.
        """

        return self.lookup.get_relationships(node_id)

    # ---------------------------------------------------------
    # Search and Get
    # ---------------------------------------------------------

    def search_and_get(
        self,
        text: str,
    ) -> List[dict]:
        """
        Search for entities and return their complete data.
        """

        return self.lookup.search_and_get(text)

    # ---------------------------------------------------------
    # Graph Statistics
    # ---------------------------------------------------------

    def get_graph_stats(self) -> dict:
        """
        Return basic graph statistics.
        """

        return {
            "nodes": self.graph.number_of_nodes(),
            "edges": self.graph.number_of_edges(),
        }