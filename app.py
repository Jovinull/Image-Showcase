from flask import Flask, render_template, send_from_directory
import os
import re

app = Flask(__name__)

@app.route('/')
def index():
    image_folder = 'static/images'
    images = os.listdir(image_folder)
    images = [img for img in images if img.endswith(('jpg', 'jpeg', 'png', 'gif'))]

    def extract_date(img_name):
        match = re.match(r'(\d{4})\.(\d{2})\.(\d{2})_(\d+)', img_name)
        if match:
            year, month, day, _ = match.groups()
            return f'{year}-{month}-{day}'
        return '9999-99-99'

    images.sort(key=extract_date)

    image_descriptions = {
        img: f"{img[:4]}/{img[5:7]}/{img[8:10]} - Foto {img[11] if '_' in img else ''}" for img in images
    }

    return render_template('index.html', images=images, image_descriptions=image_descriptions)

@app.route('/static/images/<filename>')
def get_image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)
