from flask import Flask, send_from_directory

app = Flask(__name__)

# This route serves images dynamically based on the filename
@app.route('/image/<filename>')
def serve_image(filename):
    # Specify the directory where images are stored
    image_directory = 'static/images'
    
    # Return the requested image file from the images directory
    return send_from_directory(image_directory, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

