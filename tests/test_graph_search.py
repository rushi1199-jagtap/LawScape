"""
LawScape Graph Search Tests

Tests search and lookup operations over the
Constitution legal knowledge graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.data_ingestion.constitution_loader import ConstitutionLoader
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import ConstitutionGraphBuilder
from lawscape.graph.graph_search import GraphSearch


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
# Step 2: Build Graph
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
# Step 3: Create Search Layer
# ---------------------------------------------------------

search = GraphSearch(graph)


# ---------------------------------------------------------
# Test 1: Search by Entity Type
# ---------------------------------------------------------

articles = search.search_by_entity_type(
    "Article"
)

assert set(articles) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 1 Passed: Search by entity type.")


# ---------------------------------------------------------
# Test 2: Search by Exact Title
# ---------------------------------------------------------

part = search.search_by_title(
    "Part I"
)

assert part == ["PART_I"]

print("Test 2 Passed: Search by exact title.")


# ---------------------------------------------------------
# Test 3: Search Title Contains
# ---------------------------------------------------------

article_titles = search.search_title_contains(
    "article"
)

assert set(article_titles) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 3 Passed: Partial title search.")


# ---------------------------------------------------------
# Test 4: Search by Exact Property
# ---------------------------------------------------------

article_one = search.search_by_property(
    "article_number",
    "1",
)

assert article_one == ["ARTICLE_1"]

print("Test 4 Passed: Search by exact property.")


# ---------------------------------------------------------
# Test 5: Get Node
# ---------------------------------------------------------

node = search.get_node(
    "ARTICLE_1"
)

assert node["entity_type"] == "Article"
assert node["title"] == "Article 1"
assert node["article_number"] == "1"

print("Test 5 Passed: Node lookup.")


# ---------------------------------------------------------
# Test 6: General Text Search
# ---------------------------------------------------------

results = search.search(
    "India"
)

assert "ARTICLE_1" in results

print("Test 6 Passed: General text search.")


# ---------------------------------------------------------
# Test 7: Case-Insensitive Search
# ---------------------------------------------------------

results = search.search(
    "constitution"
)

assert "CONSTITUTION" in results

print("Test 7 Passed: Case-insensitive search.")


# ---------------------------------------------------------
# Test 8: Unknown Search
# ---------------------------------------------------------

results = search.search(
    "xyz_not_found"
)

assert results == []

print("Test 8 Passed: Unknown search handled safely.")


# ---------------------------------------------------------
# Test 9: Empty Search
# ---------------------------------------------------------

assert search.search("") == []

assert search.search_title_contains("") == []

print("Test 9 Passed: Empty search handled safely.")


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print(
    "\nGraph Search Tests Passed Successfully!"
)