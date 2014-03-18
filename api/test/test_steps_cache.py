from unittest import TestCase
from mock import patch
from mockredis import mock_strict_redis_client
from src.caching_steps import StepsCache


class TestStepsCache(TestCase):

    @patch('redis.StrictRedis', mock_strict_redis_client)
    def test_init_cache(self):
        cache = StepsCache()
        client = cache.get_redis_client()
        key_name = "key set name"
        value = "first value"
        cache.add_value_to_set(client, key_name, value)
        self.assertEquals(client.sismember(key_name, value), 1)

