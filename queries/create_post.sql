-- :name create_post :insert
INSERT INTO posts(id, title, body, user, sub, url, posted_time)
VALUES(:id, :title, :body, :user, :sub, :url, :posted_time)
