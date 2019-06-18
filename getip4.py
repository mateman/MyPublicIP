#!/usr/bin/env python3.7
import urllib
def get_my_ip_address():
    whatismyip = 'http://www.whatismyip.com/automation/n09230945.asp'
    return urllib.urlopen(whatismyip).readlines()[0]

def main():
    print(get_my_ip_address())


if __name__ == "__main__":
    main()