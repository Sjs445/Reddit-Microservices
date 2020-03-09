-- :name get_recent_posts_sub :many
SELECT * from posts
WHERE sub = :sub
ORDER BY posted_time DESC
LIMIT :number_of_posts