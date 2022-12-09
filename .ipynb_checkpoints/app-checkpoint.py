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
################################################################################
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
################################################################################

# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():

    # Load NFT ABI
    with open(Path('./contracts/compiled/nfToken_abi.json')) as f:
        nfToken_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=nfToken_abi
    )
    return contract

contract = load_contract()


################################################################################
# Create NFT
################################################################################

accounts = w3.eth.accounts
account = accounts[0]
nft_details = st.text_input("Non-Fungible Token Details", value="Token Completion")
if st.button("Create NFT"):
    contract.functions.CreateNFT(account, nft_details).transact({'from': account, 'gas': 1000000})

