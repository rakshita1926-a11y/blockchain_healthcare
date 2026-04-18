from flask import Flask, render_template, request, redirect, session
import hashlib, datetime, json, os

app = Flask(__name__)
app.secret_key = "secret123"

# -------- FILE PATH FIX (IMPORTANT FOR RENDER) -------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data.json")
USER_FILE = os.path.join(BASE_DIR, "users.json")

# -------- USER FUNCTIONS -------- #
def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# -------- BLOCK -------- #
class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + self.timestamp + str(self.data) + self.prev_hash
        return hashlib.sha256(value.encode()).hexdigest()

# -------- BLOCKCHAIN -------- #
class Blockchain:
    def __init__(self):
        self.chain = []
        self.load_chain()

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        if not self.chain:
            self.chain.append(self.create_genesis_block())

        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)
        self.save_chain()

    def save_chain(self):
        with open(DATA_FILE, "w") as f:
            json.dump([block.__dict__ for block in self.chain], f)

    def load_chain(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                for b in data:
                    block = Block(b['index'], b['data'], b['prev_hash'])
                    block.timestamp = b['timestamp']
                    block.hash = b['hash']
                    self.chain.append(block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False

            if current.prev_hash != prev.hash:
                return False

        return True

blockchain = Blockchain()

# -------- HOME / LOGIN -------- #
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')

        users = load_users()

        if user in users and users[user] == pwd:
            session['user'] = user
            return redirect('/dashboard')
        else:
            return render_template('login.html', msg="Invalid Login")

    return render_template('login.html')

# -------- SIGNUP -------- #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')

        users = load_users()

        if user in users:
            return render_template('signup.html', msg="User already exists")

        users[user] = pwd
        save_users(users)

        return redirect('/')

    return render_template('signup.html')

# -------- DASHBOARD -------- #
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    return render_template('dashboard.html',
                           user=session['user'],
                           blocks=len(blockchain.chain),
                           records=max(0, len(blockchain.chain)-1),
                           valid=blockchain.is_chain_valid())

# -------- ADD RECORD -------- #
@app.route('/add', methods=['POST'])
def add():
    if 'user' not in session:
        return redirect('/')

    data = {
        "PatientID": request.form.get('pid'),
        "Diagnosis": request.form.get('diagnosis'),
        "Treatment": request.form.get('treatment')
    }

    blockchain.add_block(data)
    return redirect('/dashboard')

# -------- VIEW -------- #
@app.route('/view')
def view():
    if 'user' not in session:
        return redirect('/')

    return render_template('view.html', chain=blockchain.chain)

# -------- SEARCH -------- #
@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'user' not in session:
        return redirect('/')

    result = []

    if request.method == 'POST':
        pid = request.form.get('pid')

        for block in blockchain.chain:
            if isinstance(block.data, dict) and block.data.get("PatientID") == pid:
                result.append(block)

    return render_template('search.html', result=result)

# -------- DELETE -------- #
@app.route('/delete/<int:index>')
def delete(index):
    if 'user' not in session:
        return redirect('/')

    if index > 0 and index < len(blockchain.chain):
        blockchain.chain.pop(index)
        blockchain.save_chain()

    return redirect('/view')

# -------- EDIT -------- #
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if 'user' not in session:
        return redirect('/')

    block = blockchain.chain[index]

    if request.method == 'POST':
        block.data = {
            "PatientID": request.form.get('pid'),
            "Diagnosis": request.form.get('diagnosis'),
            "Treatment": request.form.get('treatment')
        }

        block.hash = block.calculate_hash()
        blockchain.save_chain()

        return redirect('/view')

    return render_template('edit.html', block=block)

# -------- LOGOUT -------- #
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# -------- HEALTH CHECK (FOR RENDER) -------- #
@app.route('/ping')
def ping():
    return "alive"

# -------- RUN -------- #
if __name__ == '__main__':
    app.run()