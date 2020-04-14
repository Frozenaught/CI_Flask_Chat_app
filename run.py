from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_messages(username, message):
    """Add messages to the messages list"""
    messages.append(f"{username}: {message}")


def get_all_messages():
    """get all messages and separate using the `br>`"""
    return '<br>'.join(messages)


@app.route('/')
def index():
    """Main page with instructions"""
    return 'To send a message use /USERNAME/MESSAGE'


@app.route('/<username>')
def username(username):
    """Display chat messages"""
    return f"<h1>Welcome, {username}</h1> {get_all_messages()}"


@app.route("/<username>/<message>")
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect(f"/{username}")


app.run()
# app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
