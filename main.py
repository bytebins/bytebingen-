import threading
import requests
import random
import string
from terminut import printf as print, inputf as input, init, BetaConsole, log

def send_request():
    title = ''.join(random.choices(string.ascii_lowercase, k=5))
    content = ''.join(random.choices(string.ascii_lowercase, k=5))
    payload = {"title": title, "content": content, "password": "", "autoburn": False}
    url = "https://bytebin.lol/api/v1/create"
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        paste_id = response.json().get('id', 'Unknown')
        print(f"(*) https://bytebin.lol/p/{paste_id}")
    else:
        log.error("error")  

def main():
    init(debug=False)
    num_threads = int(input('Pastes to create: '))
    console = BetaConsole(speed=2)
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(console,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    log.success("success")

if __name__ == "__main__":
    main()
