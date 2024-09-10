import requests

def get_dict_from_api(url:str)->dict:
    try:
        response = requests.get(url)
        print(dir(response))
        json_data = response.json()
        return json_data
    
    except requests.exceptions.ConnectionError as e:
        raise requests.exceptions.ConnectionError(f"Connection error occurred: {e}")
