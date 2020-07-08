import requests
import json


class King:
    def __init__(self, word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.key = word
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
        }
        self.data = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }
    
    def get_data(self):
        # 发送一个post请求，data为请求体字典
        response = requests.post(self.url, headers=self.headers, data=self.data)
        return response.content
    
    def parse_data(self, data):
        # loads方法将json字符串转换成python字典
        dict_data = json.loads(data)
        try:
            return dict_data['content']['out']
        except:
            return dict_data['content']['word_mean'][0]
    
    def run(self):
        response = self.get_data()
        print(self.parse_data(response))


if __name__ == "__main__":
    word = input("请输入要翻译的词语：")
    king = King(word)
    king.run()