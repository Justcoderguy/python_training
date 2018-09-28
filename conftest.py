import pytest
from fixtures.application import Application
__author__ = 'pzqa'


@pytest.fixture(scope='session')
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
