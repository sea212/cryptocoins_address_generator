A small side project I found full of dust on my hard drive. It allows you to generate or supply a private key for which addresses for BTC, BCH, LTC, XRP, ETH and ETC are derived.

WARNING: This programm is not well tested and should not be used on mainnets.
 
1) Install python (version 3.7 if possible)
2) open linux terminal or windows command line
3) swap to directory where this file is located (using the command "cd")
4) Execute command: python -m pip install -r requirements.txt
5) Execute command: python derive_addresses.py


Example output after step 5:

b'\xc5\x90\x98\xd7\xe9\x12l\xde8]\x81\x18\xdfSQR9\xe3$A'
Private key: 0xdc95d473fbff98900437f8670a1580c530c00b8f491e829e31d8f7f6f8083ca2
Public key:
	x: 0x5e8c23bf517eae02f78f7d9d28d9fef5cb403e636f38841065a90aa1fc07f462
	y: 0x986431ac086ffb66487ff90f814d4c8f69bc6bb8412cae854f0f7218767c0fba
BTC / BCH address: b'1K1dLa2PbgSaRZzBHcuW6vZZ2HVz88JXYt'
LTC address: b'DP9ispy2u6LrxaAn2Cu4egj9uREHSimueT'
XRP address: b'rKrdL2pPbgS2RZzBHcuWavZZpHVz33JXYt'
ETH / ETC address: 0x2D9D1989E03CD7Bb88977e244884F08386158C51
