#coding=utf-8
import requests
from retrying import retry

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"}

@retry(stop_max_attempt_number=3)
def _parse_url(url):
    response = requests.get(url,headers=headers,timeout=5)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url):
    try:
        html_str = _parse_url(url)
    except Exception as e:
        print(e)
        html_str = None
    return html_str

if __name__ == '__main__':
    pass