import os
import cv2
import numpy as np
from flask import Flask, request, send_from_directory, render_template_string, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

# ========== CSS ==========
CSS_STYLE = """
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
  margin: 0;
  padding: 0;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}
.container {
  background: white;
  width: 90%;
  max-width: 800px;
  padding: 40px;
  border-radius: 15px;
  box-shadow: 0 15px 30px rgba(0,0,0,0.1);
  text-align: center;
}
h1 {
  color: #333;
  margin-bottom: 30px;
  font-weight: 700;
  font-size: 2.2rem;
}
.upload-area {
  border: 2px dashed #ccc;
  border-radius: 10px;
  padding: 30px;
  margin-bottom: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
}
.upload-area:hover {
  border-color: #4285f4;
  background-color: #f8f9fa;
}
.upload-icon {
  font-size: 48px;
  color: #4285f4;
  margin-bottom: 10px;
}
input[type="file"] {
  display: none;
}
.control-panel {
  margin: 20px 0;
  padding: 20px;
  background: #f8f9fa;
  border-radius: 10px;
}
.button {
  padding: 12px 24px;
  background: #4285f4;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-block;
  margin: 10px 5px;
}
.button:hover {
  background: #3367d6;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}
.button.download {
  background: #34a853;
}
.button.download:hover {
  background: #2d9249;
}
.slider-container {
  margin: 20px 0;
  text-align: left;
}
.slider-container label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #555;
}
.slider {
  width: 100%;
  height: 5px;
  border-radius: 5px;
  -webkit-appearance: none;
  background: #ddd;
  outline: none;
}
.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: #4285f4;
  cursor: pointer;
}
.image-container {
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.image-wrapper {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-bottom: 20px;
  flex-wrap: wrap;
}
.image-box {
  margin: 10px;
  text-align: center;
}
.image-box h3 {
  margin-bottom: 10px;
  color: #555;
}
img {
  max-width: 600px;
  max-height: 600px;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}
img:hover {
  transform: scale(1.03);
}
.back-link {
  display: block;
  margin-top: 20px;
  color: #4285f4;
  text-decoration: none;
  font-weight: 600;
}
.action-buttons {
  display: flex;
  justify-content: center;
  gap: 15px;
  margin-top: 20px;
}
.checkbox-container {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin: 15px 0;
  padding: 5px;
}
.checkbox-container input[type="checkbox"] {
  display: inline-block;
  width: 18px;
  height: 18px;
  margin-right: 10px;
  cursor: pointer;
}
.checkbox-container label {
  font-weight: 600;
  color: #555;
  cursor: pointer;
}
"""

# ========== INDEX HTML ==========
INDEX_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Image Sharpener</title>
  <style>{{ css }}</style>
</head>
<body>
  <div class="container">
    <h1>🔍 Professional Image Sharpener</h1>
    <form id="upload-form" method="POST" enctype="multipart/form-data">
      <div class="upload-area" id="drop-area" onclick="document.getElementById('file-input').click()">
        <div class="upload-icon">📁</div>
        <p>Click to select or drag and drop an image</p>
      </div>
      <input type="file" id="file-input" name="image" accept="image/*" required>
      <div class="control-panel">
        <div class="slider-container">
          <label for="intensity">Sharpening Intensity: <span id="intensity-value">2</span></label>
          <input type="range" id="intensity" name="intensity" class="slider" min="1" max="5" value="3">
        </div>
        
        <div class="checkbox-container">
          <input type="checkbox" id="grayscale" name="grayscale" value="yes">
          <label for="grayscale">Convert to Grayscale</label>
        </div>
        
        <button type="submit" class="button">Upload & Sharpen</button>
      </div>
    </form>
  </div>
  <script>
    const intensitySlider = document.getElementById('intensity');
    const intensityValue = document.getElementById('intensity-value');
    intensitySlider.addEventListener('input', function() {
      intensityValue.textContent = this.value;
    });
    const dropArea = document.getElementById('drop-area');
    const fileInput = document.getElementById('file-input');
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
      dropArea.addEventListener(eventName, preventDefaults, false);
    });
    function preventDefaults(e) {
      e.preventDefault();
      e.stopPropagation();
    }
    ['dragenter', 'dragover'].forEach(eventName => {
      dropArea.addEventListener(eventName, highlight, false);
    });
    ['dragleave', 'drop'].forEach(eventName => {
      dropArea.addEventListener(eventName, unhighlight, false);
    });
    function highlight() {
      dropArea.style.borderColor = '#4285f4';
      dropArea.style.backgroundColor = '#f0f7ff';
    }
    function unhighlight() {
      dropArea.style.borderColor = '#ccc';
      dropArea.style.backgroundColor = 'transparent';
    }
    dropArea.addEventListener('drop', handleDrop, false);
    function handleDrop(e) {
      const dt = e.dataTransfer;
      const files = dt.files;
      if (files.length) {
        fileInput.files = files;
      }
    }
  </script>
</body>
</html>
"""

# ========== RESULT HTML ==========
RESULT_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Result</title>
  <style>{{ css }}</style>
</head>
<body>
  <div class="container">
    <h1>✨ Sharpened Result</h1>
    <div class="image-container">
      <div class="image-wrapper">
        <div class="image-box">
          <h3>Processed Image</h3>
          <img src="{{ url_for('processed_file', filename=filename) }}" alt="Processed Image">
        </div>
      </div>
      
      <div class="action-buttons">
        <a href="{{ url_for('download_file', filename=filename) }}" class="button download">⬇️ Download Image</a>
        <a href="/" class="button">⏪ Go Back</a>
      </div>
    </div>
  </div>
</body>
</html>
"""

# ========== IMAGE PROCESSING FUNCTIONS ==========
def sharpen_image(input_path, output_path, intensity=5, grayscale=False):
    image = cv2.imread(input_path)
    
    # Convert to grayscale if option is selected
    if grayscale:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Convert back to 3 channels for consistent processing
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    
    # Create sharpening kernel with adjustable intensity
    kernel = np.array([[0, -1, 0],
                      [-1, 4 + intensity, -1],
                      [0, -1, 0]])
    
    # Apply sharpening filter
    sharpened = cv2.filter2D(image, -1, kernel)
    
    # Save the processed image
    cv2.imwrite(output_path, sharpened)

# ========== ROUTES ==========
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        intensity = int(request.form.get('intensity', 5))
        grayscale = 'grayscale' in request.form
        
        if file:
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
            
            file.save(input_path)
            sharpen_image(input_path, output_path, intensity, grayscale)
            
            return render_template_string(RESULT_HTML, filename=filename, css=CSS_STYLE)
    
    return render_template_string(INDEX_HTML, css=CSS_STYLE)

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(
        directory=app.config['PROCESSED_FOLDER'],
        path=filename,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True)
