class BlockChain:
    def __init__(self):
        # 储存交易
        self.current_transactions = []
        # 储存区块链
        self.chain = []
        # 储存节点
        self.nodes = set()
        # 创建创世块
        self.new_block(previous_hash='1', proof=100)

    def register_node(self, address):
        pass

    def valid_chain(self, chain):
        pass

    def resolve_conflicts(self):
        pass

    def new_block(self, proof, previous_hash):
        pass

    def new_transaction(self, sender, recipient, amount):
        pass

    @property
    def last_block(self):
        pass

    @staticmethod
    def hash(block):
        pass

    def proof_of_work(self, last_proof):
        pass

    @staticmethod
    def valid_proof(last_proof, proof):
        pass
