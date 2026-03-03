import requests
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.example.com"
response = requests.get(url, verify=False)
print(response)
print(response.status_code)
print(response.content)

data = {"name" : "Salah" , "message" : "Hello!"}
url = "https://httpbin.org/post"
response = requests.post(url, json=data, verify=False)
response_data = response.json()
print(response_data)

response = requests.get("https://httpbin.org/status/404", verify=False)
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")

url = "https://httpbin.org/delay/10"
try:
    response = requests.get(url, timeout=5, verify=False)
except requests.exceptions.Timeout as err:
    print(err)

auth_token = "XXXXXXXX"
headers = { "Authorization" : f"Bearer {auth_token}" }
url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers, verify=False)
print(response.json())

url = "https://www.example.com"
response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]
print(f"Title: {title}")
print(f"Content: {content}")
print(f"Links: {links}")