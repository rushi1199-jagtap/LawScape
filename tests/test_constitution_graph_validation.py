"""
LawScape Constitution Graph Validation Integration Test

Tests Constitution graph construction together with
GraphValidator.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.data_ingestion.constitution_loader import ConstitutionLoader
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import ConstitutionGraphBuilder


# ---------------------------------------------------------
# Step 1: Load Constitution
# ---------------------------------------------------------

loader = ConstitutionLoader()

raw_data = loader.load(
    "datasets/constitution/constitution.txt"
)

parsed_data = loader.parse(raw_data)

assert loader.validate(parsed_data) is True

print("Test 1 Passed: Constitution data loaded and validated.")


# ---------------------------------------------------------
# Step 2: Build Constitution Graph
# ---------------------------------------------------------

graph_builder = LawGraphBuilder()

constitution_builder = ConstitutionGraphBuilder(
    graph_builder
)

constitution_builder.build(
    parts=parsed_data["parts"],
    articles=parsed_data["articles"],
)

graph = graph_builder.get_graph()

print("Test 2 Passed: Constitution graph built successfully.")


# ---------------------------------------------------------
# Step 3: Validate Graph Structure
# ---------------------------------------------------------

assert "CONSTITUTION" in graph.nodes
assert "PART_I" in graph.nodes
assert "ARTICLE_1" in graph.nodes
assert "ARTICLE_2" in graph.nodes

assert graph.number_of_nodes() == 4
assert graph.number_of_edges() == 3

print("Test 3 Passed: Graph structure is valid.")


# ---------------------------------------------------------
# Step 4: Validate Existing Relationships
# ---------------------------------------------------------

assert graph.has_edge(
    "CONSTITUTION",
    "PART_I",
)

assert graph.has_edge(
    "PART_I",
    "ARTICLE_1",
)

assert graph.has_edge(
    "PART_I",
    "ARTICLE_2",
)

print("Test 4 Passed: Valid relationships confirmed.")


# ---------------------------------------------------------
# Step 5: Invalid Relationship
# ---------------------------------------------------------

try:

    graph_builder.add_edge(
        source="CONSTITUTION",
        target="ARTICLE_1",
        relationship="invalid_relationship",
    )

    raise AssertionError(
        "Invalid relationship was accepted."
    )

except ValueError:

    print(
        "Test 5 Passed: Invalid relationship rejected."
    )


# ---------------------------------------------------------
# Step 6: Missing Node
# ---------------------------------------------------------

try:

    graph_builder.add_edge(
        source="UNKNOWN_NODE",
        target="PART_I",
        relationship="contains",
    )

    raise AssertionError(
        "Missing node was accepted."
    )

except ValueError:

    print(
        "Test 6 Passed: Missing node rejected."
    )


# ---------------------------------------------------------
# Step 7: Duplicate Node
# ---------------------------------------------------------

try:

    graph_builder.add_node(
        node_id="PART_I",
        entity_type="Part",
        title="Duplicate Part",
        part_number="I",
    )

    raise AssertionError(
        "Duplicate node was accepted."
    )

except ValueError:

    print(
        "Test 7 Passed: Duplicate node rejected."
    )


# ---------------------------------------------------------
# Step 8: Duplicate Edge
# ---------------------------------------------------------

try:

    graph_builder.add_edge(
        source="CONSTITUTION",
        target="PART_I",
        relationship="contains",
    )

    raise AssertionError(
        "Duplicate edge was accepted."
    )

except ValueError:

    print(
        "Test 8 Passed: Duplicate edge rejected."
    )


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print(
    "\nConstitution Graph Validation Integration Test "
    "Passed Successfully!"
)