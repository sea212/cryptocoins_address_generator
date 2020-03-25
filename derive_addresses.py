import base58
import basicecc
from os import urandom
from hashlib import new as newh
from sha3 import keccak_256

alphabet_btc = b'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
alphabet_bch = alphabet_btc
alphabet_ltc = alphabet_btc
alphabet_xrp = b'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz'

prefix_btc = b'\x00'
prefix_bch = prefix_btc
prefix_xrp = prefix_btc
prefix_ltc = b'\x1e'

class AddressManager(object):
    # privkey has to be hex formatted
    def __init__(self, privkey=""):
        if privkey == "":
            self.privkey = int.from_bytes(urandom(32), "big")
        else:
            self.privkey = int(privkey, 16)

        self.pubkey = basicecc.fast_multiply(basicecc.getG(), self.privkey)

    def getCompressedKey(self):
        prefix = b'\x02'

        if (self.pubkey[1] & 1):
            prefix = b'\x03'

        return prefix + self.pubkey[0].to_bytes(32, "big")

    def getUncompressedKey(self):
        return b'\x04' + self.pubkey[0].to_bytes(32, "big") + \
               self.pubkey[1].to_bytes(32, "big")

    def makeEthChecksum(self, address):
        khash = keccak_256(address.lower().encode("ascii")).digest()
        res = ""

        for idx, item in enumerate(address):
            khidx = int(idx/2)

            if (khash[khidx] & 0x0F if idx & 1 else (khash[khidx] & 0xF0) >> 4) > 7:
                res += item.upper()
            else:
                res += item.lower()

        return res      

    def getBtcFamilyPkh(self, compressed=True):
        sha256 = newh("sha256")
        ripemd160 = newh("RIPEMD160")
        sha256.update(self.getCompressedKey() if compressed else self.getUncompressedKey())
        ripemd160.update(sha256.digest())
        return ripemd160.digest()
        
    # BTC and BHC address
    def getBtcAddress(self, compressed=True):
        base58.alphabet = alphabet_btc
        print(self.getBtcFamilyPkh(compressed))
        return base58.b58encode_check(prefix_btc + self.getBtcFamilyPkh(compressed))

    def getLtcAddress(self, compressed=True):
        base58.alphabet = alphabet_ltc
        return base58.b58encode_check(prefix_ltc + self.getBtcFamilyPkh(compressed))

    def getXrpAddress(self):
        base58.alphabet = alphabet_xrp
        return base58.b58encode_check(prefix_xrp + self.getBtcFamilyPkh(True))

    # ETH and ETC address
    def getEthAddress(self):
        tohash = int(hex(self.pubkey[0]) + hex(self.pubkey[1])[2:], 16).to_bytes(64, "big")
        pubhash = keccak_256(tohash).digest()
        nocsadr = hex(int.from_bytes(pubhash[-20:], "big"))
        
        return "0x" + self.makeEthChecksum((40 - len(nocsadr[2:])) * '0' + nocsadr[2:])

    def __repr__(self):
        return "AddressManager(privkey={})".format(self.privkey)

    def __str__(self):
        return "Private key: {}\nPublic key:\n\tx: {}\n\ty: {}\n"\
               "BTC / BCH address: {}\nLTC address: {}\nXRP address: {}\n"\
               "ETH / ETC address: {}".format(hex(self.privkey), hex(self.pubkey[0]), 
               hex(self.pubkey[1]), self.getBtcAddress(), self.getLtcAddress(), 
               self.getXrpAddress(), self.getEthAddress())

def main():
    print(AddressManager())

if __name__ == "__main__":
    main()
