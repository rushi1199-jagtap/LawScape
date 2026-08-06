"""
LawScape Graph Builder

Responsible for constructing the Living Legal Knowledge Graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from typing import Any
import networkx as nx

from lawscape.graph.graph_validator import GraphValidator


class LawGraphBuilder:
    """
    Builds and manages the in-memory legal knowledge graph.
    """

    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.validator = GraphValidator()

    # ---------------------------------------------------------
    # Node Operations
    # ---------------------------------------------------------

    def add_node(
        self,
        node_id: str,
        entity_type: str,
        **properties: Any
    ) -> None:
        """
        Add a legal entity after validation.
        """

        node_data = {
            "node_id": node_id,
            "entity_type": entity_type,
            **properties,
        }

        if not self.validator.validate_node(node_data):
            raise ValueError(f"Invalid node: {node_id}")

        if self.validator.validate_duplicate_node(self.graph, node_id):
            raise ValueError(f"Duplicate node: {node_id}")

        self.graph.add_node(
            node_id,
            entity_type=entity_type,
            **properties
        )

    # ---------------------------------------------------------
    # Edge Operations
    # ---------------------------------------------------------

    def add_edge(
        self,
        source: str,
        target: str,
        relationship: str,
        **properties: Any
    ) -> None:
        """
        Add a legal relationship after validation.
        """

        if not self.validator.validate_edge(
            self.graph,
            source,
            target,
            relationship,
        ):
            raise ValueError(
                f"Invalid relationship: {source} -> {target}"
            )

        self.graph.add_edge(
            source,
            target,
            relationship=relationship,
            **properties
        )

    # ---------------------------------------------------------
    # Utility Methods
    # ---------------------------------------------------------

    def get_graph(self) -> nx.MultiDiGraph:
        return self.graph

    def number_of_nodes(self) -> int:
        return self.graph.number_of_nodes()

    def number_of_edges(self) -> int:
        return self.graph.number_of_edges()

    def clear(self) -> None:
        self.graph.clear()