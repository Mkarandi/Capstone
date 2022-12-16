# S.A.D NFTs

![image](Kila_la_heri_images/grad.jpg)

Capstone - December 2022

## Team Members
- Dylan Olsen
- Maurine Arandi
- Sam Johnson

## Motivation

- The motivation was to create an Ethereum based decentralized application that will allow users to originate and store artwork as the NFTs. Along the way, we also created a gallery to display and sell the NFTs. We used Solidity via Remix to create the contracts and Streamlit for the dApp. All artwork is registered to Pinata



## Executive Summary

In our attempt to stay true to our mission, we have created a new tool that allows our investors to invest in digital artwork with simplicity, cost reduction and decentralization using solidity contracts under ERC721 standards. 

Users are able to create their own digital, tokenize it and own it as an NFT. There is also an option to buy/sell already existing art through our gallery. 

## Technology and Techniques

### Technology
- import os
- import json
- import openai
- import imageio
- import requests
- from web3 import Web3
- from PIL import Image
- from io import BytesIO
- from io import StringIO
- import streamlit as st
- from pathlib import Path
- from dotenv import load_dotenv
- load_dotenv()
- from streamlit_player import st_player
- from transaction import send_transaction, get_balance, generate_account
- from pinata import pin_file_to_ipfs, pin_json_to_ipfs, convert_data_to_json
- Solidity
- Remix IDE

### Techniques
There were 3 main components to successfully creating the dApp:
1. Create the contract in Remix IDE using solidity
2. Create and deploy the contract using python and streamlit
3. Register the artwork to pinata





