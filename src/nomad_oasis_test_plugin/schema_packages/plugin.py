from nomad.metainfo import SchemaPackage, MSection, Quantity, Section

m_package = SchemaPackage()


class TestSection(MSection):
    """
    Minimal test section for verifying plugin loading.
    """
    m_def = Section(label="TestSection")

    name = Quantity(type=str, description="A simple test quantity.")


# IMPORTANT: registers all sections/quantities in this module into the package
m_package.__init_metainfo__()


# Entry point target: MUST be a SchemaPackage instance
test_schema = m_package
