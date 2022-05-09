import base64
import zlib


def serialize(data: str):
    return base64.b64encode(zlib.compress(data.encode("utf-8"))).decode("utf-8")


def deserialize(data: str):
    return zlib.decompress(base64.b64decode(data.encode("utf-8"))).decode("utf-8")
