from lawscape.data_ingestion.constitution_loader import (
    ConstitutionLoader,
)
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.graph.constitution_graph_builder import (
    ConstitutionGraphBuilder,
)


loader = ConstitutionLoader()

raw_data = loader.load(
    "datasets/constitution/constitution.txt"
)

parsed_data = loader.parse(raw_data)

graph_builder = LawGraphBuilder()

constitution_builder = ConstitutionGraphBuilder(
    graph_builder
)

constitution_builder.build(
    parts=parsed_data["parts"],
    articles=parsed_data["articles"],
)

graph = graph_builder.get_graph()

print("===== GRAPH SUMMARY =====")
print("Nodes:", graph.number_of_nodes())
print("Edges:", graph.number_of_edges())

print("\n===== NODES =====")

for node_id, data in graph.nodes(data=True):
    print(node_id, data)

print("\n===== EDGES =====")

for source, target, data in graph.edges(data=True):
    print(source, target, data)


assert graph.number_of_nodes() == 3
assert graph.number_of_edges() == 2

assert "PART_I" in graph.nodes
assert "ARTICLE_1" in graph.nodes
assert "ARTICLE_2" in graph.nodes

assert graph.has_edge("PART_I", "ARTICLE_1")
assert graph.has_edge("PART_I", "ARTICLE_2")

print("\nConstitution Graph Builder Test Passed Successfully!")