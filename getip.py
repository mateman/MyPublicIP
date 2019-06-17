import requests

def detect_public_ip():
    try:
        # Use a get request for api.duckduckgo.com
        raw = requests.get('https://api.duckduckgo.com/?q=ip&format=json')
        # load the request as json, look for Answer.
        # split on spaces, find the 5th index ( as it starts at 0 ), which is the IP address
        answer = raw.json()["Answer"].split()[4]
    # if there are any connection issues, error out
    except Exception as e:
        return 'Error: {0}'.format(e)
    # otherwise, return answer
    else:
        return answer

public_ip = detect_public_ip()
print(public_ip)