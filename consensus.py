import hashlib
import time
import random

#The class name called 'Block' Represents a single block in the blockchain
class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index #The index of the block in the chain
        self.previous_hash = previous_hash #The hash of the previous block in the chain
        self.timestamp = timestamp #The time at which the block was created
        self.data = data #The data stored in the block, which can be transactions or any other information
        self.nonce = nonce #A number used in the mining process
        self.hash = self.calculate_hash() #Assign it into the hash of the current block

    def calculate_hash(self):#Calculates the hash of the block based on its attributes
        data_str = ""
        for item in self.data:
            data_str += str(item)
        return hashlib.sha256(
            f"{self.index}{self.previous_hash}{self.timestamp}{data_str}{self.nonce}".encode()
        ).hexdigest()

class Blockchain: #Manages the chain of blocks
    def __init__(self):
        #A list(chain) of blocks representing the blockchain.
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):  #Creates the genesis block, which is the first block in the chain.
        return Block(0, "0", int(time.time()), ["Genesis Block"])

    def add_block(self, data, proof_of_work=True, difficulty=2): #Adds a new block to the blockchain.
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = int(time.time())
        if proof_of_work:
            new_block = self.proof_of_work_mine_block(index, previous_block.hash, timestamp, data, difficulty)
        else:
            new_block = self.proof_of_stake_mine_block(index, previous_block.hash, timestamp, data)
        self.chain.append(new_block)

        #Mines a new block using Proof of Work consensus mechanism.
    def proof_of_work_mine_block(self, index, previous_hash, timestamp, data, difficulty=2):
        nonce = 0
        prefix = "0" * difficulty
        while True:
            hash_attempt = hashlib.sha256(
                f"{index}{previous_hash}{timestamp}{data}{nonce}".encode()
            ).hexdigest()
            if hash_attempt[:difficulty] == prefix:
                return Block(index, previous_hash, timestamp, data, nonce)
            nonce += 1

            #Mines a new block using Proof of Stake consensus mechanism.
    def proof_of_stake_mine_block(self, index, previous_hash, timestamp, data):
        validators = ["Validator1", "Validator2", "Validator3"]
        chosen_validator = random.choice(validators)
        return Block(index, previous_hash, timestamp, data, chosen_validator)

    #Checks if the blockchain is valid by verifying hashes and previous hashes.
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    #Displays the contents of the blockchain.
    def display_chain(self):
        for block in self.chain:
            print(f"Block #{block.index}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Nonce: {block.nonce}")
            print(f"Hash: {block.hash}\n")


# Create a PoW blockchain and add blocks
pow_blockchain = Blockchain()
pow_blockchain.add_block(["Transaction 1", "Transaction 2"])
pow_blockchain.add_block(["Transaction 3", "Transaction 4"])

# Create a PoS blockchain and add blocks
pos_blockchain = Blockchain()
pos_blockchain.add_block(["Transaction 1", "Transaction 2"], proof_of_work=False)
pos_blockchain.add_block(["Transaction 3", "Transaction 4"], proof_of_work=False)

# Display both blockchains
print("Proof of Work Blockchain:")
pow_blockchain.display_chain()

print("\nProof of Stake Blockchain:")
pos_blockchain.display_chain()

# Check if both blockchains are valid
if pow_blockchain.is_chain_valid():
    print("\nProof of Work Blockchain is valid.")
else:
    print("\nProof of Work Blockchain is not valid.")

if pos_blockchain.is_chain_valid():
    print("Proof of Stake Blockchain is valid.")
else:
    print("Proof of Stake Blockchain is not valid.")
