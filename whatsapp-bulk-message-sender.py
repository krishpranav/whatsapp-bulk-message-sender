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
        