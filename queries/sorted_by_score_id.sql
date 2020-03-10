-- :name sorted_by_score_id :many
SELECT * FROM posts
WHERE id in :id
ORDER BY up_votes - down_votes DESC
