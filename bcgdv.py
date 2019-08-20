import requests
import json

BASE_URL =  'https://interns.bcgdvsydney.com'
Key_Url_Endpoint = '/api/v1/key'

Application_Data = {
    'name': 'Bharath krish',
    'email': 'bk271094@gmail.com'
    }

getKeyJson = requests.get(BASE_URL+Key_Url_Endpoint, timeout = 15000)
print(getKeyJson)

key_Value = getKeyJson.json().get('key')
expires_Value = getKeyJson.json().get('expires')

submit_Url_Endpoint = '/api/v1/submit?apiKey='+key_Value

Application_Post_Request = requests.post(BASE_URL+submit_Url_Endpoint, data=json.dumps(Application_Data))
print(Application_Post_Request)