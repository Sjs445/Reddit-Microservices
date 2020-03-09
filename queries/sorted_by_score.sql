SELECT * FROM votes
WHERE id in :id
ORDER BY (upvotes - downvotes) DESC
