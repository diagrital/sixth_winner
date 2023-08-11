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
# Define the list of image URLs
# Define the list of image URLs
images = [
    "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
    "https://gcdnb.pbrd.co/images/g4rsoDUZqbEn.gif?o=1",
    "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
    "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
    "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1",
    "https://gcdnb.pbrd.co/images/kxWgiWDfzsUS.jpg?o=1"
]

# Define the Streamlit app
def main():
    st.title("Giphy Image Viewer")

    # Display the current image based on the selected index
    current_index = st.slider("Select Image", 1, len(images), 1)
    st.image(images[current_index - 1], caption=f"Image {current_index}", use_container_width=True)

    # Display numbered buttons for each image
    col1, col2 = st.beta_columns(2)
    for i, img_url in enumerate(images):
        button_clicked = False
        if i == (current_index - 1):
            button_clicked = True
        with col1 if i % 2 == 0 else col2:
            if st.button(f"Image {i + 1}", key=i, help=button_clicked):
                current_index = i + 1
                st.image(images[current_index - 1], caption=f"Image {current_index}", use_container_width=True)

if __name__ == "__main__":
    main()

