"""
LawScape Legal Lookup Tests

Tests the high-level integration between graph search
and graph query operations.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.data_ingestion.constitution_loader import ConstitutionLoader
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import ConstitutionGraphBuilder
from lawscape.graph.legal_lookup import LegalLookup


# ---------------------------------------------------------
# Step 1: Load Constitution
# ---------------------------------------------------------

loader = ConstitutionLoader()

raw_data = loader.load(
    "datasets/constitution/constitution.txt"
)

parsed_data = loader.parse(raw_data)

assert loader.validate(parsed_data) is True


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


# ---------------------------------------------------------
# Step 3: Create Legal Lookup
# ---------------------------------------------------------

lookup = LegalLookup(graph)


# ---------------------------------------------------------
# Test 1: Search Entity
# ---------------------------------------------------------

results = lookup.search_entity(
    "Article 1"
)

assert "ARTICLE_1" in results

print("Test 1 Passed: Legal entity search.")


# ---------------------------------------------------------
# Test 2: Get Entity
# ---------------------------------------------------------

article = lookup.get_entity(
    "ARTICLE_1"
)

assert article["entity_type"] == "Article"
assert article["title"] == "Article 1"
assert article["article_number"] == "1"

print("Test 2 Passed: Legal entity retrieval.")


# ---------------------------------------------------------
# Test 3: Get Parent
# ---------------------------------------------------------

parent = lookup.get_parent(
    "ARTICLE_1"
)

assert parent == "PART_I"

print("Test 3 Passed: Legal parent retrieval.")


# ---------------------------------------------------------
# Test 4: Get Children
# ---------------------------------------------------------

children = lookup.get_children(
    "PART_I"
)

assert set(children) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 4 Passed: Legal children retrieval.")


# ---------------------------------------------------------
# Test 5: Get Relationships
# ---------------------------------------------------------

relationships = lookup.get_relationships(
    "ARTICLE_1"
)

assert len(relationships) == 1

assert relationships[0]["source"] == "PART_I"
assert relationships[0]["target"] == "ARTICLE_1"
assert relationships[0]["relationship"] == "contains"

print("Test 5 Passed: Legal relationships retrieval.")


# ---------------------------------------------------------
# Test 6: Search and Get
# ---------------------------------------------------------

search_results = lookup.search_and_get(
    "Article 1"
)

assert len(search_results) == 1

assert search_results[0]["node_id"] == "ARTICLE_1"

assert (
    search_results[0]["data"]["article_number"]
    == "1"
)

print("Test 6 Passed: Search and entity retrieval integration.")


# ---------------------------------------------------------
# Test 7: Unknown Entity
# ---------------------------------------------------------

assert lookup.get_entity(
    "UNKNOWN_NODE"
) == {}

assert lookup.get_parent(
    "UNKNOWN_NODE"
) is None

assert lookup.get_children(
    "UNKNOWN_NODE"
) == []

assert lookup.get_relationships(
    "UNKNOWN_NODE"
) == []

print("Test 7 Passed: Unknown entity handled safely.")


# ---------------------------------------------------------
# Test 8: Empty Search
# ---------------------------------------------------------

assert lookup.search_entity("") == []

print("Test 8 Passed: Empty search handled safely.")


# ---------------------------------------------------------
# Test 9: Search with No Result
# ---------------------------------------------------------

assert lookup.search_entity(
    "xyz_not_found"
) == []

print("Test 9 Passed: No-result search handled safely.")


# ---------------------------------------------------------
# Test 10: Empty Search and Get
# ---------------------------------------------------------

assert lookup.search_and_get("") == []

print("Test 10 Passed: Empty search-and-get handled safely.")


# ---------------------------------------------------------
# Test 11: Search and Get with No Result
# ---------------------------------------------------------

assert lookup.search_and_get(
    "xyz_not_found"
) == []

print("Test 11 Passed: Search-and-get with no result handled safely.")


# ---------------------------------------------------------
# Test 12: Unknown Entity Relationships
# ---------------------------------------------------------

assert lookup.get_relationships(
    "NOT_A_REAL_NODE"
) == []

print("Test 12 Passed: Unknown entity relationships handled safely.")


# ---------------------------------------------------------
# Test 13: Unknown Entity Children
# ---------------------------------------------------------

assert lookup.get_children(
    "NOT_A_REAL_NODE"
) == []

print("Test 13 Passed: Unknown entity children handled safely.")


# ---------------------------------------------------------
# Test 14: Unknown Entity Parent
# ---------------------------------------------------------

assert lookup.get_parent(
    "NOT_A_REAL_NODE"
) is None

print("Test 14 Passed: Unknown entity parent handled safely.")


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print(
    "\nLegal Lookup Negative Tests Passed Successfully!"
)