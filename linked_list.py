import hashlib


class Block:
    def __init__(self, index, timestamp, content, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.content = content
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.content).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()


M4BlockChain = []

from datetime import datetime


def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")


M4BlockChain.append(create_genesis_block())


# write a function `next_block` to generate a block
def next_block(last_block):
    index = last_block.index - 1
    content = "this is block " + str(index)
    prev_hash = last_block.hash
    return Block(index, datetime.now(), content, prev_hash)


# append 5 blocks to the blockchain
def app_five(block_list):
    end_block = block_list[0]
    least_index = block_list[0].index
    for block in block_list:
        if block.index < least_index:
            least_index = block.index
        #if block.index == 0:
            end_block = block
    for n in range(5):
        end_block = next_block(end_block)
        #print(end_block.index)
    pass
