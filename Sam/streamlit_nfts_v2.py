import os
import openai
import requests
from dotenv import load_dotenv
import streamlit as st

def main_page():

    # Add a title and set its style
    st.title("S.A.D. NFTs")
    st.markdown(
        """
        <style>
        h1 {
            color: #FF6347;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Add a main panel to display the items in the selected category
    #st.header("{}".format(selected_page))

    #st.sidebar.markdown("# Welcome page :balloon:")

def page2():
    #st.sidebar.markdown("# A.I. Holiday :snowflake:")
    st.markdown("# A.I. Holiday :snowflake:")

    text = st.text_input("What image would you like to create and tokenize?")

    ok = st.button("GO!")

    if ok:
        openai.api_key = "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"

        nft_image = openai.Image.create(
            prompt=text,
            n=1,
            size="1024x1024"
)

        nft_image_link = nft_image["data"][0]["url"]

        st.image(nft_image_link, width=400)
    

def page3():
    #st.sidebar.markdown("# Kila La Heri :tada:")
    st.markdown("# Kila La Heri :tada:")
    

def page4():
    #st.sidebar.markdown("# Dylan's Nifty NFTs :tada:")
    st.markdown("# Dylan's Nifty NFTs :tada:")
    

page_names_to_funcs = {
    "Welcome Page": main_page,
    "A.I. Holiday": page2,
    "Kila La Heri": page3,
    "Dylan's Nifty NFTs": page4,
}

st.sidebar.title("S.A.D. NFTs")
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()


# Add a sidebar and set its style
# st.sidebar.markdown(
#     """
#     <style>
#     h2 {
#         color: #4682B4;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Add a selectbox for users to choose the category of items they want to view
# category = st.sidebar.selectbox("Choose a category", ["Christmas Cartoons", "AI Holidays", "Dylan's Nifty NFTs"])


# Add a button for users to click to refresh the page
if st.sidebar.button("Refresh"):
    pass

# Add a main panel to display the items in the selected category
#st.header("{}".format(selected_page))

# Add some style to the main panel
st.markdown(
    """
    <style>
    h3 {
        color: #6495ED;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a photo backsplash of a Christmas tree
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://wallpaperaccess.com/full/1367742.jpg');
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# text = st.text_input("What image would you like to create and tokenize?")

# ok = st.button("GO!")

# if ok:

#     openai.api_key = "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"

#     nft_image = openai.Image.create(
#         prompt=text,
#         n=1,
#         size="1024x1024"
# )

#     nft_image_link = nft_image["data"][0]["url"]

#     st.image(nft_image_link, width=400)


# Display a placeholder message
st.text("Displaying items in the {} category".format(selected_page))

# # Add a subheader to the main panel
# if st.checkbox("Show items"):
#     display_items(selected_page)

# Add a second page to the app
# if st.button("Go to next page"):
#     st.header("Second page")
#     st.text("This is the second page of the app")


#     # Add a button to navigate back to the main page
# if st.button("Go back to main page"):
#     st.header("Category: {}".format(selected_page))
#     st.markdown(
#         """
#         <style>
#         h3 {
#             color: #6495ED;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
#     st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('https://wallpaperaccess.com/full/1367742.jpg');
#         background-size: cover;
#         background-repeat: no-repeat;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

