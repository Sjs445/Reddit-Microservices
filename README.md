# CPSC 449 Reddit-Microservices

## Shane Spangenberg, Brendon Linthurst, Collin Campbell

#### To run the server please be sure to run the following scripts in the terminal:
    ```pip3 install pugsql
    pip3 install flask_api
    pip3 install python-dotenv
    sudo gem install foreman```

#### To run the server please run the following command in terminal:
    ``sh foreman.sh```


#### Initialize the database before calling ```flask run``` with ```flask init```

### Posts in Json Format

```json
{
    "id": "Number",
    "title": "Post Title",
    "body": "Body of Post",
    "user": "username",
    "sub": "sub community",
    "url": "www.example.com",
    "up_votes": "Number",
    "down_votes": "Number",
    "posted_time": "YYY-MM-DD HH:MM:SS"
}
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


### Create a new post

```/api/v1/resources/posts``` Method = POST

#### To test create a new post run the newpost.sh as follows

First make the shell file executable by running```chmod +x newpost.sh```

Then run the shell command like```./newpost.sh```

After the post is created it should return```201 Created ```with the ID of the post that was created. If there is already a post with that same ID it will return```409 Conflict```. 

### Get n most recent posts from all communities

```/api/v1/resources/posts/recent/<int:number_of_posts>``` Method = GET

Simply returns the most recent posts limited to size n from every community.

### Get n most recent posts from specific community

```/api/v1/resources/posts/recent/<string:sub>/<int:number_of_posts>``` Method = GET

Simply returns the most recent posts limited to size n from a specified community.

### Retrieve all posts with votes

```/api/v1/resources/votes/all``` Method = GET

Retrieves all posts that have votes

### Vote up a post

```/api/v1/resources/votes/upvote/<int:id>```Method = GET, PUT

curl -X PUT http://localhost:5000/api/v1/resources/votes/upvote/1

Increases the score of a post

### Vote down a post

```/api/v1/resources/votes/upvote/<int:id>``` Method = GET, PUT

curl -X PUT http://localhost:5000/api/v1/resources/votes/downvote/2

Reduces the score of a post

### Retrieve the total number of votes for a post with a specific ID

```/api/v1/resources/votes/<int:d>``` Method = GET

### List the n top scoring posts to any community

```/api/v1/resources/votes/top/<int:top_n>``` Method = GET

### Return the list sorted by score Method = GET, POST

```/api/v1/resources/votes/highscore Method = GET, POST


