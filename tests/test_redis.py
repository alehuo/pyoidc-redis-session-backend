from unittest import TestCase
import fakeredis
from pyoidc_redis_session_backend import RedisSessionBackend
from Cryptodome.PublicKey import RSA

class TestRedis(TestCase):
    def test_set(self):
        r = fakeredis.FakeStrictRedis()
        backend = RedisSessionBackend(r)
        backend["Hello"] = "World"
        self.assertEqual(backend["Hello"], "World")

    def test_set_rsa_key(self):
        r = fakeredis.FakeStrictRedis()
        key = RSA.generate(2048)
        backend = RedisSessionBackend(r)
        backend["rsakey"] = key
        self.assertEqual(backend["rsakey"], key)

    def test_get_1(self):
        try:
            r = fakeredis.FakeStrictRedis()
            backend = RedisSessionBackend(r)
            backend["test"]
            self.assertTrue(False)   
        except KeyError:
            self.assertTrue(True)