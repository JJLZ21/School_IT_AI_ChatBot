import sqlite3


def connect_db():
    try:
        conn = sqlite3.connect('issue.db')
        return conn
    except Error as e:
        return e


conn = connect_db()
cu = conn.cursor()


'''
# use to create inpreson issue table

cu.execute("""CREATE TABLE inPersonIssue ( date text, room integer)""")

'''


def store_in_preson_issue(conn, date, room):
    with conn:
        conn.cursor().execute("INSERT INTO inPersonIssue VALUES (:date, :room)", {
            'date': date, 'room': room})
    conn.close()
