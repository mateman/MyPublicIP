#!/usr/bin/env python3.7
import requests

def get_my_ip_address():

    return requests.get("http://wtfismyip.com/text").text.strip()

print("\n[+] My Public IP: "+ get_my_ip_address()+"\n")