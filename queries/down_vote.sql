-- :name down_vote :affected
UPDATE posts
SET down_votes = down_votes + 1,
WHERE id = :id
