import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

#сколько редиректов происходит
size = response.history
print((f"Сколько редиректов происходит от изначальной точки назначения до итоговой: {len(size)}"))

#итоговый URL
last_url = response.history[len(size)-1]
print(f"URL итоговый: {last_url.url}")