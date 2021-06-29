#!/usr/bin/env python3

# imports
from selenium import webdriver
import csv
import time

messages = input(str("What's the message you want to send => "))
files = input(str("File of contacts => "))

users = []