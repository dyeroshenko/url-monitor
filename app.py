from flask import Flask, render_template, request, url_for, flash, jsonify, Blueprint
from typing import Dict

from components.handler import Handler

home_blueprint = Blueprint('home', __name__)
home_post_blueprint = Blueprint('home_post', __name__)
dashboard_blueprint = Blueprint('dashboard', __name__)

@home_blueprint.route('/', methods=['GET'])
def home() -> 'html':
    ''' Renders main page HTML '''

    return render_template(
                            'view.html',
                            title = 'URL Monitor'
                        )

@home_post_blueprint.route('/post', methods=['POST'])
def home_post() -> Dict[str, str]: 
    '''
    Takes [URL] parameter posted by home() using JS fetch: 
    1. If no url param is provided, returns an error
    2. Else adds trailling '/' and passes [url]] to Handler()
    '''

    url = request.form['url']

    if url:
        handler = Handler(f'{url}/')
        data = handler.checkStatusAndSaveToDB()
    else:
        data = {'error': 'Please provide URL'}
    
    return jsonify(data)

    
@dashboard_blueprint.route('/dashboard', methods=['GET'])
def dashboard() -> 'html':
    ''' Renders HTML view with a dasboard of processed URLs along with attributes '''
    
    handler = Handler()

    table_titles = ('URL', 'Checked', 'Host name','IP Address','Round Trip Time','Response code')

    data = handler.getRecordsFromDB()

    return render_template(
                            'dashboard.html',
                            title = 'Dashboard',
                            table_titles = table_titles,
                            data = data,
                        )