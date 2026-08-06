"""
Graph Validator for LawScape

Validates nodes, relationships, and graph integrity before
they are inserted into the Legal Knowledge Graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from __future__ import annotations

from lawscape.graph.validation_rules import VALID_RELATIONSHIPS


class GraphValidator:
    """
    Validates nodes, edges, and graph integrity.
    """

    REQUIRED_NODE_PROPERTIES = [
        "node_id",
        "entity_type",
        "title",
    ]

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Node Validation
    # ---------------------------------------------------------

    def validate_node(self, node_data: dict) -> bool:
        """
        Validate node before insertion.
        """
        return self.validate_required_properties(node_data)

    # ---------------------------------------------------------
    # Edge Validation
    # ---------------------------------------------------------

    def validate_edge(
        self,
        graph,
        source,
        target,
        relationship,
    ) -> bool:
        """
        Validate an edge before insertion.
        """

        # Source node must exist
        if source not in graph.nodes:
            return False

        # Target node must exist
        if target not in graph.nodes:
            return False

        # Duplicate edge
        if self.validate_duplicate_edge(graph, source, target):
            return False

        # Read entity types from graph
        source_type = graph.nodes[source]["entity_type"]
        target_type = graph.nodes[target]["entity_type"]

        # Validate relationship
        return self.validate_relationship(
            source_type,
            target_type,
            relationship,
        )

    # ---------------------------------------------------------
    # Relationship Validation
    # ---------------------------------------------------------

    def validate_relationship(
        self,
        source_type,
        target_type,
        relationship,
    ) -> bool:
        """
        Validate legal relationship according to ontology.
        """

        if source_type not in VALID_RELATIONSHIPS:
            return False

        if relationship not in VALID_RELATIONSHIPS[source_type]:
            return False

        allowed_targets = VALID_RELATIONSHIPS[source_type][relationship]

        return target_type in allowed_targets

    # ---------------------------------------------------------
    # Required Properties
    # ---------------------------------------------------------

    def validate_required_properties(
        self,
        node_data: dict,
    ) -> bool:
        """
        Ensure all mandatory node properties exist.
        """

        for prop in self.REQUIRED_NODE_PROPERTIES:

            if prop not in node_data:
                return False

            if node_data[prop] is None:
                return False

            if node_data[prop] == "":
                return False

        return True

    # ---------------------------------------------------------
    # Duplicate Node
    # ---------------------------------------------------------

    def validate_duplicate_node(
        self,
        graph,
        node_id,
    ) -> bool:
        """
        Returns True if node already exists.
        """

        return node_id in graph.nodes

    # ---------------------------------------------------------
    # Duplicate Edge
    # ---------------------------------------------------------

    def validate_duplicate_edge(
        self,
        graph,
        source,
        target,
    ) -> bool:
        """
        Returns True if edge already exists.
        """

        return graph.has_edge(source, target)