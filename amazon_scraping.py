from bs4 import BeautifulSoup
import requests
import time
import schedule
import datetime
import json

from twitter import *

url = "https://www.amazon.co.jp/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97-SHARP-SJ-AF50G-R-%E3%83%97%E3%83%A9%E3%82%BA%E3%83%9E%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B0%E3%83%A9%E3%83%87%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AC%E3%83%83%E3%83%89/dp/B08KJ85RJ5?ref_=fspcr_pl_dp_2_2272928051" 
HEADERS = {"Accept": "*/*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36}"}
    

class AmazonScraping():
    
    def __init__(self):
        res = requests.get(url, headers=HEADERS)
        self.soup = BeautifulSoup(res.text, "html.parser")
        
        self.stock_dict = {}
        self.stock_dict["B08KJ85RJ5"] = "在庫あり"
        self.json_string = json.dumps(self.stock_dict, ensure_ascii=False)
        
        with open("stock.json", "w") as f:
            f.write(self.json_string)
            print(f"init_write: {self.json_string}")
        

    def do_task(self):
        print(datetime.datetime.now())
        try:
            to_cart_button = str(self.soup.select("#add-to-cart-button")) # カートに入れるボタン要素取得
            print(to_cart_button)
            time.sleep(3)
        
            if to_cart_button:                        # ボタンが存在すれば                     
                with open("stock.json", "r") as f:
                    self.stock_dict = json.loads(f.read())
                    print(f"read: {self.stock_dict}")
                    
                    if self.stock_dict == {"B08KJ85RJ5": "在庫あり"}:
                        print("在庫有りから変化なし")    # 変化なし
                    else:
                        print(f"在庫有り")
                        yes_stock_status()          # Twitterに在庫有りツイート
                        
            else:                                     # ボタンが存在しなければ
                with open("stock.json", "w") as f:
                    self.json_string = ""
                    f.write(self.json_string)
                    print(f"else_write: {self.json_string}")
                    print("在庫無し")
                    nothing_stock_status()           # Twitterに在庫無しツイート
        except:
            None    
                                    

    def main(self):
        schedule.every(3).hours.do(self.do_task)
        while True:
            schedule.run_pending()
            time.sleep(1)

amazon = AmazonScraping()

if __name__ == "__main__":
    amazon.main()
