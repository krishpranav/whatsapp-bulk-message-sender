#!/usr/bin/env python3

# imports
from selenium import webdriver
import csv
import time

messages = input(str("What's the message you want to send => "))
files = input(str("File of contacts => "))

users = []
with open(r"{}".format(files), encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = row[0]
        users.append(user)


class WhatsappBot:
    
    def __init__(self):
        self.message = messages
        self.contatos = users

        options = webdriver.ChromeOption()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path = './chromedriver')

    def SendMessage(self):
        link = 'https://web.whatsapp.com/'
        self.driver.get(link)
        time.sleep(10)

        for contato in self.contatos:
            try:
                whatsappsendlink = 'https://web.whatsapp.com/send?phone='+ contato + '&text=' + self.message
                self.driver.get(link)
                time.sleep(5)
                chat_box = self.driver.find_element_by_class_name('_1U1xa')
                chat_box.click()
                time.sleep(5)
            except:
                pass