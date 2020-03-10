-- :name vote_by_id :one
SELECT * FROM posts
WHERE id = :id
