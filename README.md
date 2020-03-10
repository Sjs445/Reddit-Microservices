# CPSC 449 Reddit-Microservices

## Shane Spangenberg, Brendon Linthurst, Collin Campbell

#### Initialize the database before calling ```flask run``` with ```flask init```

### Posts in Json Format

```json
[
    "id": "Number",
    "title": "Post Title",
    "body": "Body of Post",
    "user": "username",
    "sub": "sub community",
    "url": "www.example.com",
    "posted_time": "YYY-MM-DD HH:MM:SS"
]
```

### Votes in Json Format

```json
[
    "id": "Number",
    "up_votes": "Number",
    "down_votes": "Number"
]
```
## Homepage

```/``` Method = GET

Returns the homepage of the Reddit Microservices.


## Post Routes


### Get all posts

```/api/v1/resources/posts/all``` Method = GET

Returns all posts in json format.

### Get post by ID and delete post by ID

```/api/v1/resources/posts/<int:id>``` Methods = GET && DELETE

Returns the specified post by ID in json format.

#### To test delete run the deletepost.sh as follows

First make the shell file executable by running ```chmod +x deletepost.sh```

Then run the shell command like ```./deletepost.sh <:id>``` where <:id> is the id of the post you want to delete.

Note that when we delete a post we also delete the same row from the votes table that references the same ID.

### Create a new post

```/api/v1/resources/posts``` Method = POST

#### To test create a new post run the newpost.sh as follows

First make the shell file executable by running```chmod +x newpost.sh```

Then run the shell command like```./newpost.sh```

After the post is created it should return```201 Created ```with the ID of the post that was created. If there is already a post with that same ID it will return```409 Conflict```. Note that when we create a post we insert into the votes table referencing the same ID as posts and initialize the votes to 0.

### Get n most recent posts from all communities

```/api/v1/resources/posts/recent/<int:number_of_posts>``` Method = GET

Simply returns the most recent posts limited to size n from every community.

### Get n most recent posts from specific community

```/api/v1/resources/posts/recent/<string:sub>/<int:number_of_posts>``` Method = GET

Simply returns the most recent posts limited to size n from a specified community.
