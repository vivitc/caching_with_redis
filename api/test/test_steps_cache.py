from unittest import TestCase
from mock import patch, Mock
from mockredis import mock_strict_redis_client
from src.caching_steps import StepsCache


class TestStepsCache(TestCase):

    @patch('redis.StrictRedis', mock_strict_redis_client)
    def test_that_data_from_api_is_stored(self):
        cache = StepsCache()
        key_name = "script 1"
        first_value = "step 1 1"
        second_value = "step 1 2"
        data = {key_name: [first_value, second_value]}
        cache.get_steps_information = Mock(return_value=data)

        client = cache.get_redis_client()
        cache.add_script_data(client)

        self.assertTrue(client.sismember(key_name, first_value))
        self.assertTrue(client.sismember(key_name, second_value))
