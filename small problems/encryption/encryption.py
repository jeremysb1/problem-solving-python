from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    #generate length random bytes
    tb: bytes = token_bytes(length)
    #convert those bytes into a big string and return it
    return int.from_bytes(tb, "big")
