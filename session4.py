import hashlib
import time

class Block:
    def first(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calc_hash(self):
        data_str = ''.join(str(transaction) for transaction in self.data)
        block_content = str(self.index) + self.previous_hash + str(self.timestamp) + data_str + str(self.nonce)
        return hashlib.sha256(block_content.encode()).hexdigest()

    def second(self):
        return f"Block #{self.index} - Hash: {self.hash}"

    def mine_block(block, difficulty):
        while block.hash[:difficulty] != '0' * difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block.nonce, block.hash
    
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), ["Genesis Block"])
        self.chain.append(genesis_block)

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.index = len(self.chain)
        new_block.timestamp = time.time()
        nonce, new_block.hash = self.mine_block(new_block, 2)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(block)

# Create a blockchain object
blockchain = Blockchain()

# Add some transactions
transactions = ["Transaction 1", "Transaction 2", "Transaction 3"]

# Mine and add blocks
for transaction in transactions:
    new_block = Block(0, "", time.time(), [transaction])
    blockchain.add_block(new_block)

# Verify integrity
print("Is blockchain valid?", blockchain.is_chain_valid())

# Display blockchain
blockchain.display_chain()