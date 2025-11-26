from books.book_repository import BookRepository


def test_add_book():
    repo = BookRepository()
    count_before = len(repo.get_books())

    new_book = repo.add_book({
        "title": "Test Book",
        "author": "Tester",
        "year": 2024
    })

    assert new_book["id"] > 0
    assert len(repo.get_books()) == count_before + 1


def test_delete_book():
    repo = BookRepository()
    repo.add_book({"title": "ToDelete", "author": "A", "year": 2023})
    last_id = repo.all_books[-1].id
    assert repo.delete_book(last_id) is True
