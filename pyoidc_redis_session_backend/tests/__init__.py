from unittest import TestCase
import jsonpickle
from pyoidc_redis_session_backend import RSAHandler
from Crypto.PublicKey.RSA import RsaKey
from Crypto.PublicKey import RSA

class TestSerializer(TestCase):
    def test_encode_works(self):
        jsonpickle.register(RsaKey, RSAHandler)
        key = RSA.generate(2048)
        encoded = jsonpickle.encode(key)
        self.assertEqual(True, True)

    def test_decode_works(self):
        jsonpickle.register(RsaKey, RSAHandler)
        key = RSA.generate(2048)
        encoded_key = jsonpickle.encode(key)
        decoded_key = jsonpickle.decode(encoded_key)
        self.assertEqual(key, decoded_key)