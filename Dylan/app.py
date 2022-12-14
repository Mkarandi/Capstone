import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json
# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function

# Define the load_contract function
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts/compiled/artregistry_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS_2")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract


# Load the contract
contract = load_contract()

accounts = w3.eth.accounts
account = accounts[0]

################################################################################
# Helper functions to pin files and json to Pinata
################################################################################


def pin_artwork(artwork_name, artwork_file):
    # Pin the file to IPFS with Pinata
    ipfs_file_hash = pin_file_to_ipfs(artwork_file.getvalue())

    # Build a token metadata file for the artwork
    token_json = {
        "name": artwork_name,
        "image": ipfs_file_hash
    }
    json_data = convert_data_to_json(token_json)

    # Pin the json to IPFS with Pinata
    json_ipfs_hash = pin_json_to_ipfs(json_data)

    return json_ipfs_hash, token_json


def pin_appraisal_report(report_content):
    json_report = convert_data_to_json(report_content)
    report_ipfs_hash = pin_json_to_ipfs(json_report)
    return report_ipfs_hash

################################################################################
# Use Pinata to bridge the gap to uploading files to IPFS
################################################################################
st.markdown("## Decentralize your Art")
artwork_name = st.text_input("Name the Art")
artist_name = st.text_input("Name the Artist")

# Use the Streamlit `file_uploader` function create the list of digital image file types(jpg, jpeg, or png) that will be uploaded to Pinata.
file = st.file_uploader("Upload Artwork", type=["jpg", "jpeg", "png"])

token_account = st.selectbox("Select the address you would like to save the Non-Fungible Token to:", options=accounts)
token_details = st.text_input("Artwork Details", value="Genesis Event for Non-Fungible Token")

if st.button("Decentralize Artwork"):
    # Use the `pin_artwork` helper function to pin the file to IPFS
    artwork_ipfs_hash, token_json = pin_artwork(artwork_name, file)

    artwork_uri = f"ipfs://{artwork_ipfs_hash}"

    tx_hash = contract.functions.registerArtwork(
        token_account,
        artwork_name,
        artist_name,
        artwork_uri,
        token_json['image']
    ).transact({'from': account, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
    st.write("You can view the pinned metadata file with the following IPFS Gateway Link")
    st.markdown(f"[Artwork IPFS Gateway Link](https://ipfs.io/ipfs/{artwork_ipfs_hash})")
    st.markdown(f"[Artwork IPFS Image Link](https://ipfs.io/ipfs/{token_json['image']})")

st.markdown("---")

################################################################################
# Display NFT
################################################################################

st.markdown(f"### Display Token Identification Details")
token_id = st.number_input("Enter the Token ID to display", value=0, step=1)
token_uri = st.text_input("Paste Artwork IPFS Image Link")

if st.button("Display Token Details"):
    st.write(f"The Non-Fungible Token was distributed to {token_account}")
    st.write(f"The Non-Fungible Token's tokenURI is {token_uri}")
