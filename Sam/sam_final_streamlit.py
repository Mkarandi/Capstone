import os
import openai
import requests
from dotenv import load_dotenv
import streamlit as st

from PIL import Image
from io import BytesIO
import imageio


showcase_list = ["Christmas.jpeg", "Christmas_v2.jpeg", "Diwali.jpeg", "eid_al-fitr.jpeg", "Hanukkah.jpeg", "hanukkah2.jpeg"]
pricing_list = ["1", "2", "3", "4", "5", "6"]

def main_page():

    st.title("NFT SHOWCASE")
    st.markdown(
        """
        <style>
        h1 {
            font-size: 80px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.image(["output1.png", "output2.png"], width=220)
    st.image(showcase_list, width=220)
    


def page2():

    st.markdown("# A.I. Holiday")
    st.markdown(
        """
        <style>
        h1 {
            font-size: 80px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    text = st.text_input("What image would you like to create and tokenize?")

    ok = st.button("GO!")

    if ok:
        openai.api_key = ""

        nft_image = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024"
)

        nft_image_link = nft_image["data"][0]["url"]

    # Read the image from the URL
        url = nft_image_link
        img = imageio.imread(url)

    # Save the image to a file or stream in PNG format
        imageio.imwrite('output1.png', img)

    st.image('output1.png', width=400)

    
def page3():

    st.markdown("# Kila La Heri")
    st.markdown(
        """
        <style>
        h1 {
            font-size: 80px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    for image in range(len(showcase_list)):
        st.image(showcase_list[image], caption=pricing_list[image], width=400, output_format="auto")

    

def page4():

    st.markdown("# Dylan's Nifty NFTs")
    st.markdown(
        """
        <style>
        h1 {
            font-size: 80px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    text = st.text_input("What image would you like to create and tokenize?")

    ok = st.button("GO!")

    if ok:
        openai.api_key = ""

        nft_image = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024"
)

        nft_image_link = nft_image["data"][0]["url"]

    # Read the image from the URL
        url = nft_image_link
        img = imageio.imread(url)

    # Save the image to a file or stream in PNG format
        imageio.imwrite('output2.png', img)

    st.image('output2.png', width=400)
    

page_names_to_funcs = {
    "Welcome Page": main_page,
    "A.I. Holiday": page2,
    "Kila La Heri": page3,
    "Dylan's Nifty NFTs": page4,
}

st.sidebar.title("S.A.D. NFTs")
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


# Add a button for users to click to refresh the page
if st.sidebar.button("Refresh"):
    pass

# Add simple black background for easy viewing
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://www.solidbackgrounds.com/images/3840x2160/3840x2160-black-solid-color-background.jpg');
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Display a placeholder message
st.text("Displaying items in the {} category".format(selected_page))

