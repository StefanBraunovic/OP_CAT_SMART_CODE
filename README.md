# Bitcoin Smart Contract Script

This Python script constructs a Bitcoin smart contract script using the Bitcoin library. The script involves the concatenation of secret parts from Alice and Bob, hashing the result, and checking it against a predetermined hash.

## Dependencies

- Bitcoin library: Install using `pip install python-bitcoinlib`

## Usage

1. Set the secret parts for Alice and Bob (`secret_part_alice` and `secret_part_bob` variables).
2. Set the predetermined hash value (`predetermined_hash` variable).
3. Run the script.

## Script Construction Steps

1. Convert secret parts to bytes.
2. Concatenate the secret parts using `OP_CAT`.
3. Apply SHA-256 hash using `OP_SHA256`.
4. Push the predetermined hash onto the stack.
5. Compare the two hash values using `OP_EQUALVERIFY`.
6. Perform signature verification using `OP_CHECKSIG`.

## Logging Output

The script will print the constructed smart contract script and its hex representation.

```bash
Smart Contract Script: OP_PUSHDATA1 <alice_hex_bytes> OP_PUSHDATA1 <bob_hex_bytes> OP_CAT OP_SHA256 OP_PUSHDATA1 <predetermined_hash> OP_EQUALVERIFY OP_CHECKSIG
Hex Representation: <hex_representation>
