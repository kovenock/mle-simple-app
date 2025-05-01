import pytest

def pytest_addoption(parser):
    """Add command line options for pytest."""
    parser.addoption(
        "--base-url",
        dest="base_url",
        action="store",
        default="http://localhost:80",
        help="Base URL for the API tests"
    )