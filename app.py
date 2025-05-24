import cv2
from flask import Flask, render_template, request
import os
def generate_video(prompt):
    print(f"Generating video for prompt: {prompt}")

    # Make sure static/videos/ exists
    os.makedirs("static/videos", exist_ok=True)

    # Create a dummy video file
    filename = f"{prompt.replace(' ','_')}.mp4"
    filepath = os.path.join("static/videos", filename)

    with open(filepath, "wb") as f:
        f.write(b"0" * 1024) # Simulate 1KB video content

    return f"Video Generated : <a href='/static/videos/{filename}' target='_blank'>Download / View </a> "

    


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['prompt']
        filename = generate_video(user_input)
        return render_template('index.html', video_url=f"/static/videos/{filename}" )
    return render_template('index.html')






















if __name__ == "__main__":
    app.run(ssl_context=('certs/cert.pem', 'certs/key.pem'))