from unittest import TestCase
import jsonpickle
import fakeredis
from pyoidc_redis_session_backend import RSAHandler, RedisSessionBackend
from Cryptodome.PublicKey.RSA import RsaKey
from Cryptodome.PublicKey import RSA

class TestSerializer(TestCase):
    def test_encode_works_1(self):
        key = RSA.generate(2048)
        encoded = jsonpickle.encode(key)

    def test_decode_works_1(self):
        key = RSA.generate(2048)
        encoded_key = jsonpickle.encode(key)
        decoded_key = jsonpickle.decode(encoded_key)
        self.assertEqual(key, decoded_key)

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