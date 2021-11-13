import requests
import json
import argparse 

from requests.models import Response

date = input()
id = input()
def req(date,id):
    if(date,id):
        
        response = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="+date+"&api_key=MQZfRETJLmLcQnTGwIdB6wfB6ci3dug8Sb3UMJU3")
    else:
        print("Sorry Nothing could be found")

    print(response.status_code)
    print(response.json())


req(date,id)    
