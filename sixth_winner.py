# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:06:36 2023

@author: aspirex99
"""

import base64
import streamlit as st
import plotly.express as px

df = px.data.iris()

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


#img = get_img_as_base64(r"https://gcdnb.pbrd.co/images/YtAsRPjbYOLF.gif?o=1")
x = " "

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://gcdnb.pbrd.co/images/qi7M8xYRcT10.gif?o=1");
background-size: 99%;
background-position: top center;
background-repeat: non-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
#background-image: url("data:image/png;base64,{x}");
background-position: center center; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#-------------------------------------------------------Button---------------------------------------

# CSS and HTML to center-align the button and customize its appearance
centered_button = """
<style>
.center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Adjust this value to control vertical alignment */
}

.center button {
    width: 150px; /* Adjust the width to make the button larger */
    height: 150px; /* Adjust the height to make the button larger */
    border-radius: 50%; /* Make the button circular */
    background-color: #007BFF; /* Set the background color */
    color: white; /* Set the text color */
    font-size: 16px; /* Adjust the font size */
    cursor: pointer;
}
</style>

<div class="center">
    <button id="showImage">Show Image</button>
    <img id="giphyImage" style="display: none; max-width: 300px;" src="https://i.giphy.com/media/VRhsYYBw8AE36/200w.webp" alt="Giphy Image">
</div>

<script>
    document.getElementById("showImage").addEventListener("click", function() {
        // Show the Giphy image
        document.getElementById("giphyImage").style.display = "block";

        // After a delay of 5 seconds, hide the button
        setTimeout(function() {
            document.getElementById("showImage").style.display = "none";
        }, 5000);
    });
</script>
"""

st.markdown(centered_button, unsafe_allow_html=True)


#-----------------------------------------------------------------------------------------
# buttons
# CSS and HTML to center-align the buttons, Giphy image, and customize their appearance
centered_content = """
<style>
.center {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 120vh; /* Adjust this value to control vertical alignment */
}

.center .giphy-container {
    margin-bottom: 20px; /* Add spacing between Giphy and buttons */
}

.center .button-container {
    display: flex;
    align-items: center;
    flex-wrap: wrap; /* Allow buttons to wrap to a new line if needed */
    justify-content: center;
}

.center button {
    width: 80px; /* Adjust the width to make the button larger */
    height: 40px; /* Adjust the height to make the button larger */
    border-radius: 40%; /* Make the button circular */
    background-color: #007BFF; /* Set the background color */
    color: white; /* Set the text color */
    font-size: 16px; /* Adjust the font size */
    cursor: pointer;
    margin: 10px; /* Add spacing between buttons */
}

.center img {
    max-width: 300px; /* Customize the size of the Giphy image */
}
</style>

<div class="center">
    <div class="giphy-container">
        <img src="https://media1.giphy.com/media/VRhsYYBw8AE36/200w.webp?cid=ecf05e47qw7a3jba6noh19nnderc28uoprhou5n587x24iy2&ep=v1_gifs_search&rid=200w.webp&ct=g" alt="Giphy Image">
    </div>
    <div class="button-container">
        <a href="https://grandprizewinners-6uye2ujttyngreyi2hznbh.streamlit.app/" target="_blank"><button>Button 1</button></a>
        <a href="https://www.link2.com" target="_blank"><button>Button 2</button></a>
        <a href="https://www.link3.com" target="_blank"><button>Button 3</button></a>
    </div>
    <div class="button-container">
        <a href="https://www.link4.com" target="_blank"><button>Button 4</button></a>
        <a href="https://www.link5.com" target="_blank"><button>Button 5</button></a>
        <a href="https://www.link6.com" target="_blank"><button>Button 6</button></a>
    </div>
</div>
"""

st.markdown(centered_content, unsafe_allow_html=True)
