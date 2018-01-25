import requests
import json
import random
import config


def get_proxies():
    r = requests.get(config.PROXY_API_URL)
    ip_ports = json.loads(r.text)
    count = 0
    proxies = None
    while count < config.PROXY_RETRY_COUNT:
        try:
            ip_port = random.choice(ip_ports)
            ip = ip_port[0]
            port = ip_port[1]
            proxies = {
                'http': 'http://{ip}:{port}'.format(ip=ip, port=port),
                'https': 'http://{ip}:{port}'.format(ip=ip, port=port)
            }
            requests.get(config.BASE_URL, proxies=proxies)
            proxies = proxies
            print('get proxy success')
            count = config.PROXY_RETRY_COUNT
        except:
            count = count + 1
            print('try get proxy')
    return proxies
