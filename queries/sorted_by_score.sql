-- :name sorted_by_score :many
SELECT * FROM votes
WHERE id in :id
ORDER BY up_votes - down_votes DESC;