from unittest.mock import Mock, patch, MagicMock

from data_entry_app.utils import RedisCache


@patch("redis.StrictRedis")
def test_01_redis(self, mock_redis):
    # initialising the cache with test values
    redis_cache = {"foo": "bar", "foobar": {"Foo": "Bar"}}

    mock_redis_obj = RedisCache(redis_cache)

    mock_redis_method = MagicMock()
    mock_redis_method.hget = Mock(side_effect=mock_redis_obj.get)
    mock_redis_method.set = Mock(side_effect=mock_redis_obj.set)

    mock_redis.return_value = mock_redis_method
