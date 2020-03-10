-- :name down_vote :affected
UPDATE votes
SET down_votes = down_votes + 1,
WHERE id = :id;
