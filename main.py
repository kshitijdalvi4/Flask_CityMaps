import streamlit as st
import os
from PIL import Image
import webbrowser

# Configuration
UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def geography_info(topology):
    topology_dict = {
        "Plain": "monochrome network of city map of plain area, where there are bigger squared grids and symmetry, highly-highly zoomed-in hd",
        "Coastal": "monochrome network of city map near coastal area, where there is a main highway road near the coast (water body) and a stream of narrow roads towards the city, zoomed-in hd",
        "Hill": "monochrome network of city map of hilly areas with dense forest cover, where there are curved roads, highly-highly zoomed-in hd"
    }
    
    topology_links = {
        "Plain": "https://colab.research.google.com/drive/1wJHQqNLihM3cjkYzGiN45YGGqERYylhK#scrollTo=yEErJFjlrSWS",
        "Coastal": "https://colab.research.google.com/drive/1UDU-icPSm3VenAqu051sXcPelr3Ao9jE#scrollTo=-YAFLvWWrSdM",
        "Hill": "https://colab.research.google.com/drive/1YhDcAqSENr2kVFw8rzR0qlA4fHsGmsSB#scrollTo=xSKWBKFPArKS"
    }
    
    if topology in topology_dict:
        webbrowser.open(topology_links[topology])
        return f"Launching Colab notebook for {topology} topology"
    return "Please select a valid topology."

def main():
    st.title("City Maps Explorer 🗺️")
    
    # Navigation sidebar
    page = st.sidebar.radio("Go to", ["Home", "App", "Edit"])
    
    if page == "Home":
        st.header("Welcome to City Maps Explorer")
        st.write("This application helps you analyze different city topologies.")
        
    elif page == "App":
        st.header("Map Analysis")
        topology = st.selectbox(
            "Select Topology", 
            ["", "Plain", "Coastal", "Hill"],
            index=0
        )
        
        if st.button("Analyze") and topology:
            result = geography_info(topology)
            st.success(result)
            
    elif page == "Edit":
        st.header("Upload Map Image")
        uploaded_file = st.file_uploader(
            "Choose an image file", 
            type=ALLOWED_EXTENSIONS
        )
        
        if uploaded_file and allowed_file(uploaded_file.name):
            # Save file
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            # Display image
            st.success(f"File saved to: {file_path}")
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Map", use_column_width=True)

if __name__ == "__main__":
    main()