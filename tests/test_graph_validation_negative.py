"""
LawScape Negative Graph Validation Tests

Tests whether invalid graph operations are correctly rejected.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.graph.graph_builder import LawGraphBuilder


# ---------------------------------------------------------
# Setup
# ---------------------------------------------------------

builder = LawGraphBuilder()


# ---------------------------------------------------------
# Add Valid Nodes
# ---------------------------------------------------------

builder.add_node(
    node_id="ACT_001",
    entity_type="Act",
    title="Information Technology Act, 2000",
)

builder.add_node(
    node_id="SECTION_43A",
    entity_type="Section",
    title="Section 43A",
)


# ---------------------------------------------------------
# Test 1: Valid Edge
# ---------------------------------------------------------

builder.add_edge(
    source="ACT_001",
    target="SECTION_43A",
    relationship="contains",
)

assert builder.number_of_edges() == 1

print("Test 1 Passed: Valid edge accepted.")


# ---------------------------------------------------------
# Test 2: Invalid Relationship
# ---------------------------------------------------------

try:

    builder.add_edge(
        source="ACT_001",
        target="SECTION_43A",
        relationship="invalid_relationship",
    )

    raise AssertionError(
        "Invalid relationship was accepted."
    )

except ValueError:

    print(
        "Test 2 Passed: Invalid relationship rejected."
    )


# ---------------------------------------------------------
# Test 3: Missing Source Node
# ---------------------------------------------------------

try:

    builder.add_edge(
        source="UNKNOWN_NODE",
        target="SECTION_43A",
        relationship="contains",
    )

    raise AssertionError(
        "Missing source node was accepted."
    )

except ValueError:

    print(
        "Test 3 Passed: Missing source node rejected."
    )


# ---------------------------------------------------------
# Test 4: Missing Target Node
# ---------------------------------------------------------

try:

    builder.add_edge(
        source="ACT_001",
        target="UNKNOWN_NODE",
        relationship="contains",
    )

    raise AssertionError(
        "Missing target node was accepted."
    )

except ValueError:

    print(
        "Test 4 Passed: Missing target node rejected."
    )


# ---------------------------------------------------------
# Test 5: Duplicate Node
# ---------------------------------------------------------

try:

    builder.add_node(
        node_id="ACT_001",
        entity_type="Act",
        title="Duplicate Act",
    )

    raise AssertionError(
        "Duplicate node was accepted."
    )

except ValueError:

    print(
        "Test 5 Passed: Duplicate node rejected."
    )


# ---------------------------------------------------------
# Test 6: Duplicate Edge
# ---------------------------------------------------------

try:

    builder.add_edge(
        source="ACT_001",
        target="SECTION_43A",
        relationship="contains",
    )

    raise AssertionError(
        "Duplicate edge was accepted."
    )

except ValueError:

    print(
        "Test 6 Passed: Duplicate edge rejected."
    )


# ---------------------------------------------------------
# Test 7: Invalid Node - Missing Title
# ---------------------------------------------------------

try:

    builder.add_node(
        node_id="INVALID_NODE",
        entity_type="Act",
    )

    raise AssertionError(
        "Node without title was accepted."
    )

except ValueError:

    print(
        "Test 7 Passed: Invalid node without title rejected."
    )


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print(
    "\nNegative Graph Validation Tests Passed Successfully!"
)