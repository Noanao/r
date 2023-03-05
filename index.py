import requests
 
url = 'https://www.google.co.jp/search'
 
#接続
response = requests.get(url, params={'q': '理系夫婦'})
 
#検索結果表示
print(response.text)
