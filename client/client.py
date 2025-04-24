import urllib.request
import time

# Даем серверу немного времени на запуск
time.sleep(3)

urls = [
    "http://server:8000/",
    "http://server:8000/git",
    "http://server:8000/docker"
]

for url in urls:
    print(f"\n🔗 Запрос: {url}")
    response = urllib.request.urlopen(url)
    print(response.read().decode("utf8"))
    response.close()
