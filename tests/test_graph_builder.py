"""
Tests for LawScape Graph Builder

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.graph.graph_builder import LawGraphBuilder


def test_graph_builder():
    """
    Test basic graph construction.
    """

    builder = LawGraphBuilder()

    # Add an Act node
    builder.add_node(
        node_id="ACT_001",
        entity_type="ACT",
        title="Information Technology Act, 2000"
    )

    # Add a Section node
    builder.add_node(
        node_id="SEC_43A",
        entity_type="SECTION",
        title="Section 43A"
    )

    # Connect the nodes
    builder.add_edge(
        source="ACT_001",
        target="SEC_43A",
        relationship="contains"
    )

    # Verify graph statistics
    assert builder.number_of_nodes() == 2
    assert builder.number_of_edges() == 1

    graph = builder.get_graph()

    print("\n===== GRAPH SUMMARY =====")
    print(f"Nodes: {builder.number_of_nodes()}")
    print(f"Edges: {builder.number_of_edges()}")

    print("\n===== NODES =====")
    for node in graph.nodes(data=True):
        print(node)

    print("\n===== EDGES =====")
    for edge in graph.edges(data=True):
        print(edge)

    print("\n✅ Graph Builder Test Passed Successfully!")


if __name__ == "__main__":
    test_graph_builder()