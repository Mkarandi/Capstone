import os
import openai
import requests
from dotenv import load_dotenv
import streamlit as st

from PIL import Image
from io import BytesIO
import imageio


showcase_list = ["img-soGYJAiYW0pyRRR4gVwDT76q.png", "Christmas.jpeg", "Christmas_v2.jpeg", "Diwali.jpeg", "eid_al-fitr.jpeg", "Hanukkah.jpeg", "hanukkah2.jpeg"]

def main_page():

    # Add a title and set its style
    st.title("NFT SHOWCASE")
    st.markdown(
        """
        <style>
        h1 {
            color: #FF6947;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.image("output.png", width=200)
    st.image(showcase_list, width=200)
    

    # Add a main panel to display the items in the selected category
    #st.header("{}".format(selected_page))

    #st.sidebar.markdown("# Welcome page :balloon:")

def page2():
    #st.sidebar.markdown("# A.I. Holiday :snowflake:")
    st.markdown("# A.I. Holiday :snowflake:")

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
        imageio.imwrite('output.png', img)

    st.image('output.png', width=400)

    ################################################################################
    # Use Pinata to bridge the gap to uploading files to IPFS
    ################################################################################

    # st.markdown("## Decentralize your Art")
    # artwork_name = st.text_input("Name the Art")
    # artist_name = st.text_input("Name the Artist")

    # Use the Streamlit `file_uploader` function create the list of digital image file types(jpg, jpeg, or png) that will be uploaded to Pinata.
    # file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])

    # token_account = st.selectbox("Select the address you would like to save the Non-Fungible Token to:", options=accounts)
    # token_details = st.text_input("Artwork Details", value="Genesis Event for Non-Fungible Token")

    # if st.button("Decentralize Artwork"):
    #     # Use the `pin_artwork` helper function to pin the file to IPFS
    #     artwork_ipfs_hash, token_json = pin_artwork(artwork_name, file)

    #     artwork_uri = f"ipfs://{artwork_ipfs_hash}"

    #     tx_hash = contract.functions.registerArtwork(
    #         token_account,
    #         artwork_name,
    #         artist_name,
    #         artwork_uri,
    #         token_json['image']
    #     ).transact({'from': account, 'gas': 1000000})
    #     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    #     st.write("Transaction receipt mined:")
    #     st.write(dict(receipt))
    #     st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
    #     st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{artwork_ipfs_hash})")
    #     st.markdown(f"[Artwork IPFS Image Link](https://ipfs.io/ipfs/{token_json['image']})")

    # st.markdown("---")

################################################################################
# Display NFT
################################################################################

    # st.markdown(f"### Display Token Identification Details")
    # token_id = st.number_input("Enter the Token ID to display", value=0, step=1)
    # token_uri = st.text_input("Paste Artwork IPFS Image Link")

    # if st.button("Display Token Details"):
    #     st.write(f"The Non-Fungible Token was distributed to {token_account}")
    #     st.write(f"The Non-Fungible Token's tokenURI is {token_uri}")

    
def page3():
    #st.sidebar.markdown("# Kila La Heri :tada:")
    st.markdown("# Kila La Heri :tada:")
    st.image(showcase_list, width=200, output_format="auto")
    

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

# Main Page function call to display showcase
#main_page()




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

