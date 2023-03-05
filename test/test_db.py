import psycopg2
import pytest

@pytest.fixture(scope='session')
def db_conn():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        dbname='waifu-db',
        user='root',
        password='root'
    )
    yield conn
    conn.close()

def test_my_query(db_conn):
    cursor = db_conn.cursor()
    cursor.execute('SELECT * FROM waifu_table')
    rows = cursor.fetchall()
    assert len(rows) == 15425
