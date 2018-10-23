from app import app
from flask import render_template
from app.scraper import parse

@app.route('/')
@app.route('/software')
def software():
    data = parse()
    return render_template('mytable.html',rows = data[0],headers=data[1])