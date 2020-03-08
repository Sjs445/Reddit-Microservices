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
    "up_votes": "Number",
    "down_votes": "Number",
    "posted_time": "YYY-MM-DD HH:MM:SS"
]
```