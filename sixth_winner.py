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



#-----------------------------------------------------------------------------------------
# buttons
# CSS and HTML to center-align the buttons, Giphy image, and customize their appearance
centered_content = """
import streamlit as st

# HTML and JavaScript for the centered layout with buttons
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
    max-width: 600px; /* Customize the size of the Giphy image */
}
</style>

<div class="center">
    <div class="giphy-container">
        <img id="giphy-image" src="https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1" alt="Giphy Image">
    </div>
    <div class="button-container">
        <button id="back-button">Back</button>
        <button id="next-button">Next</button>
    </div>
</div>

<script>
    const images = [
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1", // Giphy image
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1", // Image for Button 2
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1", // Image for Button 3
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1", // Image for Button 4
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1", // Image for Button 5
        "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1"  // Image for Button 6
    ];

    const giphyImage = document.getElementById("giphy-image");
    const backButton = document.getElementById("back-button");
    const nextButton = document.getElementById("next-button");
    let currentIndex = 0;

    // Function to update the image
    function updateImage() {
        giphyImage.src = images[currentIndex];
    }

    // Event listeners for the buttons
    backButton.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateImage();
    });

    nextButton.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % images.length;
        updateImage();
    });
</script>
"""

st.markdown(centered_content, unsafe_allow_html=True)

