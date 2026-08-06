from lawscape.data_ingestion.parser import LegalDocumentParser
from lawscape.data_ingestion.data_models import (
    LegalArticle,
    LegalPart,
)


parser = LegalDocumentParser()

text = """
PART I

Article 1
India, that is Bharat, shall be a Union of States.

Article 2
Parliament may by law admit into the Union...
"""

parts = parser.extract_parts(text)

articles = parser.extract_articles(
    text,
    part_number="I",
)

print("===== PARTS =====")
print(parts)

print("\n===== ARTICLES =====")
print(articles)

assert len(parts) == 1
assert isinstance(parts[0], LegalPart)
assert parts[0].part_number == "I"

assert len(articles) == 2

assert isinstance(articles[0], LegalArticle)
assert isinstance(articles[1], LegalArticle)

assert articles[0].article_number == "1"
assert articles[1].article_number == "2"

assert articles[0].part_number == "I"
assert articles[1].part_number == "I"

print("\nParser Test Passed Successfully!")