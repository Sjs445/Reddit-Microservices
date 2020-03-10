-- :name up_vote :affected
UPDATE posts
SET up_votes = up_votes + 1,
WHERE id=:id;

