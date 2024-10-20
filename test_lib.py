from mylib.transform_load import load
from mylib.query import query


def test_load():
    test1 = load()
    assert test1 == "db loaded or already loaded"


def test_query():
    test2 = query()
    assert test2 == "query successful"


if __name__ == "__main__":
    test_load()
    test_query()