# S.A.D NFTs


Capstone - December 2022


- Dylan Olsen
- Maurine Arandi
- Sam Johnson

<img src=(https://user-images.githubusercontent.com/104539357/208269105-a2a2e349-e0cd-4511-bf77-638d35db40e1.png) width="100" height="100">

<img src=(https://user-images.githubusercontent.com/104539357/208269108-d675a327-bba7-417e-b0e7-ebc88720e19f.png) width="100" height="100">

## Overview and summary

We were motivated to create an Ethereum based decentralized application that will allow users to originate and store artwork as the NFTs. Along the way, we also created a gallery to display and sell the NFTs. We used Solidity via Remix to create the contracts and Streamlit for the dApp. All artwork is registered to IPFS via Pinata.

In our attempt to stay true to our mission, we have created a new tool that  our investors will utilize to invest in digital artwork with simplicity, cost reduction and decentralization using solidity contracts under ERC721 standards. 

Users are able to create their own digital, tokenize it and own it as an NFT. There is also an option to buy/sell already existing art through our gallery. 

## Technology requirements

1. Git clone repository to your local files:

`git clone https://github.com/Mkarandi/S.A.D-NFTs`

2. Open a .ipynb file and pip install the following packages:
      
`!pip install streamlit`

`!pip install streamlit_player`

`!pip install openai`

`!pip install web3`

`!pip install json`

`!pip install imageio`
      
3. Open the app.py file

4. Find the following code block on line 119 and 338:
      
`openai.api_key = ""`

5. Update the string to match your OpenAI API key.

6. Create a .env file to hold API keys, such as:
      `PINATA_API_KEY=
      OPENAI_API_KEY=
      PINATA_SECRET_API_KEY=
      WEB3_PROVIDER_URI=
      SMART_CONTRACT_ADDRESS=
      MNEMONIC=`
 
7. Deploy the contract in Remix IDE using solidity, MetaMask, and Ganache 
 
8. Open terminal and direct yourself to where the file was cloned to and run this to open application:
      
      `streamlit run app.py`

## Techniques

There were 3 main components to successfully creating the dApp:

1. Create and deploy the contract in Remix IDE using solidity, MetaMask, and Ganache

2. Integrate OpenAi’s API key to generate artificially intelligent produced artwork
 
3. Register the artwork to IPFS through Pinata
 
4. Use a Helper file of Web3 transaction functions to implement selling gallery artwork







