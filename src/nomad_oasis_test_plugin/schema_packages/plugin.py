from nomad.config.models.plugins import SchemaPackageEntryPoint
from nomad.metainfo import SchemaPackage, MSection, Quantity, Section

m_package = SchemaPackage()


class TestSection(MSection):
    m_def = Section(label="TestSection")
    name = Quantity(type=str, description="A simple test quantity.")


m_package.__init_metainfo__()


class TestSchemaEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        return m_package


test_schema = TestSchemaEntryPoint(
    name="TestSchema",
    description="Minimal test schema for verifying plugin loading.",
)
