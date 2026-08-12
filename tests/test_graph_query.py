"""
LawScape Graph Query Tests

Tests query and traversal operations over the
Constitution legal knowledge graph.

Author: Rushikesh Jagtap
Project: LawScape
"""

from lawscape.data_ingestion.constitution_loader import ConstitutionLoader
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import ConstitutionGraphBuilder
from lawscape.graph.graph_query import GraphQuery


# ---------------------------------------------------------
# Step 1: Load and Parse Constitution
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
# Step 3: Create Query Layer
# ---------------------------------------------------------

query = GraphQuery(graph)


# ---------------------------------------------------------
# Test 1: Get Constitution Parts
# ---------------------------------------------------------

parts = query.get_children(
    "CONSTITUTION",
    "contains",
)

assert parts == ["PART_I"]

print("Test 1 Passed: Constitution parts retrieved.")


# ---------------------------------------------------------
# Test 2: Get Articles of Part I
# ---------------------------------------------------------

articles = query.get_children(
    "PART_I",
    "contains",
)

assert set(articles) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 2 Passed: Part I articles retrieved.")


# ---------------------------------------------------------
# Test 3: Get Parent of Article 1
# ---------------------------------------------------------

parents = query.get_parents(
    "ARTICLE_1",
    "contains",
)

assert parents == ["PART_I"]

print("Test 3 Passed: Article parent retrieved.")


# ---------------------------------------------------------
# Test 4: Get Node Information
# ---------------------------------------------------------

article = query.get_node(
    "ARTICLE_1"
)

assert article["entity_type"] == "Article"
assert article["article_number"] == "1"
assert article["part_number"] == "I"

print("Test 4 Passed: Node information retrieved.")


# ---------------------------------------------------------
# Test 5: Check Relationship
# ---------------------------------------------------------

assert query.has_relationship(
    "CONSTITUTION",
    "PART_I",
    "contains",
)

assert query.has_relationship(
    "PART_I",
    "ARTICLE_1",
    "contains",
)

print("Test 5 Passed: Relationships verified.")


# ---------------------------------------------------------
# Test 6: Invalid Relationship Check
# ---------------------------------------------------------

assert not query.has_relationship(
    "CONSTITUTION",
    "ARTICLE_1",
    "contains",
)

print("Test 6 Passed: Invalid relationship correctly rejected.")


# ---------------------------------------------------------
# Test 7: Get Descendants
# ---------------------------------------------------------

descendants = query.get_descendants(
    "CONSTITUTION",
    "contains",
)

assert set(descendants) == {
    "PART_I",
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 7 Passed: Descendants retrieved.")


# ---------------------------------------------------------
# Test 8: Unknown Node
# ---------------------------------------------------------

assert query.get_children(
    "UNKNOWN_NODE"
) == []

assert query.get_parents(
    "UNKNOWN_NODE"
) == []

assert query.get_node(
    "UNKNOWN_NODE"
) == {}

assert query.get_descendants(
    "UNKNOWN_NODE"
) == []

print("Test 8 Passed: Unknown node handled safely.")

# ---------------------------------------------------------
# Test 9: Find Nodes by Entity Type
# ---------------------------------------------------------

articles_by_type = query.find_by_entity_type(
    "Article"
)

assert set(articles_by_type) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 9 Passed: Nodes found by entity type.")


# ---------------------------------------------------------
# Test 10: Find Nodes by Property
# ---------------------------------------------------------

part_articles = query.find_nodes_by_property(
    "part_number",
    "I",
)

print("Nodes with part_number='I':", part_articles)

assert "ARTICLE_1" in part_articles
assert "ARTICLE_2" in part_articles

print("Test 10 Passed: Nodes found by property.")


# ---------------------------------------------------------
# Test 11: Get Node Relationships
# ---------------------------------------------------------

article_relationships = query.get_relationships(
    "ARTICLE_1"
)

assert len(article_relationships) == 1

assert article_relationships[0]["source"] == "PART_I"
assert article_relationships[0]["target"] == "ARTICLE_1"
assert article_relationships[0]["relationship"] == "contains"
assert article_relationships[0]["direction"] == "incoming"

print("Test 11 Passed: Node relationships retrieved.")


# ---------------------------------------------------------
# Test 12: Unknown Property
# ---------------------------------------------------------

unknown_property = query.find_nodes_by_property(
    "unknown_property",
    "unknown_value",
)

assert unknown_property == []

print("Test 12 Passed: Unknown property handled safely.")


# ---------------------------------------------------------
# Test 13: Unknown Node Relationships
# ---------------------------------------------------------

assert query.get_relationships(
    "UNKNOWN_NODE"
) == []

print("Test 13 Passed: Unknown node relationships handled safely.")


# ---------------------------------------------------------
# Test 14: Get Constitution Parts
# ---------------------------------------------------------

parts = query.get_parts()

assert parts == ["PART_I"]

print("Test 14 Passed: Constitution parts retrieved through legal interface.")


# ---------------------------------------------------------
# Test 15: Get Articles of Part I
# ---------------------------------------------------------

part_articles = query.get_articles(
    "PART_I"
)

assert set(part_articles) == {
    "ARTICLE_1",
    "ARTICLE_2",
}

print("Test 15 Passed: Part articles retrieved through legal interface.")


# ---------------------------------------------------------
# Test 16: Get Parent of Article 1
# ---------------------------------------------------------

parent = query.get_parent(
    "ARTICLE_1"
)

assert parent == "PART_I"

print("Test 16 Passed: Article parent retrieved through legal interface.")


# ---------------------------------------------------------
# Test 17: Get Article by Number
# ---------------------------------------------------------

article_id = query.get_article(
    "1"
)

assert article_id == "ARTICLE_1"

print("Test 17 Passed: Article found by article number.")


# ---------------------------------------------------------
# Test 18: Unknown Article
# ---------------------------------------------------------

unknown_article = query.get_article(
    "999"
)

assert unknown_article is None

print("Test 18 Passed: Unknown article handled safely.")


# ---------------------------------------------------------
# Test 19: Unknown Parent
# ---------------------------------------------------------

unknown_parent = query.get_parent(
    "UNKNOWN_NODE"
)

assert unknown_parent is None

print("Test 19 Passed: Unknown parent handled safely.")


# ---------------------------------------------------------
# Test 20: Unknown Part
# ---------------------------------------------------------

unknown_part_articles = query.get_articles(
    "UNKNOWN_PART"
)

assert unknown_part_articles == []

print("Test 20 Passed: Unknown part handled safely.")


# ---------------------------------------------------------
# Final Result
# ---------------------------------------------------------

print(
    "\nLegal Graph Query Interface Tests Passed Successfully!"
)

