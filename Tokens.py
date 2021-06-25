import requests
import json
import time

# 1) создавал задачу
create_task = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(create_task.text)
token = {"token":obj['token']}
seconds = obj['seconds']

# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
check_result_before_task_is_done = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(check_result_before_task_is_done.text)

# 3) & 4) ждал нужное количество секунд. Делал один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
time.sleep(seconds)
check_result_ater_task_is_done = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(check_result_ater_task_is_done.text)