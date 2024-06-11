from datetime import datetime
from hashlib import md5
from .extensions import db

class Link(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  original_url = db.Column(db.String(1024))
  short_url = db.Column(db.String(64), unique=True)
  visits = db.Column(db.Integer, default=0)
  date_created = db.Column(db.DateTime, default=datetime.now())

  def __init__(self, original_url, **kwargs):
    self.original_url = original_url
    self.short_url = self.generate_short_link()

  def __repr__(self):
    return f'<Link {self.short_url}'

  def generate_short_link(self):
    short_url = md5(self.original_url.encode())
    return short_url.hexdigest()[:7]
