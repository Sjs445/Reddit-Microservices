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

# POST request for a new post
@app.route('/api/v1/resources/posts', methods=['POST'])
def posts():
    if request.method == 'POST':
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

# Get n most recent posts from all communities
@app.route('/api/v1/resources/posts/recent/<int:number_of_posts>', methods=['GET'])
def recent_posts(number_of_posts):
    get_recent_posts_all = queries.get_recent_posts_all(number_of_posts=number_of_posts)
    return list(get_recent_posts_all)

# Get n most recent posts from specific community
@app.route('/api/v1/resources/posts/recent/<string:sub>/<int:number_of_posts>', methods=['GET'])
def recent_posts_sub(sub, number_of_posts):
    get_recent_posts_sub = queries.get_recent_posts_sub(sub=sub, number_of_posts=number_of_posts)
    return list(get_recent_posts_sub)