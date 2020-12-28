import requests

CURRENT_REFRESH_TOKEN = 'Atnr|E...'

cookies = {
    'at-main': CURRENT_ACCESS_TOKEN,
}

headers = {
    'User-Agent': 'AmazonWebView/Amazon Alexa/2.2.223830.0/iOS/11.4.1/iPhone',
    'Accept-Language': 'en-US',
    'Accept-Charset': 'utf-8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*'
}

data = {
    'di.os.name': 'iOS',
    'app_version': '2.2.223830.0',
    'domain': '.' + 'api.amazon.com',
    'source_token': CURRENT_REFRESH_TOKEN,    
    'requested_token_type': 'auth_cookies',
    'source_token_type': 'refresh_token',
    'di.hw.version': 'iPhone',
    'di.sdk.version': '6.10.0',
    'cookies': {},
    'app_name': 'Amazon Alexa',
    'di.os.version': '11.4.1'
}

# using the refresh token get the cookies needed for making calls to alexa.amazon.com
response = requests.post('https://api.amazon.com/ap/exchangetoken/cookies', headers=headers, cookies=cookies, data=data)


# Extract the cookies from the response
raw_cookies = response.json()['response']['tokens']['cookies']['.amazon.com']

# Create a new cookies object to be used with requsts.
cookies = {}
for cookie in raw_cookies:
    cookies[cookie['Name']] = cookie['Value']


# generic headers for api call to alexa.amazon.com
headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': 'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 PitanguiBridge/2.2.389238.0-[HARDWARE=iPhone12_3][SOFTWARE=14.3]',
    'Accept-Language': 'en-US,en-US;q=1.0',
}

# data for making an api call to turn on my bedroom lights
data = '{"controlRequests":[{"entityId":"0d1b8083-8609-425c-8f23-0f8c1cb95a41","entityType":"APPLIANCE","parameters":{"action":"turnOn"}}]}'

# make the call and print the response.
response = requests.put('https://alexa.amazon.com/api/phoenix/state', headers=headers, cookies=cookies, data=data)
print(response.text)
