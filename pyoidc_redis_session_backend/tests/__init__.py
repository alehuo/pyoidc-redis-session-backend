from unittest import TestCase
import jsonpickle
from pyoidc_redis_session_backend import RSAHandler
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