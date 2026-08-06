from lawscape.data_ingestion.data_models import (
    LegalArticle,
    LegalPart,
)


part = LegalPart(
    part_number="I",
    title="Part I",
)

article = LegalArticle(
    article_number="1",
    content="India, that is Bharat, shall be a Union of States.",
    part_number="I",
)

print("===== PART =====")
print(part)

print("\n===== ARTICLE =====")
print(article)

assert part.part_number == "I"
assert part.title == "Part I"

assert article.article_number == "1"
assert article.part_number == "I"

print("\nData Models Test Passed Successfully!")
