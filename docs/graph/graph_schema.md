# LawScape Graph Schema

## Purpose

This document defines the official graph structure used by LawScape.

It specifies:

- Node types
- Edge types
- Edge direction
- Graph constraints
- Temporal modeling
- Version tracking

---

# Node Categories

## Constitutional

- Constitution
- Article

## Legislative

- Act
- Chapter
- Section
- Subsection
- Rule
- Regulation
- Bill
- Amendment

## Judicial

- Judgment
- Court
- Judge

## Administrative

- Ministry
- Department
- Notification
- Circular

## Domain

- Industry
- Company

## Semantic

- Legal Concept
- Legal Principle

## International

- Treaty

---

# Graph Direction Principles

Every edge is directed.

Examples

Judgment
→ interprets
→ Section

Amendment
→ modifies
→ Section

Rule
→ implements
→ Act

Act
→ governs
→ Industry

Court
→ delivers
→ Judgment

Judge
→ authors
→ Judgment

---

# Temporal Design

Every legal entity stores

- version
- effective_date
- end_date
- status

Every edge stores

- timestamp
- confidence
- source
- jurisdiction

Historical versions are never deleted.

---

# Explainability

Every prediction must provide:

- reasoning path
- supporting entities
- supporting relationships
- confidence score

---

# Research Goal

The graph supports:

- Living Legal Intelligence
- LEIA
- TJDA
- Explainable AI
- Temporal Reasoning