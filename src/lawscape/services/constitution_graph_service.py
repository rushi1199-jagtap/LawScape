"""
LawScape Constitution Graph Service

Builds the Constitution of India knowledge graph from
the source dataset and exposes the resulting legal graph
through the LegalGraphService.

Author: Rushikesh Jagtap
Project: LawScape
"""

from pathlib import Path

from lawscape.data_ingestion.constitution_loader import (
    ConstitutionLoader,
)
from lawscape.graph.constitution_graph_builder import (
    ConstitutionGraphBuilder,
)
from lawscape.graph.graph_builder import LawGraphBuilder
from lawscape.services.legal_graph_service import (
    LegalGraphService,
)


class ConstitutionGraphService:
    """
    High-level service for building and accessing the
    Constitution of India legal knowledge graph.
    """

    def __init__(
        self,
        source: str,
    ):
        self.source = Path(source)

        self.loader = ConstitutionLoader()

        self.graph_builder = LawGraphBuilder()

        self.constitution_builder = ConstitutionGraphBuilder(
            self.graph_builder
        )

        self.service = None

    # ---------------------------------------------------------
    # Build Graph
    # ---------------------------------------------------------

    def build(self) -> LegalGraphService:
        """
        Load, parse, validate, and build the Constitution graph.

        Returns:
            LegalGraphService: service connected to the
            constructed legal graph.
        """

        raw_data = self.loader.load(
            str(self.source)
        )

        parsed_data = self.loader.parse(
            raw_data
        )

        if not self.loader.validate(
            parsed_data
        ):
            raise ValueError(
                "Invalid Constitution data."
            )

        self.constitution_builder.build(
            parts=parsed_data["parts"],
            articles=parsed_data["articles"],
        )

        graph = self.graph_builder.get_graph()

        self.service = LegalGraphService(
            graph
        )

        return self.service

    # ---------------------------------------------------------
    # Service Access
    # ---------------------------------------------------------

    def get_service(self) -> LegalGraphService:
        """
        Return the underlying LegalGraphService.

        Raises:
            RuntimeError: if the graph has not been built yet.
        """

        if self.service is None:
            raise RuntimeError(
                "Constitution graph has not been built yet."
            )

        return self.service

    # ---------------------------------------------------------
    # Graph Access
    # ---------------------------------------------------------

    def get_graph(self):
        """
        Return the constructed NetworkX graph.
        """

        return self.graph_builder.get_graph()