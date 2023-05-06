import requests
import random
import string
length = 6
characters = string.ascii_lowercase + string.digits
password = 'Awawa1919!'
while True:
    random_string = ''.join(random.choice(characters) for i in range(length))
    cookies = {
        'session': 'f2a974e6-5960-4d9a-8031-5a597b1f49e5',
    }

    re = requests.get('https://ouo.xn--ed-2bc.tk/api/csrftoken',cookies=cookies)
    token = re.json()['token']
    print(token)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-CSRFToken': token,
    }
    json_data = {
        'username': random_string,
        'password': password,
    }
    response = requests.post('https://ouo.xn--ed-2bc.tk/api/register', cookies=cookies, headers=headers, json=json_data)
    if response.status_code == 200:
        name = response.json()['display_name']
        print(f"成功ｗ {name}:{password}")