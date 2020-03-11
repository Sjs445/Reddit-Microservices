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

# Homepage
@app.route('/', methods=['GET'])
def home():
    return '''<h1>The New Reddit</h1>
<p>Welcome to the new reddit for votes...</p>'''

# Retrieve all votes
@app.route('/api/v1/resources/votes/all', methods=['GET'])
def retrieve_all_votes():
    return list(queries.all_votes())

# Vote up a post
@app.route('/api/v1/resources/votes/upvote/<int:id>', methods=['GET', 'PUT'])
def upvote(id):
    if request.method == 'GET':
        return list(queries.all_votes()), status.HTTP_200_OK
    else:
        queries.up_vote(id=id)
        return list(queries.all_votes()), status.HTTP_200_OK

# Vote down a post
@app.route('/api/v1/resources/votes/downvote/<int:id>', methods=['GET', 'PUT'])
def downvote(id):
    if request.method == 'GET':
        return list(queries.all_votes()), status.HTTP_200_OK
    else:
        queries.down_vote(id=id)
        return list(queries.all_votes()), status.HTTP_200_OK

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
def top_scoring_posts(top_n):
    top = queries.top_n(top_n = top_n)
    if top:
        return list(top)
    else:
        return {'message': f'Error 404 Resource Not Found'}, status.HTTP_404_NOT_FOUND

# Return the list sorted by score
@app.route('/api/v1/resources/votes/highscore', methods=['GET', 'POST'])
def sorted_by_score():
    method = request.method

    if method == 'GET':
        return list(queries.sorted_by_score())
    elif method == 'POST':
        return sorted_list(request.data)
    else:
        return {'message': f'Error 400 Bad Request'}, status.HTTP_400_BAD_REQUEST

def sorted_list(post_id):
    sort = queries.sorted_by_score_id(id=post_id[0])
    if sort:
        return list(sort), status.HTTP_200_OK
    else:
        return {'message': f'Error 400 Bad Request'}, status.HTTP_400_BAD_REQUEST

# Helper function from example
def filter_votes(query_parameters):
    id = query_parameters.get('id')
    query = "SELECT * FROM votes WHERE"
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if not (id):
        raise exceptions.NotFound()

    query = query[:-4] + ';'
    results = queries._engine.execute(query, to_filter).fetchall()
    return list(map(dict, results))
