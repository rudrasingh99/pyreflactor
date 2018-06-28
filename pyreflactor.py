import requests , sys


print("""

  _____       _____       __ _           _
 |  __ \     |  __ \     / _| |         | |
 | |__) _   _| |__) |___| |_| | ___  ___| |_
 |  ___| | | |  _  // _ |  _| |/ _ \/ __| __|
 | |   | |_| | | \ |  __| | | |  __| (__| |_
 |_|    \__, |_|  \_\___|_| |_|\___|\___|\__|
         __/ |
        |___/


""")

site = sys.argv[1]

url = 'https://' + str(site)
url_without_ssl = 'http://'+ str(site)
ssl = 'true'  
try:
    result = requests.get(url)
    url_key = result
except requests.exceptions.SSLError:
    url_http = 'http://' + str(site)
    final_url = 'http://' + site
    result_1 = requests.get(url_http)
    url_key1 = result_1
    ssl = 'fail'
except requests.exceptions.ConnectionError:
    print('Domain seems to be down or Invalid')
    exit()
keyword = '123justakeyword'
if ssl == 'fail':
    keyword_not_ssl = str(final_url) + '/' +str(keyword)
    request_me_no_ssl = requests.get(keyword_not_ssl)
    if keyword not in str(request_me_no_ssl.content):
        print('Our keyword was not reflected in the response.')
if ssl == 'true':
    request_https = str(url) + '/' + str(keyword)
    final_https_request = requests.get(request_https)
    if keyword in str(final_https_request.content):
        print('Yayy!! Keyword Found in the source')
print('Script was run successfully')
exit()
