# Flask modules
import flask_api
from flask import request
from flask_api import status, exceptions
import pugsql

# Flask intance
app = flask_api.FlaskAPI(__name__)
app.config.from_envvar('APP_CONFIG')

# Queries and database paths
queries = pugsql.module('queries/')
queries.connect(app.config['DATABASE_URL'])

# Initialize the database by running 'flask init'
@app.cli.command('init')
def init_db():
    with app.app_context():
        db = queries._engine.raw_connection()
        with app.open_resource('posts.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Homepage
@app.route('/', methods=['GET'])
def home():
    return '''<h1>The New Reddit</h1>
<p>Welcome to the new reddit...</p>'''

# Get all posts
@app.route('/api/v1/resources/posts/all', methods=['GET'])
def all_posts():
    all_posts = queries.all_posts()
    
    return list(all_posts)

# Get post by id and delete post by id
@app.route('/api/v1/resources/posts/<int:id>', methods=['GET', 'DELETE'])
def post(id):
    if request.method == 'GET':
        post = queries.post_by_id(id=id)
        return post
    elif request.method == 'DELETE':
        queries.delete_post_by_id(id=id)
        return {'message': f'Post deleted successfully'}, status.HTTP_200_OK 
    else:
        raise exceptions.NotFound()

# GET and POST 
@app.route('/api/v1/resources/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
       # return filter_posts(request.args)
       return
    elif request.method == 'POST':
        return create_post(request.data)

# create a post
def create_post(post):
    posted_fields = {*post.keys()}
    required_fields = {'id', 'title', 'body', 'sub', 'up_votes', 'down_votes', 'posted_time'}

    if not required_fields <= posted_fields:
        message = f'Missing fields: {required_fields - posted_fields}'
        raise exceptions.ParseError(message)
    try:
        post['id'] = queries.create_post(**post)
    except Exception as e:
        return { 'error': str(e) }, status.HTTP_409_CONFLICT

    return post, status.HTTP_201_CREATED, {
        'Location': f'/api/v1/resources/posts/{post["id"]}'
    }