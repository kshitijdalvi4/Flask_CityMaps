'''from flask import Flask,render_template,request,flash
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
    
      


app.run(debug=True,port=5001)'''


from flask import Flask, render_template, request, redirect, url_for
import gradio as gr
import webbrowser

my_app = Flask(__name__)

def geography_info(topologies):
    topology_dict = {
        "Plain": "monochrome network of city map of plain area, where there are bigger squared grids and symmetry, highly-highly zoomed- in hd",
        "Coastal": "monochrome network of city map near coastal area, where there is a main highway road near the coast (water body) and a stream of narrow roads towards the city, zoomed-in hd",
        "Hill": "monochrome network of city map of hilly areas with dense forest cover, where there are curved roads, highly-highly zoomed-in hd"
    }

    # Assuming the user can select only one topology
    selected_topology = topologies[0] if topologies else None

    if selected_topology and selected_topology in topology_dict:
        description = topology_dict[selected_topology]

        # Dictionary to map topology to Colab notebook link
        topology_links = {
            "Plain": "https://colab.research.google.com/drive/1wJHQqNLihM3cjkYzGiN45YGGqERYylhK#scrollTo=yEErJFjlrSWS",
            "Coastal": "https://colab.research.google.com/drive/1UDU-icPSm3VenAqu051sXcPelr3Ao9jE#scrollTo=-YAFLvWWrSdM",
            "Hill": "https://colab.research.google.com/drive/1YhDcAqSENr2kVFw8rzR0qlA4fHsGmsSB#scrollTo=xSKWBKFPArKS"
        }

        # Open the corresponding Colab notebook link
        webbrowser.open(topology_links[selected_topology])

        return f"Launching Colab notebook for {selected_topology} with the selected description: {description}"
    else:
        return "Please select a valid topology."

@my_app.route('/')
def index():
    return render_template('index.html')

@my_app.route('/app')
def app():
    return render_template('App.html')

@my_app.route('/geography_info', methods=['POST'])
def process_form():
    topology = request.form.getlist('topology')
    result = geography_info(topology)
    
    # Redirect to the '/app' page after processing the form
    return redirect(url_for('app'))

@my_app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)

if __name__ == "__main__":
    my_app.run(debug=True)






