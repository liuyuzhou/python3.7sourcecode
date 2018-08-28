from server import app

@app.route('/mine', methods=['GET'])
def mine():
    pass

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    pass

@app.route('/chain', methods=['GET'])
def full_chain():
    pass

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    pass

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    pass
