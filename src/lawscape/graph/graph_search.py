"""
LawScape Graph Search

Provides search and lookup operations over the
LawScape legal knowledge graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from typing import Any, List

import networkx as nx


class GraphSearch:
    """
    Provides search and lookup operations for
    legal entities stored in the graph.
    """

    def __init__(self, graph: nx.MultiDiGraph):
        self.graph = graph

    # ---------------------------------------------------------
    # Search by Exact Property
    # ---------------------------------------------------------

    def search_by_property(
        self,
        property_name: str,
        property_value: Any,
    ) -> List[str]:
        """
        Return node IDs whose property exactly matches
        the supplied value.
        """

        results = []

        for node_id, data in self.graph.nodes(data=True):

            if data.get(property_name) == property_value:
                results.append(node_id)

        return results

    # ---------------------------------------------------------
    # Search by Entity Type
    # ---------------------------------------------------------

    def search_by_entity_type(
        self,
        entity_type: str,
    ) -> List[str]:
        """
        Return all nodes matching the specified entity type.
        """

        return self.search_by_property(
            "entity_type",
            entity_type,
        )

    # ---------------------------------------------------------
    # Search by Title
    # ---------------------------------------------------------

    def search_by_title(
        self,
        title: str,
    ) -> List[str]:
        """
        Return nodes whose title exactly matches
        the supplied title.
        """

        return self.search_by_property(
            "title",
            title,
        )

    # ---------------------------------------------------------
    # Search Title Contains
    # ---------------------------------------------------------

    def search_title_contains(
        self,
        text: str,
    ) -> List[str]:
        """
        Return nodes whose title contains the supplied
        text, case-insensitively.
        """

        if not text:
            return []

        text = text.lower()

        results = []

        for node_id, data in self.graph.nodes(data=True):

            title = data.get("title")

            if not isinstance(title, str):
                continue

            if text in title.lower():
                results.append(node_id)

        return results

    # ---------------------------------------------------------
    # Get Node
    # ---------------------------------------------------------

    def get_node(
        self,
        node_id: str,
    ) -> dict:
        """
        Return node data for a given node ID.
        """

        if node_id not in self.graph:
            return {}

        return dict(
            self.graph.nodes[node_id]
        )

    # ---------------------------------------------------------
    # Search All
    # ---------------------------------------------------------

    def search(
        self,
        text: str,
    ) -> List[str]:
        """
        Perform a simple text search across node IDs
        and string-valued node properties.

        Search is case-insensitive.
        """

        if not text:
            return []

        text = text.lower()

        results = []

        for node_id, data in self.graph.nodes(data=True):

            if text in node_id.lower():
                results.append(node_id)
                continue

            for value in data.values():

                if isinstance(value, str):
                    if text in value.lower():
                        results.append(node_id)
                        break

        return results