import os
from flask import Flask, request, jsonify
import sqlite3
from convert import extract_audio, getTranscribedAudio
from db_controller import create_table, insert_data, get_data



app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_video():

    create_table()
    # Assuming the frontend sends the video as a file
    video = request.files['file']
    video_path = f"videos/{video.filename}"
    # audio = 'audio/test.wav'

    video.save(video_path)

    audio = extract_audio(video_path)
    transcript = getTranscribedAudio(audio)
    
    
    #  Save URL to SQLite database
    insert_data(video_path, transcript)

    return jsonify({
        'message': 'Video saved successfully',
        'status': '200',
        'transcript': transcript,
        'video': video_path
        })

@app.route('/get_video/<int:video_id>', methods=['GET'])
def get_video(video_id):
    data = get_data(video_id)
    
    if data:
        return jsonify({'id': video_id,
                        'video_url': data[0],
                        'transcript': data[1]})
    else:
        return jsonify({'error': 'Video not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
