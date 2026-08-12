from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import ConstitutionGraphBuilder
from lawscape.data_ingestion.data_models import LegalPart, LegalArticle


# ---------------------------------------------------------
# Test Data
# ---------------------------------------------------------

parts = [
    LegalPart(
        part_number="I",
        title="Part I",
    )
]

articles = [
    LegalArticle(
        article_number="1",
        content="India, that is Bharat, shall be a Union of States.",
        part_number="I",
    ),
    LegalArticle(
        article_number="2",
        content="Parliament may by law admit into the Union...",
        part_number="I",
    ),
]


# ---------------------------------------------------------
# Build Graph
# ---------------------------------------------------------

graph_builder = LawGraphBuilder()

constitution_builder = ConstitutionGraphBuilder(
    graph_builder
)

constitution_builder.build(
    parts=parts,
    articles=articles,
)

graph = graph_builder.get_graph()


# ---------------------------------------------------------
# Graph Summary
# ---------------------------------------------------------

print("===== GRAPH SUMMARY =====")
print(f"Nodes: {graph.number_of_nodes()}")
print(f"Edges: {graph.number_of_edges()}")


print("\n===== NODES =====")

for node, data in graph.nodes(data=True):
    print(node, data)


print("\n===== EDGES =====")

for source, target, data in graph.edges(data=True):
    print(source, target, data)


# ---------------------------------------------------------
# Assertions
# ---------------------------------------------------------

assert graph.number_of_nodes() == 4
assert graph.number_of_edges() == 3

# Constitution node
assert "CONSTITUTION" in graph.nodes

assert graph.nodes["CONSTITUTION"]["entity_type"] == "Constitution"
assert graph.nodes["CONSTITUTION"]["title"] == "Constitution of India"

# Part node
assert "PART_I" in graph.nodes

assert graph.nodes["PART_I"]["entity_type"] == "Part"
assert graph.nodes["PART_I"]["part_number"] == "I"

# Article nodes
assert "ARTICLE_1" in graph.nodes
assert "ARTICLE_2" in graph.nodes

assert graph.nodes["ARTICLE_1"]["entity_type"] == "Article"
assert graph.nodes["ARTICLE_2"]["entity_type"] == "Article"

# Constitution -> Part
assert graph.has_edge(
    "CONSTITUTION",
    "PART_I",
)

assert graph["CONSTITUTION"]["PART_I"][0]["relationship"] == "contains"

# Part -> Article
assert graph.has_edge(
    "PART_I",
    "ARTICLE_1",
)

assert graph.has_edge(
    "PART_I",
    "ARTICLE_2",
)

assert graph["PART_I"]["ARTICLE_1"][0]["relationship"] == "contains"
assert graph["PART_I"]["ARTICLE_2"][0]["relationship"] == "contains"


print("\nConstitution Graph Builder Test Passed Successfully!")