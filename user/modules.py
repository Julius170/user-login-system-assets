from flask import Flask, jsonify

# request
# from passLib.hash import pbkdf2_sha256
# import uuid


class User:

    def signup():
        user = {
            "_id": "",
            "name": "",
            "email": ""
        }
        return jsonify(user), 200

