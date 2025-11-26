from app import app


def test_get_books():
    client = app.test_client()
    res = client.get("/books")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)


def test_get_unknown():
    client = app.test_client()
    res = client.get("/book/99999")
    assert res.status_code == 404
