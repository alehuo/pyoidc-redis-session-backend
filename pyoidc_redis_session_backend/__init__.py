import redis
import jsonpickle
import base64
import jsonpickle
from jsonpickle.handlers import BaseHandler
from oic.utils.session_backend import AuthnEvent, SessionBackend
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from typing import cast
from Crypto.PublicKey.RSA import RsaKey, import_key

class RSAHandler(BaseHandler):
    def flatten(self, obj: RsaKey, data): 
        data["rsa_key"] = base64.b64encode(obj.export_key()).decode("utf-8")
        return data

    def restore(self, obj):
        return import_key(base64.b64decode(obj["rsa_key"]))

jsonpickle.register(RsaKey, RSAHandler)

class RedisSessionBackend(SessionBackend):
    """
    Redis session backend
    """

    def __init__(self, redis_instance: redis.Redis, **args):
        """Create the storage."""
        self.r = redis_instance

    def __setitem__(self, key: str, value: Dict[str, Union[str, bool]]) -> None:
        """Store the session info in the storage."""
        self.r.set(key, jsonpickle.encode(value))

    def __getitem__(self, key: str) -> Dict[str, Union[str, bool]]:
        """Retrieve session information based on session id."""
        data = self.r.get(key)
        return jsonpickle.decode(data.decode("utf-8"))

    def __delitem__(self, key: str) -> None:
        """Delete the session info."""
        self.r.delete(key)

    def __contains__(self, key: str) -> bool:
        return key in self.r.keys()

    def get_by_sub(self, sub: str) -> List[str]:
        """Return session ids based on sub."""
        return [
            key for key in self.r.keys() if jsonpickle.loads(self.r.get(key).decode("utf-8")).get("sub") == sub
        ]

    def get_by_uid(self, uid: str) -> List[str]:
        """Return session ids based on uid."""
        return [
            key
            for key in self.r.keys()
            if AuthnEvent.from_json(self.r.get(key).decode("utf-8"))["authn_event"].uid == uid
        ]

    def get(self, attr: str, val: str) -> List[str]:
        """Return session ids based on attribute name and value."""
        return [
            key for key in self.r.keys() if jsonpickle.loads(self.r.get(key).decode("utf-8")).get(attr) == val
        ]
