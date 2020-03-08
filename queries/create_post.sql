-- :name create_post :insert
INSERT INTO posts(id, title, body, user, sub, up_votes, down_votes, posted_time)
VALUES(:id, :title, :body, :user, :sub, :up_votes, :down_votes, :posted_time)
