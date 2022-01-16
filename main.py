from Mail_send import Mail
from bs4 import BeautifulSoup
import html5lib
import requests
import time
import multiprocessing


class Product_Tracker():

    def __init__(self):

        """
        BF 2042: 1015067
        AppleWatch: 998288
        """


        self.product_nummber = ""

        self.url_interdiscount = f"https://www.interdiscount.ch/de/search?search={self.product_nummber}"
        self.price = None







    def thread(self):

        y = 0

        while True:

            self.product_nummber = str(input("Product nummber >> "))
            self.product_nummber = str(self.product_nummber)
            self.url_interdiscount = f"https://www.interdiscount.ch/de/search?search={self.product_nummber}"

            multiprocessing.Process(target=self.time_update, name=f"thread{y}").start()
            y = y + 1



    def get_act_price(self):

        self.data = requests.get(self.url_interdiscount)
        self.html_code = BeautifulSoup(self.data.content, "html5lib")

        try:
            self.price = self.html_code.find(class_="_3H04_H").get_text()
        except:
            print("Error")





    def time_update(self):


        i = 0

        while True:

            self.thread_number = self.product_nummber
            self.get_act_price()
            self.temp_price = self.price


            if(i == 0):
                with open(f"log_file_{self.thread_number}.txt", "a") as file:
                    file.write(
                        "Actual price from article: " + str(self.thread_number) + " is: " + str(self.price) + "\n")
            else:
                None

            i = i + 1
            time.sleep(10)

            self.get_act_price()
            with open(f"log_file_{self.thread_number}.txt", "a") as file:
                file.write(f"Price after {i}h from article: " + str(self.thread_number) + " is: " + str(self.price) + "\n")



            if(self.temp_price == self.price):
                None
            else:
                self.Mail = Mail()

                self.Mail.mail["body"] = f"""
The product: {self.thread_number} has changed his Price.
-----------------------------------------------------------
The new Price is: {self.price}
"""
                self.Mail.send_mail()
                break






if __name__ == "__main__":
    tracker = Product_Tracker()
    tracker.thread()







"""
<div class="lLlyk8">
    <div class="krweWr czipba">
        <div class="_3H04_H">
            <span class="_8l1F7H">
                CHF
            </span>
            159
            <!-- -->
            .
            <span class="_1pPJlh">
                90
            </span>
        </div>
    </div>
"""