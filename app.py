from flask import Flask
import platform
import socket

app = Flask(__name__)

@app.route("/")
def system_info():
    return {
        "OS": platform.system(),
        "Version": platform.version(),
        "Hostname": socket.gethostname()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

