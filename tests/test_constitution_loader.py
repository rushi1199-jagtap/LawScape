from lawscape.data_ingestion.constitution_loader import ConstitutionLoader
from lawscape.data_ingestion.data_models import (
    LegalArticle,
    LegalPart,
)


loader = ConstitutionLoader()

data = loader.load(
    "datasets/constitution/constitution.txt"
)

parsed = loader.parse(data)

print("===== PARTS =====")
print(parsed["parts"])

print("\n===== ARTICLES =====")
print(parsed["articles"])

print("\n===== VALIDATION =====")
print(loader.validate(parsed))

assert len(parsed["parts"]) == 1
assert len(parsed["articles"]) == 2

assert isinstance(parsed["parts"][0], LegalPart)
assert isinstance(parsed["articles"][0], LegalArticle)

assert parsed["parts"][0].part_number == "I"
assert parsed["parts"][0].title == "Part I"

assert parsed["articles"][0].article_number == "1"
assert parsed["articles"][1].article_number == "2"

assert parsed["articles"][0].part_number == "I"
assert parsed["articles"][1].part_number == "I"

assert loader.validate(parsed) is True

print("\nConstitution Loader Test Passed Successfully!")