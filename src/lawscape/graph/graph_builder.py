"""
LawScape Graph Builder

Responsible for constructing the Living Legal Knowledge Graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from typing import Any
import networkx as nx


class LawGraphBuilder:
    """
    Builds and manages the in-memory legal knowledge graph.
    """

    def __init__(self):
        self.graph = nx.MultiDiGraph()

    def add_node(
        self,
        node_id: str,
        entity_type: str,
        **properties: Any
    ) -> None:
        """
        Add a legal entity to the graph.
        """

        self.graph.add_node(
            node_id,
            entity_type=entity_type,
            **properties
        )

    def add_edge(
        self,
        source: str,
        target: str,
        relationship: str,
        **properties: Any
    ) -> None:
        """
        Add a relationship between two legal entities.
        """

        self.graph.add_edge(
            source,
            target,
            relationship=relationship,
            **properties
        )

    def get_graph(self) -> nx.MultiDiGraph:
        """
        Return the complete graph.
        """

        return self.graph

    def number_of_nodes(self) -> int:
        return self.graph.number_of_nodes()

    def number_of_edges(self) -> int:
        return self.graph.number_of_edges()

    def clear(self) -> None:
        """
        Remove all nodes and edges.
        """

        self.graph.clear()