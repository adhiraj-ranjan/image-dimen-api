from flask import Flask, render_template, request, jsonify
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "key_secrat_for_app"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload/', methods=['POST'])
def upload_image():
  file = request.files['file']
  if file:
      try:
          img = Image.open(file)
          dimensions = img.size
          img.close()
          return jsonify({"status": "ok",
               "width" : dimensions[0],
               "height" : dimensions[1]
            })
      except Exception as e:
          return jsonify({
          "status": "fail",
          "message": str(e)
            })
  else:
        return jsonify({
          "status": "fail",
          "message": "invalid file type"
        })

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)