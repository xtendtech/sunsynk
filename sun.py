import requests,json
import pprint
from requests.auth import HTTPBasicAuth
import os


def get_posts():
    url = f'https://api.sunsynk.net/oauth/token'
    my_email = os.getenv('sunsynk_email')
    my_password = os.getenv('sunsynk_password')
 
    payload = {'areaCode': 'sunsynk',
                'client_id': 'csp-web',
                'grant_type': 'password',
                'password': f"{my_password}",
                'source': 'sunsynk',
                'username': f"{ my_email}" }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'User-Agent':'Thunder Client'    }
    
    try:
        response = requests.post(url,json=payload,headers=headers)
        response.raise_for_status() 
    except requests.exceptions.HTTPError as errh: 
        print("HTTP Error") 
        print(errh.args[0]) 
    except requests.exceptions.ReadTimeout as errrt: 
        print("Time out") 
    except requests.exceptions.ConnectionError as conerr: 
        print("Connection error") 
    except requests.exceptions.RequestException as errex: 
        print("Exception request") 
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None
    return response.json()

def get_bearer_token(posts:json):
    my_refresh_token = posts["data"]["refresh_token"]
    return  my_refresh_token 
def main():
    global the_bearer_token_string 
    posts = get_posts()
    the_bearer_token_string = get_bearer_token(posts)
    if posts:
                                               
        my_access_token = posts["data"]["access_token"]
        my_refresh_token = posts["data"]["refresh_token"]
        # print(my_access_token)
        # global the_bearer_token_string
        
        # the_bearer_token_string = ('Bearer '+my_refresh_token )
        the_bearer_token_string = ('Bearer '+  my_access_token )
        
        # print(the_bearer_token_string)
        # print('****************************************************')
        # print('Your access token is: ' + my_access_token)
        # print(json.dumps(parsed, indent=4))
        # the_bearer_token_string = 'Bearer 4AXXX583qWqKn9Smu7XSkoLKZ04'
        global  headers_and_token 
        headers_and_token = {
        'Content-type':'application/json', 
        'Accept':'application/json',
        'Authorization': the_bearer_token_string }

        plant_id_endpoint = ('https://api.sunsynk.net/api/v1/plants?page=1&limit=10&name=&status=')
        r = requests.get( plant_id_endpoint, headers=headers_and_token)
        data_response = r.json()
        print(json.dumps(data_response, indent=4))
        # print(data_response)
        print('****************************************************')
        plant_id_and_pac = data_response['data']['infos']
        # print( plant_id_and_pac )
        for d in plant_id_and_pac:
            your_plant_id = d['id']
            your_plant_pac = d['pac']
            current_gen_w = str(your_plant_pac)
        # print('Your plant id is: ' + str(your_plant_id))
        print('****************************************************')
        # You can take actions based on the generation amount, e.g. trigger IoT device, SMS, adjust inverter settings like push to grid
        print('Your current power generation is: ' + str(current_gen_w) +'W')
    #     # print('First Post Body:', posts[0]['body'])
    else:
        print('Failed to fetch posts from API.')
    
def read_settings():        
        print('****************************************************')
        plant_id_endpoint = ('https://api.sunsynk.net/api/v1/common/setting/2301176142/read')
        r = requests.get( plant_id_endpoint, headers=headers_and_token)
        data_response = r.json()
        print(json.dumps(data_response, indent=4))
        return None


        return None
def set_settings():
        # settings saved
        plant_id_endpoint = ('https://api.sunsynk.net/api/v1/common/setting/2301176142/set')
        save_settings={}
        posts1 ["batteryEmptyV"] = 48
        r = requests.post(plant_id_endpoint, headers=headers_and_token,json =save_settings)
        data_response = r.json()
        print(json.dumps(data_response, indent=4))
        return None

# print functions showing token and current generation in Watts
if __name__ == '__main__':
    main()