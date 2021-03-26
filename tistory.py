import os
import markdown
import requests
from bs4 import BeautifulSoup


client_id = "ce09b063c495d4ac0b913e029dceb9a5"

Secret_key = "ce09b063c495d4ac0b913e029dceb9a5288bb57ce391293337e754117a0561b261a19cf9"

access_token = "4521d88efad56d2400498add71e36d91_56b2a74c7a47cfb90f0b0f2ba54379ee"

blog_name = "shinyo17"

redirect_uri = "http://shinyo17.tistory.com"
state_param = ""
output_type = "json"

path = "./"
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith(".md")]
files = [file_list_py[0], file_list_py[1]]

for i in files:
    with open(i, 'r') as file:
        a = file.readlines()
        b = ''.join(a)
        html = markdown.markdown(b)
        soup = BeautifulSoup(html, 'html.parser')
        title = f"{os.path.splitext(i)[0]}"
        url = 'https://www.tistory.com/apis/post/write'
        data = {
            'access_token': access_token,
            'blogName': blog_name,
            # 'output': 'lxml',
            'title': title,
            'content': "타이가",
            'viisibility': '3',
            'category': '953637',
        }
        resp = requests.post(url, data=data)
        print(resp.text)
