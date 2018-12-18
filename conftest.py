import pytest
from fixture.application import Application

fixture = None
target = None


@pytest.fixture(scope="session", autouse=True)
def app():
    global fixture
    global target
    fixture = Application(base_url="https://www.stoloto.ru/")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
