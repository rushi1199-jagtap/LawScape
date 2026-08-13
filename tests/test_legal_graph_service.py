"""
LawScape Legal Graph Service Tests

Tests the high-level service interface for the
LawScape legal knowledge graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.data_ingestion.constitution_loader import ConstitutionLoader
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import ConstitutionGraphBuilder
from lawscape.services.legal_graph_service import LegalGraphService


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
# Step 3: Create Service
# ---------------------------------------------------------

service = LegalGraphService(graph)


# ---------------------------------------------------------
# Test 1: Search Entities
# ---------------------------------------------------------

results = service.search_entities(
    "Article 1"
)

assert "ARTICLE_1" in results

print("Test 1 Passed: Entity search through service.")


# ---------------------------------------------------------
# Test 2: Get Entity
# ---------------------------------------------------------

article = service.get_entity(
    "ARTICLE_1"
)

assert article["entity_type"] == "Article"
assert article["article_number"] == "1"

print("Test 2 Passed: Entity retrieval through service.")


# ---------------------------------------------------------
# Test 3: Get Parent
# ---------------------------------------------------------

parent = service.get_parent(
    "ARTICLE_1"
)

assert parent == "PART_I"

print("Test 3 Passed: Parent retrieval through service.")


# ---------------------------------------------------------
# Test 4: Get Children
# ---------------------------------------------------------

children = service.get_children(
    "PART_I"
)

assert set(children) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 4 Passed: Children retrieval through service.")


# ---------------------------------------------------------
# Test 5: Get Relationships
# ---------------------------------------------------------

relationships = service.get_relationships(
    "ARTICLE_1"
)

assert len(relationships) == 1

assert relationships[0]["source"] == "PART_I"
assert relationships[0]["target"] == "ARTICLE_1"
assert relationships[0]["relationship"] == "contains"

print("Test 5 Passed: Relationship retrieval through service.")


# ---------------------------------------------------------
# Test 6: Search and Get
# ---------------------------------------------------------

results = service.search_and_get(
    "Article 1"
)

assert len(results) == 1
assert results[0]["node_id"] == "ARTICLE_1"

print("Test 6 Passed: Search and get through service.")


# ---------------------------------------------------------
# Test 7: Graph Statistics
# ---------------------------------------------------------

stats = service.get_graph_stats()

assert stats["nodes"] == 4
assert stats["edges"] == 3

print("Test 7 Passed: Graph statistics retrieved.")


# ---------------------------------------------------------
# Test 8: Unknown Entity
# ---------------------------------------------------------

assert service.get_entity(
    "UNKNOWN_NODE"
) == {}

assert service.get_parent(
    "UNKNOWN_NODE"
) is None

assert service.get_children(
    "UNKNOWN_NODE"
) == []

assert service.get_relationships(
    "UNKNOWN_NODE"
) == []

print("Test 8 Passed: Unknown entity handled safely.")


# ---------------------------------------------------------
# Test 9: Empty Search
# ---------------------------------------------------------

assert service.search_entities("") == []

print("Test 9 Passed: Empty search handled safely.")


# ---------------------------------------------------------
# Test 10: Search with No Result
# ---------------------------------------------------------

assert service.search_entities(
    "xyz_not_found"
) == []

print("Test 10 Passed: No-result search handled safely.")


# ---------------------------------------------------------
# Test 11: Empty Search and Get
# ---------------------------------------------------------

assert service.search_and_get("") == []

print("Test 11 Passed: Empty search-and-get handled safely.")


# ---------------------------------------------------------
# Test 12: Search and Get with No Result
# ---------------------------------------------------------

assert service.search_and_get(
    "xyz_not_found"
) == []

print("Test 12 Passed: Search-and-get with no result handled safely.")


# ---------------------------------------------------------
# Test 13: Unknown Entity
# ---------------------------------------------------------

assert service.get_entity(
    "NOT_A_REAL_NODE"
) == {}

print("Test 13 Passed: Unknown entity retrieval handled safely.")


# ---------------------------------------------------------
# Test 14: Unknown Parent
# ---------------------------------------------------------

assert service.get_parent(
    "NOT_A_REAL_NODE"
) is None

print("Test 14 Passed: Unknown parent handled safely.")


# ---------------------------------------------------------
# Test 15: Unknown Children
# ---------------------------------------------------------

assert service.get_children(
    "NOT_A_REAL_NODE"
) == []

print("Test 15 Passed: Unknown children handled safely.")


# ---------------------------------------------------------
# Test 16: Unknown Relationships
# ---------------------------------------------------------

assert service.get_relationships(
    "NOT_A_REAL_NODE"
) == []

print("Test 16 Passed: Unknown relationships handled safely.")


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print(
    "\nLegal Graph Service Negative Tests Passed Successfully!"
)