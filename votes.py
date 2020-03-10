import flask_api
from flask import request
from flask_api import status, exceptions
import pugsql

# Initializing Flask API
app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

# Initialize PugSQL
queries = pugsql.module('queries/')
queries.connect(app.config['DATABASE_URL'])

# Initialize database
@app.cli.command('init')
def init_db():
    with app.app_context():
        db = queries._engine.raw_connection()
        with app.open_resource('votes.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Retrieve all votes
@app.route('/api/v1/resources/votes/all', methods=['GET'])
def retrieve_all_votes():
    return list(queries.all_votes())

# Vote up a post
@app.route('/api/v1/resources/votes/upvote/<int:id>', methods=['GET', 'POST'])
def vote_up(id):
    post = queries.post_by_id(id=id)

    if post:
        queries.up_vote(post=id)
        return { 'message': f' {id} upvoted successfully'}, status.HTTP_200_OK
    else:
        return { 'message': f' Error 404 post {id} not found'}, status.HTTP_404_NOT_FOUND

# Vote down a post
@app.route('/api/v1/resources/votes/downvote/<int:id>', methods=['GET', 'POST'])
def vote_down(id):
    post = queries.post_by_id(id=id)

    if post:
        queries.down_vote(post=id)
        return { 'message': f' {id} voted down successfully'}, status.HTTP_200_OK
    else:
        return {'message': f'Error 404 post {id} not found'}, status.HTTP_404_NOT_FOUND

# Retrieve the total number of votes for a post with a specific ID
@app.route('/api/v1/resources/votes/<int:id>', methods=['GET'])
def report_number_of_votes(id):
    view_vote_by_id = queries.vote_by_id(id=id)
    if view_vote_by_id:
        return view_vote_by_id
    else:
        return {'message': f'Error 404 post {id} was not found'}, status.HTTP_404_NOT_FOUND

# List the n top scoring posts to any community
@app.route('/api/v1/resources/votes/top/<int:top_n>', methods=['GET'])
def top_n_score(top_n):
    top = queries.top_n(top_n = top_n)
    if top:
        return list(top)
    else:
        return {'message': f'Error 404 Resource Not Found'}, status.HTTP_404_NOT_FOUND

# Return the list sorted by score
@app.route('/api/v1/resources/votes/highscore', methods=['GET', 'POST'])
def sorted_by_score():
    idList = request.json['id']
    sorted_list = queries.sorted_by_score(idList=idList)
    if sorted_list:
        return list(sorted_list)
    else:
       return { 'message': 'Error 404 Resource Not Found' }, status.HTTP_404_NOT_FOUND
'''
def sorted_by_score(id):
    sorted = queries.sorted_by_score()
    if sorted:
        return list(sorted)
    else:
        return {'message': f'Error 404 Resource Not Found'}, status.HTTP_404_NOT_FOUND
'''