import pytest

from cookiecutter_pypackage_example.foo import foo


@pytest.fixture
def bar() -> str:
    return "bar"


def test_foo(bar: str) -> None:
    assert foo(bar) == "foobar"
