import pytest
from fixture.application import Application



@pytest.fixture
def app():
    fixture = Application()
    return fixture



