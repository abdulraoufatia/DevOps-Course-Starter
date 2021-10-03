from flask import Flask

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return """
    <html>
<head>
<style>
h1 {text-align: center;}
p {text-align: center;}
</style>
</head>
<body>

<h1>My todo list</h1>
<p>What do you wish to complete mi amigo?</p>

</body>
</html>
    
    """