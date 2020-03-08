-- :name delete_post_by_id :one
DELETE FROM posts
WHERE id = :id;