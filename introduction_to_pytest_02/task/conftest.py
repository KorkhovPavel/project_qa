import pytest


@pytest.fixture()
def function_fixture(request):
    print(f"\n function_fixture start of the test")

    def fin():
        print(f"\n function_fixture end of test")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def module_fixture(request):
    print(f"\n module_fixture start of the test")

    def fin():
        print(f"\n module_fixture end of test")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def session_fixture(request):
    print(f"\n session_fixture start of the test")

    def fin():
        print(f"\n session_fixture end of test")

    request.addfinalizer(fin)

