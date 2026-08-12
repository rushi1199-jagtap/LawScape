"""
LawScape Constitution Integration Test

Tests the complete pipeline from Constitution text
to the Legal Knowledge Graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.data_ingestion.constitution_loader import ConstitutionLoader
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import ConstitutionGraphBuilder


# ---------------------------------------------------------
# Step 1: Load Constitution Data
# ---------------------------------------------------------

loader = ConstitutionLoader()

raw_data = loader.load(
    "datasets/constitution/constitution.txt"
)

print("===== RAW DATA LOADED =====")
print(f"Characters: {len(raw_data)}")


# ---------------------------------------------------------
# Step 2: Parse Constitution
# ---------------------------------------------------------

parsed_data = loader.parse(raw_data)

print("\n===== DATA PARSED =====")

print(
    f"Parts: {len(parsed_data['parts'])}"
)

print(
    f"Articles: {len(parsed_data['articles'])}"
)


# ---------------------------------------------------------
# Step 3: Validate Parsed Data
# ---------------------------------------------------------

is_valid = loader.validate(parsed_data)

print("\n===== DATA VALIDATION =====")
print(f"Valid: {is_valid}")

assert is_valid is True


# ---------------------------------------------------------
# Step 4: Create Graph Builder
# ---------------------------------------------------------

graph_builder = LawGraphBuilder()


# ---------------------------------------------------------
# Step 5: Build Constitution Graph
# ---------------------------------------------------------

constitution_builder = ConstitutionGraphBuilder(
    graph_builder
)

constitution_builder.build(
    parts=parsed_data["parts"],
    articles=parsed_data["articles"],
)


# ---------------------------------------------------------
# Step 6: Get Graph
# ---------------------------------------------------------

graph = graph_builder.get_graph()


# ---------------------------------------------------------
# Step 7: Graph Summary
# ---------------------------------------------------------

print("\n===== GRAPH SUMMARY =====")

print(
    f"Nodes: {graph.number_of_nodes()}"
)

print(
    f"Edges: {graph.number_of_edges()}"
)


# ---------------------------------------------------------
# Step 8: Validate Graph Structure
# ---------------------------------------------------------

assert "CONSTITUTION" in graph.nodes

assert "PART_I" in graph.nodes

assert "ARTICLE_1" in graph.nodes

assert "ARTICLE_2" in graph.nodes


# ---------------------------------------------------------
# Step 9: Validate Relationships
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


# ---------------------------------------------------------
# Step 10: Validate Relationship Types
# ---------------------------------------------------------

assert (
    graph["CONSTITUTION"]["PART_I"][0]["relationship"]
    == "contains"
)

assert (
    graph["PART_I"]["ARTICLE_1"][0]["relationship"]
    == "contains"
)

assert (
    graph["PART_I"]["ARTICLE_2"][0]["relationship"]
    == "contains"
)


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print("\nConstitution Integration Test Passed Successfully!")