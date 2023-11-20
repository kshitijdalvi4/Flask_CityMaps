from flask import Flask,render_template,request,flash
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def Image():
    pass

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/App.html")
def App():
    return render_template("App.html")

@app.route("/edit",methods=["GET","POST"])
def edit():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "Error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return 'No fILE sEELECTED'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(f"File saved to: {os.path.join(app.config['UPLOAD_FOLDER'], filename)}")

            #imasge()
            return render_template("App.html")
        
    return render_template("App.html")
    
      


app.run(debug=True,port=5001)

