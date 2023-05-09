import requests
import os

print(os.getcwd())
resp = requests.delete("https://reqres.in/api/users/40")

print(resp.status_code)