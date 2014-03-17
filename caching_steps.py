import redis

class StepsCache:
    def init_cache(self):
        """"
        For the example we have choose set as main value structure.
        """""
        client = self.get_redis_client()
        set_name = 'process_steps'
        self.add_value_to_set(client, set_name, 'step 1 description')
        self.add_value_to_set(client, set_name, 'step 2 description')

    def get_redis_client(self):
        return redis.StrictRedis(host='localhost', port=6379, db=0)

    def add_value_to_set(self, client, set_name, value):
        return client.sadd(set_name, value)

    def is_value_in_set(self, client, set_name, value):
        return client.sismember(set_name, value)


StepsCache().init_cache()