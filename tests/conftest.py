from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from .example_app import build_wheke


@pytest.fixture
def client() -> Generator[TestClient]:
    with TestClient(build_wheke().create_app()) as client:
        yield client
