-- :name top_n :many
SELECT * FROM posts
ORDER BY up_votes - down_votes DESC
LIMIT :top_n;
