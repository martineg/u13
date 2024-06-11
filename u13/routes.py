from flask import Blueprint, render_template, request, redirect, jsonify, abort
from .extensions import db, auth
from .models import Link

short = Blueprint('short', __name__, url_prefix='/short')

@short.route('/')
def index():
  return 'u13'

@short.route('/<short_url>')
def redirect_to_url(short_url):
  link = Link.query.filter_by(short_url=short_url).first_or_404()
  link.visits = link.visits + 1
  db.session.commit()
  return redirect(link.original_url)

@short.route('/add_link', methods=['POST'])
def add_link():
  data = request.get_json()
  if 'url' in data:
    link = Link(original_url=data['url'])
    if not Link.query.filter_by(original_url=data['url']).first():
      db.session.add(link)
      db.session.commit()
    return jsonify(url=link.original_url, short_url=link.short_url)
  else:
    return jsonify(error='url is missing'), 400

@short.route('/stats')
@auth.login_required(role='admin')
def stats():
  stats = {l.original_url: l.visits for l in Link.query.all() }
  return jsonify(stats=stats)
