from flask import Flask, jsonify, request
# from passLib.hash import pbkdf2_sha256
import uuid


def signup():
    print(request.form)

    # CREATING THE USER OBJECT
    user = {
        "_id": uuid.uuid4().hex,
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "password": request.form.get('password')
    }

    # ENCRYPTING THE PASSWORD
    # user['password'] = pbkdf2_sha256.encrypt(user['password'])

    return jsonify(user), 200


class User:
    pass
