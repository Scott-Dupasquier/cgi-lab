#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
import os

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")

# Question 1
# print(os.environ)

# Question 2
# print(os.environ["QUERY_STRING"])

# Question 3
# print(os.environ["HTTP_USER_AGENT"])