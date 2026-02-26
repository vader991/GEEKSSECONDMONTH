import sqlite3

DB_NAME = "library.db"


def create_connection(db_name: str = DB_NAME):
    return sqlite3.connect(db_name)


def create_table(conn):
    query = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        author TEXT NOT NULL,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    );
    """
    conn.execute(query)
    conn.commit()


def insert_books(conn):
    conn.execute("DELETE FROM books;")

    books = [
        ("1984", "George Orwell", 1949, "Dystopian", 328, 5),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopian", 288, 4),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Dystopian", 194, 6),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 3),
        ("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 1997, "Fantasy", 223, 7),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fairy tale", 96, 10),
        ("The Alchemist", "Paulo Coelho", 1988, "Adventure", 208, 5),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Classic", 671, 2),
        ("The Master and Margarita", "Mikhail Bulgakov", 1967, "Classic", 384, 2),
        ("Murder on the Orient Express", "Agatha Christie", 1934, "Detective", 256, 4),
    ]

    query = """
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    conn.executemany(query, books)
    conn.commit()


def get_books_by_author(conn, author):
    query = """
    SELECT id, name, author, publication_year, genre, number_of_pages, number_of_copies
    FROM books
    WHERE author = ?
    ORDER BY name ASC;
    """
    cursor = conn.execute(query, (author,))
    return cursor.fetchall()


if __name__ == "__main__":
    connection = create_connection()
    create_table(connection)
    insert_books(connection)

    books = get_books_by_author(connection, "Agatha Christie")

    for book in books:
        print(book)

    connection.close()