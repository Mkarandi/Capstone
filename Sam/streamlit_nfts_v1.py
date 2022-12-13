import streamlit as st

# From openai_generation.ipynb import nft_image_link
from openai_generation import nft_image_link


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

# Add a sidebar and set its style
st.sidebar.title("S.A.D. NFTs")
st.sidebar.markdown(
    """
    <style>
    h2 {
        color: #4682B4;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add a selectbox for users to choose the category of items they want to view
category = st.sidebar.selectbox("Choose a category", ["Christmas Cartoons", "AI Holidays", "Dylan's Nifty NFTs"])

# Add a button for users to click to refresh the page
if st.sidebar.button("Refresh"):
    pass

# Add a main panel to display the items in the selected category
st.header("Category: {}".format(category))

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

# Add a photo backsplash of an ocean
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

text = st.text_input("What should I create?")

num_images = st.slider("How many images?", 1, 5)

ok = st.button("GO!")

if ok:
    st.image(nft_image_link, width=400)

# Display a placeholder message
st.text("Displaying items in the {} category".format(category))

# Add a subheader to the main panel
if st.checkbox("Show items"):
    display_items(category)

# Add a second page to the app
if st.button("Go to next page"):
    st.header("Second page")
    st.text("This is the second page of the app")


    # Add a button to navigate back to the main page
if st.button("Go back to main page"):
    st.header("Category: {}".format(category))
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

