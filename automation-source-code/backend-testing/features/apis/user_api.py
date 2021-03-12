import json
import requests
from utils import print_exception

base_url = "https://gorest.co.in/public-api/"

def get_user_by_name(name = ""):
    url = base_url + "users?" + "Name=" + name
    try:
        response = requests.get(url)
        return response
    except OSError as err:
        print_exception("request get_user_by_name failed:", err)  

def get_user_list():
    url = base_url + "users?data"
    try:
        response = requests.get(url)
        return response
    except OSError as err:
        print_exception("request get_user_list failed:", err) 
        