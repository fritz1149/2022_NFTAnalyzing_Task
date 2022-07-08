import time
import json
import requests
import common

proxies = {
  "http": "http://127.0.0.1:10809",
  "https": "http://127.0.0.1:10809",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49",
    "Accept-Encoding": "gzip, deflate, br"
}

def test():
    slug = "fluf"
    url = "https://api.opensea.io/api/v1/collection/%s"%(slug)
    response = requests.get(url = url, proxies = proxies)
    print(response.text)

if __name__ == "__main__":
    collections = []
    lost_collections = []
    multiple_collections = []
    begin_time = time.time()
    
    for i, href in enumerate(common.input_lines("../data/collection_hrefs.txt")):
        if i % 10 == 0:
            print("progress %d: %d"%(i, time.time() - begin_time))
            
        slug = href.replace("https://opensea.io/collection/", "").rstrip()
        url = "https://api.opensea.io/api/v1/collection/%s"%(slug)
        res = json.loads(requests.get(url=url, proxies=proxies).text).get("collection")
        # print(type(res))
        # for key in res.keys():
        #     print(key)
        primary_asset_contracts = res["primary_asset_contracts"]
        if not len(primary_asset_contracts) == 1:
            if len(primary_asset_contracts) > 1:
                print("more than 1 primary_asset_contracts:\n%s"%(slug))
                multiple_collections.append(slug)
                continue
            else:
                print("0 primary_asset_contracts:\n%s"%(slug))
                lost_collections.append(slug)
                continue
                
        primary_asset_contracts = primary_asset_contracts[0]
        stats = res["stats"]
        collections.append({
            "name": primary_asset_contracts["name"],
            "address": primary_asset_contracts["address"],
            "asset_contract_type": primary_asset_contracts["asset_contract_type"],
            "created_date": primary_asset_contracts["created_date"],
            "owner": primary_asset_contracts["owner"],
            "schema_name": primary_asset_contracts["schema_name"],
            "description": primary_asset_contracts["description"],
            "img_url": primary_asset_contracts["image_url"],
            "symbol": primary_asset_contracts["symbol"],
            "count": stats["total_supply"],
            "average_price": stats["average_price"],
            "floor_price": stats["floor_price"],
            "total_sales": stats["total_sales"]
        })
        common.sleep_random(0.5, 1)
        # break
    common.output("../data/lost_collections.txt", lost_collections)
    common.output("../data/multiple_collections.txt", multiple_collections)
    common.output_json("../data/collection_details.json", collections)
    # test()