import redis


class StepsCache:

    def get_redis_client(self):
        return redis.StrictRedis(host='localhost', port=6379, db=0)

    def is_value_in_set(self, client, set_name, value):
        return client.sismember(set_name, value)

    def add_script_data(self, client):
        """"
        For the example we have choose set as main value structure.
        Set allows to store unique keys
        """""
        data = self.get_steps_information()
        for key in data.iterkeys():
            for value in data[key]:
                client.sadd(key, value)

    def get_steps_information(self):
        return {}
