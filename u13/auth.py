import os

from .extensions import auth
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

users = {}
def get_users():
   global users
   with current_app.open_instance_resource('users.txt') as u:
    for user in u.readlines():
      username, role, passwd = user.decode().strip().split(':', 2)
      users[username] = {
        'role' : role,
        'passwd' : passwd
      }
  
@auth.verify_password
def verify_password(username, passwd):
  get_users()
  if username in users and check_password_hash(users[username]['passwd'],passwd):
    return username

@auth.get_user_roles
def get_user_roles(username):
  get_users()
  if username in users:
    return users[username]['role']
