import requests
import json

test_url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1) http-запрос любого типа без параметра method
response1 = requests.get(test_url)
print(f"http-запрос GET без параметра method. Результат ответа: {response1.text}")

# 2) http-запрос не из списка. Например, HEAD
response2 = requests.head(test_url)
print(f"http-запрос не из списка. Например, HEAD. Результат: {response2.text}")

# 3) http-запрос с правильным значением method
response3 = requests.post(test_url, data={"method":"POST"})
print(f"http-запрос POST с правильным значением method. Результат: {response3.text}")

# 4)
json_text = '{"methods":[{"method":"GET"},{"method":"POST"},{"method":"PUT"},{"method":"PATCH"},{"method":"DELETE"},{"method":"COPY"},{"method":"HEAD"},{"method":"OPTIONS"},{"method":"LINK"},{"method":"UNLINK"},{"method":"PURGE"},{"method":"LOCK"},{"method":"UNLOCK"},{"method":"PROPFIND"},{"method":"VIEW"}]}'
obj = json.loads(json_text)
list = obj['methods']
size = len(list)

# проверяет все возможные сочетания http-запроса GET и значений параметра method из json_text
print("Cочетания http-запроса GET и значений параметра method")
for i in list:
    r = requests.get(test_url,params=i)
    print(f"http-запрос GET и значение параметра method {i} : {r.text}")

# проверяет все возможные сочетания http-запроса POST и значений параметра method из json_text
print("Cочетания http-запроса POST и значений параметра method")
for i in list:
    r = requests.post(test_url,data=i)
    print(f"http-запрос POST и значение параметра method {i} : {r.text}")

# проверяет все возможные сочетания http-запроса HEAD и значений параметра method из json_text
print("Cочетания http-запроса HEAD и значений параметра method")
for i in list:
    r = requests.head(test_url,data=i)
    print(f"http-запрос HEAD и значение параметра method {i} : {r.text}")

# проверяет все возможные сочетания http-запроса DELETE и значений параметра method из json_text
print("Cочетания http-запроса DELETE и значений параметра method")
for i in list:
    r = requests.delete(test_url,data=i)
    print(f"http-запрос DELETE и значение параметра method {i} : {r.text}")

# проверяет все возможные сочетания http-запроса PUT и значений параметра method из json_text
print("Cочетания http-запроса DELETE и значений параметра method")
for i in list:
    r = requests.put(test_url,data=i)
    print(f"http-запрос PUT и значение параметра method {i} : {r.text}")

# проверяет все возможные сочетания http-запроса PATCH и значений параметра method из json_text
print("Cочетания http-запроса PATCH и значений параметра method")
for i in list:
    r = requests.patch(test_url,data=i)
    print(f"http-запрос PATCH и значение параметра method {i} : {r.text}")

# проверяет все возможные сочетания http-запроса OPTIONS и значений параметра method из json_text
print("Cочетания http-запроса OPTIONS и значений параметра method")
for i in list:
    r = requests.options(test_url,data=i)
    print(f"http-запрос OPTIONS и значение параметра method {i} : {r.text}")