from web3 import Web3
import json
import requests
import common
import time

ABI = json.loads(open("ERC721_ABI.json").read())
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/02dbb85360b44913a1cec6d144a79e56'))

if __name__ == "__main__":
    collection_detials = common.input_json("../data/collection_details.json")
    token_URIs = common.input_json("../data/tokenURI.json")
    for collection, token_URI in zip(collection_detials, token_URIs):
        if token_URI[0] is None:
            continue
        protocol = token_URI[0].split(",", 1)
        if len(protocol) > 1:
            protocol = protocol[0]
        else:
            protocol = (token_URI[0].split("://", 1)[0])
        if protocol == "":
            continue

        
    