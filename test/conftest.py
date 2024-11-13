import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("C:\\Tools\\AddressBook\\AddressBook.exe")
    request.addfinlizer(fixture.destroy)
    return fixture
