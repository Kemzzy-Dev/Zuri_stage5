import os
from flask import Flask, request, jsonify
import cloudinary.uploader
import sqlite3
from convert import extract_audio, getTranscribedAudio



app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY AUTOINCREMENT, video_url TEXT, transcript TEXT)''')
conn.commit()

# Cloudinary configuration
cloudinary.config(
    cloud_name='dqxp8sid3',
    api_key='583537237715728',
    api_secret='DPUMbU3-3MGZ0fGK9lgtoxJXJfI'
)

@app.route('/upload', methods=['POST'])
def upload_video():
    # Assuming the frontend sends the video as a file
    video = request.files['video']

    video.save()

    # audio = extract_audio(video)
    # transcript = getTranscribedAudio(audio)
    
    # # Upload video to Cloudinary
    # result = cloudinary.uploader.upload(video)

    # # Save Cloudinary URL to SQLite database
    # url = result['url']
    # c.execute('INSERT INTO videos (video_url) VALUES (?)', (url,))
    # c.execute('INSERT INTO videos (transcript) VALUES (?)', (transcript,))
    # conn.commit()

    return jsonify({'message': "done"})

@app.route('/get_video/<int:video_id>', methods=['GET'])
def get_video(video_id):
    c.execute('SELECT url FROM videos WHERE id = ?', (video_id,))
    url = c.fetchone()
    if url:
        return jsonify({'video_url': url[0]})
    else:
        return jsonify({'error': 'Video not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
