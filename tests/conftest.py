import pytest

pytest_plugins = "pytester"


@pytest.fixture
def ctestdir(testdir):
    testdir.makeconftest("""
        import sys
        if "pytest_dependency" not in sys.modules:
            pytest_plugins = "pytest_dependency"
    """)
    return testdir
