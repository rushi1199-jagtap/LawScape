"""
LawScape Graph Query

Provides read-only query and traversal operations
over the LawScape legal knowledge graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from typing import List

import networkx as nx


class GraphQuery:
    """
    Provides query and traversal operations for
    the LawScape legal knowledge graph.
    """

    def __init__(self, graph: nx.MultiDiGraph):
        self.graph = graph

    # ---------------------------------------------------------
    # Direct Children
    # ---------------------------------------------------------

    def get_children(
        self,
        node_id: str,
        relationship: str = "contains",
    ) -> List[str]:
        """
        Return nodes directly connected from the given node
        using the specified relationship.
        """

        if node_id not in self.graph:
            return []

        children = []

        for _, target, data in self.graph.out_edges(
            node_id,
            data=True,
        ):
            if data.get("relationship") == relationship:
                children.append(target)

        return children

    # ---------------------------------------------------------
    # Direct Parents
    # ---------------------------------------------------------

    def get_parents(
        self,
        node_id: str,
        relationship: str = "contains",
    ) -> List[str]:
        """
        Return nodes directly connected to the given node
        using the specified relationship.
        """

        if node_id not in self.graph:
            return []

        parents = []

        for source, _, data in self.graph.in_edges(
            node_id,
            data=True,
        ):
            if data.get("relationship") == relationship:
                parents.append(source)

        return parents

    # ---------------------------------------------------------
    # Node Information
    # ---------------------------------------------------------

    def get_node(
        self,
        node_id: str,
    ) -> dict:
        """
        Return node properties.
        """

        if node_id not in self.graph:
            return {}

        return dict(self.graph.nodes[node_id])

    # ---------------------------------------------------------
    # Relationship Check
    # ---------------------------------------------------------

    def has_relationship(
        self,
        source: str,
        target: str,
        relationship: str,
    ) -> bool:
        """
        Check whether a specific relationship exists
        between two nodes.
        """

        if not self.graph.has_edge(source, target):
            return False

        edge_data = self.graph.get_edge_data(
            source,
            target,
        )

        if edge_data is None:
            return False

        for data in edge_data.values():
            if data.get("relationship") == relationship:
                return True

        return False

    # ---------------------------------------------------------
    # Descendants
    # ---------------------------------------------------------

    def get_descendants(
        self,
        node_id: str,
        relationship: str = "contains",
    ) -> List[str]:
        """
        Return all reachable descendant nodes using
        the specified relationship.
        """

        if node_id not in self.graph:
            return []

        descendants = []

        queue = list(
            self.get_children(
                node_id,
                relationship,
            )
        )

        visited = set()

        while queue:

            current = queue.pop(0)

            if current in visited:
                continue

            visited.add(current)
            descendants.append(current)

            children = self.get_children(
                current,
                relationship,
            )

            queue.extend(children)

        return descendants

    # ---------------------------------------------------------
    # Find Nodes by Entity Type
    # ---------------------------------------------------------

    def find_by_entity_type(
        self,
        entity_type: str,
    ) -> List[str]:
        """
        Return all node IDs matching the given entity type.
        """

        return [
            node_id
            for node_id, data in self.graph.nodes(data=True)
            if data.get("entity_type") == entity_type
        ]

    # ---------------------------------------------------------
    # Get All Relationships
    # ---------------------------------------------------------

    def get_relationships(
        self,
        node_id: str,
    ) -> List[dict]:
        """
        Return all incoming and outgoing relationships
        associated with a node.
        """

        if node_id not in self.graph:
            return []

        relationships = []

        for source, target, data in self.graph.in_edges(
            node_id,
            data=True,
        ):
            relationships.append(
                {
                    "source": source,
                    "target": target,
                    "relationship": data.get("relationship"),
                    "direction": "incoming",
                }
            )

        for source, target, data in self.graph.out_edges(
            node_id,
            data=True,
        ):
            relationships.append(
                {
                    "source": source,
                    "target": target,
                    "relationship": data.get("relationship"),
                    "direction": "outgoing",
                }
            )

        return relationships

    # ---------------------------------------------------------
    # Find Nodes by Property
    # ---------------------------------------------------------

    def find_nodes_by_property(
        self,
        property_name: str,
        property_value,
    ) -> List[str]:
        """
        Return all node IDs where the given property
        matches the specified value.
        """

        return [
            node_id
            for node_id, data in self.graph.nodes(data=True)
            if data.get(property_name) == property_value
        ]
    
        # ---------------------------------------------------------
    # Get Constitution Parts
    # ---------------------------------------------------------

    def get_parts(self) -> List[str]:
        """
        Return all Parts directly contained by the Constitution.
        """

        return self.get_children(
            "CONSTITUTION",
            "contains",
        )

    # ---------------------------------------------------------
    # Get Articles of a Part
    # ---------------------------------------------------------

    def get_articles(
        self,
        part_id: str,
    ) -> List[str]:
        """
        Return all Articles directly contained by a Part.
        """

        return self.get_children(
            part_id,
            "contains",
        )

    # ---------------------------------------------------------
    # Get Parent Node
    # ---------------------------------------------------------

    def get_parent(
        self,
        node_id: str,
    ) -> str | None:
        """
        Return the direct parent of a node.

        Returns None if the node does not exist or
        has no parent.
        """

        parents = self.get_parents(
            node_id,
            "contains",
        )

        if not parents:
            return None

        return parents[0]

    # ---------------------------------------------------------
    # Get Article by Number
    # ---------------------------------------------------------

    def get_article(
        self,
        article_number: str,
    ) -> str | None:
        """
        Find an Article node using its article number.

        Returns the node ID if found, otherwise None.
        """

        articles = self.find_nodes_by_property(
            "article_number",
            article_number,
        )

        for article_id in articles:

            node = self.get_node(article_id)

            if node.get("entity_type") == "Article":
                return article_id

        return None    