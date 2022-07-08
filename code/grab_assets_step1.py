from web3 import Web3
import json
import requests
import common
import time
import storage

ABI = json.loads(open("ERC721_ABI.json").read())
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/02dbb85360b44913a1cec6d144a79e56'))

def get_single_tokenURI(contract_address, index):
    contract_address = Web3.toChecksumAddress(contract_address)
    contract = w3.eth.contract(contract_address, abi=ABI)
    tokenURI = contract.functions.tokenURI(index).call()
    return tokenURI

def insert_collections():
    start = time.time()
    for i, collection in enumerate(common.input_json("../data/collection_details.json")):
        if i % 10 == 0:
            print("%d: %d"%(i, time.time() - start))
        storage.insert(collection, collection["address"])

def insert_assets(collection):
    print("%s begin"%(collection["address"]))
    

if __name__ == "__main__":
    # insert_collections()
    
    # tokenURI_list = []
    # start = time.time()
    # for i, collection in enumerate(common.input_json("../data/collection_details.json")):
    #     if i % 10 == 0:
    #         print("%d: %d"%(i, time.time() - start))
    #     tokenURI = None
        
    #     count = int(collection["count"])
        
    #     for i in range(0, count + 1):
    #         try:
    #             tokenURI = get_single_tokenURI(collection["address"], i)
    #             break
    #         except:
    #             continue
    #     tokenURI_list.append((tokenURI, i))
    #     break
        
    # common.output_json("../data/tokenURI.txt", tokenURI_list)
