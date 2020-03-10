-- :name vote_by_id :one
SELECT * FROM votes
WHERE id = :id
