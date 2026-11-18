
# Blockchain Simulator

This repository contains an educational implementation of a blockchain in Python.

The project demonstrates the fundamental concepts of a block chain:

- Creation of the initial block, called the **Genesis Block**
- Storage of index, timestamp, data, and previous hash
- Generation of SHA-256 hashes for each block
- Chaining of blocks through the `previous_hash` field
- Chain integrity validation
- Detection of tampered data or hashes

## How It Works

The `Block` class represents a block in the blockchain and contains:

- `index`: position of the block in the chain
- `timestamp`: creation date and time
- `data`: stored content or transaction
- `previous_hash`: hash of the previous block
- `hash`: hash calculated from the block's data

The `Blockchain` class creates the genesis block and allows adding new blocks linked to the previous one.

Integrity is verified by the `is_chain_valid()` method, which confirms:

1. Whether the stored hash matches the current content of the block.
2. Whether the `previous_hash` matches the actual hash of the previous block.

## Requirements

- Python 3

No external libraries are required.

## Running the Project

Clone the repository:

```bash
git clone [https://github.com/rique-decoder/blockchain-simulator.git](https://github.com/rique-decoder/blockchain-simulator.git)
cd blockchain-simulator
```

Run the simulator:

```bash
python blockchain.py
```

The example file creates a blockchain named `henriquecoin` and adds five fictional transactions.

## Testing Integrity

The code contains commented-out tests that demonstrate how to tamper with a block's data or previous hash. By uncommenting these sections, you can see how the validation method detects chain tampering.

## License

This project is available under the MIT License.
