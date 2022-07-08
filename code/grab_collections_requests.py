import requests

payload = {"id":"RankingsPagePaginationQuery",
           "query":"query RankingsPagePaginationQuery(\n  $chain: [ChainScalar!]\n  $count: Int\n  $createdAfter: DateTime\n  $cursor: String\n  $parents: [CollectionSlug!]\n  $sortBy: CollectionSort\n) {\n  ...RankingsPage_data\n}\n\nfragment PaymentAssetLogo_data on PaymentAssetType {\n  symbol\n  asset {\n    imageUrl\n    id\n  }\n}\n\nfragment RankingsPage_data on Query {\n  rankings(after: $cursor, chains: $chain, first: $count, sortBy: $sortBy, parents: $parents, createdAfter: $createdAfter) {\n    edges {\n      node {\n        createdDate\n        name\n        slug\n        logo\n        isVerified\n        nativePaymentAsset {\n          ...PaymentAssetLogo_data\n          id\n        }\n        statsV2 {\n          floorPrice {\n            unit\n            eth\n          }\n          numOwners\n          totalSupply\n          sevenDayChange\n          sevenDayVolume {\n            unit\n          }\n          oneDayChange\n          oneDayVolume {\n            unit\n          }\n          thirtyDayChange\n          thirtyDayVolume {\n            unit\n          }\n          totalVolume {\n            unit\n          }\n        }\n        id\n        __typename\n      }\n      cursor\n    }\n    pageInfo {\n      endCursor\n      hasNextPage\n    }\n  }\n}\n",
           "variables":{
               "chain":"null",
               "count":100,
               "createdAfter":"null",
               "cursor":"YXJyYXljb25uZWN0aW9uOjk5",
               "parents":"null",
               "sortBy":"ONE_DAY_VOLUME"}}
proxies = {
  "http": "http://127.0.0.1:10809",
  "https": "http://127.0.0.1:10809",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# headers = {
#     "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36'
# }
# res = requests.get('https://opensea.io/rankings', proxies=proxies)

# res = requests.post(url = "https://api.opensea.io/graphql/", 
#               data = payload,
#               proxies=proxies,
#               headers=headers)

res = requests.post(url = "https://202.160.129.36:443/graphql/", 
              data = payload,
              proxies=proxies,
              headers=headers)
print(res.text)