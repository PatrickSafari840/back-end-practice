import sqlite3

def view_comments():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # Select all names and messages from the comments table
    c.execute('SELECT name, message FROM comments')
    comments = c.fetchall()
    conn.close()
    return comments

if __name__ == '__main__':
    comments = view_comments()
    for comment in comments:
        print(f'Name: {comment[0]}, Message: {comment[1]}')
