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