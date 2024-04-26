import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        data_str = ''.join(str(transaction) for transaction in self.data)
        block_content = str(self.index) + self.previous_hash + str(self.timestamp) + data_str + str(self.nonce)
        return hashlib.sha256(block_content.encode()).hexdigest()
    
    def __str__(self):
        return f"Block #{self.index} - Hash: {self.hash}"

class Blockchain:
    def __init__(self):
        self.chain = [self.create_starting_block()]

    def create_starting_block(self):
        return Block(0, "0" * 64, int(time.time()), ["Starting Block"])

    def add_block(self, data):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        new_block = Block(index, previous_block.hash, timestamp, data)
        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block, difficulty=2):
        while block.hash[:difficulty] != '0' * difficulty:
            block.nonce += 1
            block.hash = block.calc_hash()
        print(f"Block mined: {block.hash}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calc_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(block)
            print("Previous Hash:", block.previous_hash)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Nonce:", block.nonce)
            print("Hash:", block.hash)
            print()

# Create a blockchain and add blocks to it
blockchain = Blockchain()
blockchain.add_block(["Transaction 1", "Transaction 2"])
blockchain.add_block(["Transaction 3", "Transaction 4"])

# Display the blockchain
blockchain.display_chain()
