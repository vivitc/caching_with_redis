import redis


class StepsCache:

    def get_redis_client(self):
        return redis.StrictRedis(host='localhost', port=6379, db=0)

    def add_value_to_set(self, client, set_name, value):
        """"
        For the example we have choose set as main value structure.
        """""
        return client.sadd(set_name, value)

    def is_value_in_set(self, client, set_name, value):
        return client.sismember(set_name, value)
