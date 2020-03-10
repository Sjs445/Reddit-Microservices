-- :name sorted_by_score :many
SELECT id, up_votes, down_votes FROM votes
ORDER BY (up_votes - down_votes) DESC