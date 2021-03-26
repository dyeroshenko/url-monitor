from flask import Flask, render_template, request, url_for, flash, jsonify, Blueprint
from typing import Dict

from components.handler import Handler

home_blueprint = Blueprint('home', __name__)
home_post_blueprint = Blueprint('home_post', __name__)
dashboard_blueprint = Blueprint('dashboard', __name__)

@home_blueprint.route('/', methods=['GET'])
def home() -> 'html':

    return render_template(
                            'view.html',
                            title = 'URL Monitor'
                        )

@home_post_blueprint.route('/post', methods=['POST'])
def home_post() -> Dict[str, str]: 
    url = request.form['url']

    if url:
        handler = Handler(f'{url}/')
        data = handler.checkStatusAndSaveToDB()
    else:
        data = {'error': 'Please provide URL'}
    
    return jsonify(data)

    
@dashboard_blueprint.route('/dashboard', methods=['GET'])
def dashboard() -> 'html':

    handler = Handler()

    table_titles = ('URL', 'Checked', 'Host name','IP Address','Round Trip Time','Response code')

    data = handler.getRecordsFromDB()

    return render_template(
                            'dashboard.html',
                            title = 'Dashboard',
                            table_titles = table_titles,
                            data = data,
                        )