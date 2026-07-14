# LawScape Legal Ontology

## Overview

The LawScape ontology defines the structure of the Living Legal Knowledge Graph.
It specifies:

- Legal entities
- Legal relationships
- Graph constraints
- Temporal versioning
- Entity hierarchy

This ontology serves as the single source of truth for:

- Knowledge Graph Construction
- Neo4j Database
- Heterogeneous Graph Neural Networks
- Explainable AI
- Legal Ecosystem Impact Analysis (LEIA)
- Temporal Judgment Dependency Analysis (TJDA)

---

# Entity Hierarchy

```
Legal System
│
├── Constitution
│     └── Article
│
├── Act
│     ├── Chapter
│     │      └── Section
│     │              └── Subsection
│
├── Rule
├── Regulation
├── Government Notification
├── Circular
├── Bill
├── Amendment
├── Judgment
├── Court
├── Judge
├── Ministry
├── Department
├── Industry
├── Company
├── Legal Concept
├── Legal Principle
└── International Treaty
```

---

# Relationship Categories

The ontology supports multiple relationship types.

## Structural Relationships

- contains
- belongs_to

## Legislative Relationships

- amends
- modifies
- repeals
- replaces

## Judicial Relationships

- interprets
- cites
- follows
- overrules

## Regulatory Relationships

- implements
- enforced_by
- issued_by

## Dependency Relationships

- depends_on
- affects
- conflicts_with

## Semantic Relationships

- related_to
- applicable_to

## Temporal Relationships

- has_version
- supersedes
- precedes
- succeeds

---

# Design Principles

- Every entity has a unique identifier.
- Every relationship is directed.
- Every relationship has semantic meaning.
- Every legal version is preserved.
- No legal information is deleted.
- The graph is explainable by design.

---

# Research Contributions

The ontology enables:

- Living Legal Knowledge Graph
- Temporal Legal Evolution
- Version-Aware Reasoning
- Legal Ecosystem Impact Analysis (LEIA)
- Temporal Judgment Dependency Analysis (TJDA)
- Explainable Legal Intelligence