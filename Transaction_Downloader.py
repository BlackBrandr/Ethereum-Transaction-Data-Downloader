import requests
import json

url = "http://api.etherscan.io/api?module=account&action=txlist&address=0x829BD824B016326A401d083B33D092293333A830&startblock=0&endblock=999999999&sort=asc&apikey=U6AQW35PH7PWMAGPHG4KEBD4VV8PAKKBTU"


wallets=[]
with open("amllist.txt") as file:
    wallets = file.readlines()
    wallets = [line.rstrip() for line in wallets]
    
for addr in wallets:
    url = "http://api.etherscan.io/api?module=account&action=txlist&address=" +addr+"&startblock=0&endblock=999999999&sort=asc&apikey=U6AQW35PH7PWMAGPHG4KEBD4VV8PAKKBTU"

    sonuc = requests.get(url)
    sonuc = sonuc.text
    
    json_object = json.loads(sonuc)
    jsonFile = open("amllist/"+addr+".json", "w")
    jsonFile.write(str(json_object))
    jsonFile.close()
    
    print(" + 1 \n") 