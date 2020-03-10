-- :name sorted_by_score :many
SELECT * FROM posts
ORDER BY up_votes - down_votes DESC;