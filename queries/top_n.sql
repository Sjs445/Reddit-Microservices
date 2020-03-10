-- :name top_n :many
SELECT * FROM votes
ORDER BY (up_votes - down_votes) DESC
LIMIT :top_n;
