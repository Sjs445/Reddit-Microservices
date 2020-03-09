SELECT * FROM votes
ORDER BY (upvotes - downvotes) DESC
LIMIT :top_n
