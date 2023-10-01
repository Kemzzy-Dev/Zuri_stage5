import sqlite3

# Initialize SQLite database

 

def create_table():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()  

    c.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            video_url TEXT,
            transcript TEXT
        )
    ''')
    conn.commit()

def insert_data(video_path, transcript):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()  

    c.execute('INSERT INTO videos (video_url, transcript) VALUES (?,?)', (video_path,transcript))
    conn.commit()

def get_data(video_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()  

    c.execute('SELECT video_url, transcript FROM videos WHERE id = ?', (video_id,))
    video_data = c.fetchone()
    return video_data
