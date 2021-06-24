import requests
import json

base_rest_url = 'http(s)://your-domain.com/MicroStrategyLibrary'
event_id = 'XXXXXXXXXX'
auth_data = {
    'loginMode': 1,
    'username': 'user',
    'password': 'password'
}


def get_auth_items(url, data):
    response = requests.post(url, data=data)
    auth_token = response.headers['X-MSTR-AuthToken']
    cookies = response.cookies
    return (auth_token, cookies)


def main():
    auth_url = '{0}/api/auth/login'.format(base_rest_url)
    auth_token, cookies = get_auth_items(auth_url, auth_data)
    trigger_event_url = '{0}/api/events/{1}/trigger'.format(
        base_rest_url, event_id)
    headers = {
        'X-MSTR-AuthToken': auth_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    requests.post(trigger_event_url, headers=headers, cookies=cookies)


if __name__ == '__main__':
    main()
