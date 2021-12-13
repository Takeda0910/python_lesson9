from bs4 import BeautifulSoup
import requests
import time
import schedule
import datetime

from twitter import *

url = "https://www.amazon.co.jp/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97-SHARP-SJ-AF50G-R-%E3%83%97%E3%83%A9%E3%82%BA%E3%83%9E%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B0%E3%83%A9%E3%83%87%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AC%E3%83%83%E3%83%89/dp/B08KJ85RJ5?ref_=fspcr_pl_dp_2_2272928051" 
HEADERS = {"Accept": "*/*",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36}"}
    

res = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser")

def do_task():
    count = 0
    while True:
        print(datetime.datetime.now())
        to_cart_button = str(soup.select("#add-to-cart-button")) # カートに入れるボタン
        print(to_cart_button)
        time.sleep(3)

        if to_cart_button and count == 0:    # Twitterに在庫有りツイート
            yes_stock_status()             
            print("在庫有り")
            count+=1
        elif to_cart_button and count >= 1:  # 在庫有りから変化なし
            print("pass")
            pass    
        else:
            nothing_stock_status()           # Twitterに在庫無しツイート
            print("在庫無し")               
            count = 0


def main():
    schedule.every(3).hours.do(do_task)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
