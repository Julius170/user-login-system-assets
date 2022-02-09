from flask import Flask, jsonify, request, session, redirect
from passlib.hash import bcrypt #pdkdf2_sha256
from app import db
import uuid




# CREATING THE USER OBJECT
class User:

    def start_session(self, user):
        del user['password']
        session["Logged_in"] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        print(request.form)

        # THE USER OBJECT
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # ENCRYPTING THE PASSWORD
        # user['password'] = pdkdf2_sha256.encrypt(user['password'])
        # hash =  bcrypt.hash["password"]
        user["password"] = bcrypt.encrypt(user["password"])


        # CHECK FOR EXISTING EMAIL ADDRESS
        if db.user.find_one({"email": user['email'] }):
            return jsonify({"error": "Email address already in use"}), 400

        # OTHERWISE INSERT THE USER INTO THE DATABASE
        if db.users.insert_one(user):
            return self.start_session(user), 200

        # ELSE PASS ON A GENERIC ERROR (SOMETHING WENT WRONG)
        return jsonify({"error": "Signup failed"}), 400


    def signout(self):
        session.clear()
        return redirect('/')