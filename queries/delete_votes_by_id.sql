-- :name delete_votes_by_id :affected
DELETE FROM votes
WHERE id = :id;