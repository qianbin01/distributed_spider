import redis
import config


class RedisUrlManager:
    def __init__(self):
        self.redis_client = redis.Redis(config.REDIS_HOST, config.REDIS_PORT)
        self.redis_client.sadd('toDoUrls', config.ENTER_URL)

    def put_url_to_do_set(self, url):
        if not self.redis_client.sismember('OverUrls', url):
            self.redis_client.sadd('toDoUrls', url)

    def put_url_to_over_set(self, url):
        self.redis_client.sadd('OverUrls', url)

    def get_url_from_do_set(self):
        url = self.redis_client.spop('toDoUrls')
        return url

    def to_do_set_is_empty(self):
        return self.redis_client.scard('toDoUrls') == 0

    def get_to_do_set_size(self):
        return self.redis_client.scard('toDoUrls')
