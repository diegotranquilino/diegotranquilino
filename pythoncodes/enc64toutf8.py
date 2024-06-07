#!/usr/bin/env python3
import requests, json
import base64
import sys

string_input = sys.argv[1]
base64_convert = base64.b64encode(string_input).decode("utf-8")
print (base64_convert)
