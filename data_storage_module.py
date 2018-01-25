from pymongo import MongoClient
import config


class DataStorage:
    def __init__(self):
        client = MongoClient(config.MONGODB_HOST, config.MONGODB_PORT)
        db = client[config.MONGODB_DB_NAME]
        db.authenticate(config.MONGODB_NAME,config.MONGODB_PWD)
        self.spider_data = db[config.MONGODB_COL_NAME]

    def save(self, data):
        if data:
            check_data = self.spider_data.find_one({'url': data.get('url')})
            if not check_data:
                print('insert data')
                print(data)
                self.spider_data.insert(data)
