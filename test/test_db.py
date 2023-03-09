import cursor as cursor
import psycopg2
import pytest


@pytest.fixture(scope="session")
def db_conn() -> None:
    """Test connection to database."""
    conn = psycopg2.connect(
        host="localhost", port="5432", dbname="waifu-db", user="root", password="root"
    )
    yield conn
    conn.close()


def test_my_query(db_conn: {cursor}) -> None:
    """Test database data and connection by running a query."""
    cursor_conn = db_conn.cursor()
    cursor_conn.execute("SELECT * FROM waifu_table")
    rows = cursor_conn.fetchall()
    assert len(rows) == 15425
