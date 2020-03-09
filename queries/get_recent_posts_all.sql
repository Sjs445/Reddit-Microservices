-- :name get_recent_posts_all :many
SELECT * from posts
ORDER BY posted_time DESC
LIMIT :number_of_posts
