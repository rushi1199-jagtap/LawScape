"""
LawScape Constitution Graph Service Tests

Tests the complete Constitution ingestion-to-service pipeline.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.services.constitution_graph_service import (
    ConstitutionGraphService,
)


# ---------------------------------------------------------
# Step 1: Create Constitution Graph Service
# ---------------------------------------------------------

service_builder = ConstitutionGraphService(
    "datasets/constitution/constitution.txt"
)


# ---------------------------------------------------------
# Step 2: Build Complete Pipeline
# ---------------------------------------------------------

service = service_builder.build()


# ---------------------------------------------------------
# Test 1: Graph Statistics
# ---------------------------------------------------------

stats = service.get_graph_stats()

assert stats["nodes"] == 4
assert stats["edges"] == 3

print("Test 1 Passed: Constitution graph built successfully.")


# ---------------------------------------------------------
# Test 2: Search Article
# ---------------------------------------------------------

results = service.search_entities(
    "Article 1"
)

assert "ARTICLE_1" in results

print("Test 2 Passed: Article search works end-to-end.")


# ---------------------------------------------------------
# Test 3: Get Article
# ---------------------------------------------------------

article = service.get_entity(
    "ARTICLE_1"
)

assert article["entity_type"] == "Article"
assert article["article_number"] == "1"
assert article["part_number"] == "I"

print("Test 3 Passed: Article retrieval works end-to-end.")


# ---------------------------------------------------------
# Test 4: Get Parent
# ---------------------------------------------------------

parent = service.get_parent(
    "ARTICLE_1"
)

assert parent == "PART_I"

print("Test 4 Passed: Article parent retrieved end-to-end.")


# ---------------------------------------------------------
# Test 5: Get Part Children
# ---------------------------------------------------------

children = service.get_children(
    "PART_I"
)

assert set(children) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 5 Passed: Part articles retrieved end-to-end.")


# ---------------------------------------------------------
# Test 6: Get Relationships
# ---------------------------------------------------------

relationships = service.get_relationships(
    "ARTICLE_1"
)

assert len(relationships) == 1

assert relationships[0]["source"] == "PART_I"
assert relationships[0]["target"] == "ARTICLE_1"
assert relationships[0]["relationship"] == "contains"

print("Test 6 Passed: Legal relationship retrieved end-to-end.")


# ---------------------------------------------------------
# Test 7: Search and Get
# ---------------------------------------------------------

results = service.search_and_get(
    "Union of States"
)

assert len(results) == 1

assert results[0]["node_id"] == "ARTICLE_1"

print("Test 7 Passed: Search and retrieval pipeline works.")

# ---------------------------------------------------------
# Test 8: Direct Graph Access
# ---------------------------------------------------------

graph = service_builder.get_graph()

assert graph.number_of_nodes() == 4
assert graph.number_of_edges() == 3

print("Test 8 Passed: Constructed graph accessible.")


# ---------------------------------------------------------
# Test 9: Same Service Instance
# ---------------------------------------------------------

assert service_builder.get_service() is service

print("Test 9 Passed: Service instance correctly retained.")


# ---------------------------------------------------------
# Test 10: Invalid Constitution Source
# ---------------------------------------------------------

invalid_builder = ConstitutionGraphService(
    "datasets/constitution/does_not_exist.txt"
)

try:
    invalid_builder.build()
    assert False, "Expected FileNotFoundError"
except FileNotFoundError:
    pass

print("Test 10 Passed: Invalid Constitution source rejected.")


# ---------------------------------------------------------
# Test 11: Service Access Before Build
# ---------------------------------------------------------

unbuilt_service = ConstitutionGraphService(
    "datasets/constitution/constitution.txt"
)

try:
    unbuilt_service.get_service()
    assert False, "Expected RuntimeError"
except RuntimeError:
    pass

print("Test 11 Passed: Service access before build rejected.")


# ---------------------------------------------------------
# Test 12: Graph Access Before Build
# ---------------------------------------------------------

empty_graph = unbuilt_service.get_graph()

assert empty_graph.number_of_nodes() == 0
assert empty_graph.number_of_edges() == 0

print("Test 12 Passed: Empty graph state handled safely.")


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print(
    "\nConstitution Graph Service Negative Tests "
    "Passed Successfully!"
)