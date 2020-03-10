-- $ sqlite3 posts.db < posts.sql

BEGIN TRANSACTION;
DROP TABLE IF EXISTS posts;
CREATE TABLE posts (
    id INTEGER primary key,
    title VARCHAR,
    body VARCHAR,
    user VARCHAR,       
    sub VARCHAR,
    url VARCHAR,
    posted_time DATETIME,
    UNIQUE(id)
);
INSERT INTO posts(id, title, body, user, sub, url, posted_time) VALUES(0, "Initial Title", "This is the body of the post.", "user1", "Sub", "www.example.com", "2020-03-07 17:53:33");
INSERT INTO posts(id, title, body, user, sub, url, posted_time) VALUES(1, "Water Slide", "There is a hole in the ceiling in EC-109", "CPSC-Student1002", "CSUF", "www.fullerton.edu", "2020-03-08 13:43:23");
INSERT INTO posts(id, title, body, user, sub, url, posted_time) VALUES(2, "Suber Bowl", "Who's gonna win?", "nflfan28392", "NFL", "www.NFL.com", "2020-01-27 12:20:10");
INSERT INTO posts(id, title, body, user, sub, url, posted_time) VALUES(3, "Something Controversial", "This post is controversial", "controversyuser1190","mildlycontroversial", "https://en.wikipedia.org/wiki/Controversy", "2020-02-10 08:34:21");
COMMIT;

BEGIN TRANSACTION;
DROP TABLE IF EXISTS votes;
CREATE TABLE votes (
    id INTEGER primary key,
    up_votes INT,
    down_votes INT,
    FOREIGN KEY (id) REFERENCES posts(id)
);

INSERT INTO votes(id, up_votes, down_votes) VALUES(0, 37, 2);
INSERT INTO votes(id, up_votes, down_votes) VALUES(1, 127, 20);
INSERT INTO votes(id, up_votes, down_votes) VALUES(2, 90, 12);
INSERT INTO votes(id, up_votes, down_votes) VALUES(3, 20, 232);