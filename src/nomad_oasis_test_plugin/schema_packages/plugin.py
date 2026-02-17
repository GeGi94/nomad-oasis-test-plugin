from nomad.metainfo import (
    MSection,
    Quantity,
    Section,
)
from nomad.config.models.plugins import SchemaPackageEntryPoint


class TestSection(MSection):
    """
    Minimal test section for verifying plugin loading.
    """

    m_def = Section(label="TestSection")

    name = Quantity(
        type=str,
        description="A simple test quantity."
    )


class TestSchema(SchemaPackageEntryPoint):
    def load(self):
        return TestSection
