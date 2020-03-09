-- :name delete_post_by_id :affected
DELETE FROM posts
WHERE id = :id;