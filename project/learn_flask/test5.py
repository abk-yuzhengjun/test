from aip import AipSpeech

''' APPID '''

APP_ID = '17979629'
API_KEY = 'nXN1oufPemKwEfGTBqLey1n9'
SECRET_KEY = 'dGV0AsvP7OktIR5oXWzKtpm7CN1zmYyO'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)


result = client.synthesis('你好百度', 'zh', 1, {
    'vol': 5,
})

if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)
else:
    print(result)