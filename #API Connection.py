#API  Connection
import requests
baseurl ="https://pokeapi.co/api/v2/"
def pokeinfo(name):
    url=f"{baseurl}/pokemon/{name}"
    r=requests.get(url)
    
    if r.status_code==200:
        pokedata=r.json()
        return pokedata
    else:
        print("failed to retrieve data")
pkname="pikachu"
pkinfo=pokeinfo(pkname)
if pkinfo:
    print(f"{pkinfo["name"]}")
    print(f"{pkinfo["height"]}")


