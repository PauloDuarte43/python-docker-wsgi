#!/usr/bin/python
from flask import Flask, jsonify

app = Flask(__name__)
app.secret_key = "ausdhas879dyh78asdyh78asdyh8a7shd8a7h*DSA&*H&*HS*DGS87FGSA*FGAS*&fy8(AFSg"


@app.route("/", methods=['GET', 'POST'])
def main():
    return jsonify({'test': 'WORKS'})


if __name__ == "__main__":
    app.run()
