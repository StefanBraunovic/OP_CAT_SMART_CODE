from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging
from decimal import Decimal
from bitcoin.core.script import CScript, OP_PUSHDATA1, OP_CAT, OP_SHA256, OP_EQUALVERIFY, OP_CHECKSIG

# Configure the Bitcoin logger
logging.basicConfig()
logger = logging.getLogger("BitcoinRPC")
logger.setLevel(logging.DEBUG)

rpc_user = "r1"
rpc_pass = "r123"
rpc_host = "127.0.0.1"
rpc_port = 8333  # Corrected RPC port for regtest

# Connect to the Regtest server
rpc_client = AuthServiceProxy(f"http://{rpc_user}:{rpc_pass}@{rpc_host}:{rpc_port}", timeout=300)

# Alice's secret part
secret_part_alice = "AliceSecret"

# Bob's secret part
secret_part_bob = "BobSecret"

# Predetermined hash value (replace with an actual hash)
predetermined_hash = "d571eea7817f002a80c48c83720cf46ed7f8e3de4242f65c9a780b1cc69e0da4"

# Convert the secrets to bytes
alice_bytes = secret_part_alice.encode('utf-8')
bob_bytes = secret_part_bob.encode('utf-8')

# Concatenate the secrets using OP_CAT
script = [
    OP_PUSHDATA1, len(alice_bytes), alice_bytes,
    OP_PUSHDATA1, len(bob_bytes), bob_bytes,
    OP_CAT,
    OP_SHA256,
    OP_PUSHDATA1, len(predetermined_hash)//2, bytes.fromhex(predetermined_hash),
    OP_EQUALVERIFY,
    OP_CHECKSIG
]

# Convert the script to hex
script_hex = CScript(script).hex()

# Print the script and its hex representation
logger.debug("Smart Contract Script: %s", " ".join(map(str, script)))
logger.debug("Hex Representation: %s", script_hex)
