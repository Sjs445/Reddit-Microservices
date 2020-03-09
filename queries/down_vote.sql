UPDATE votes
SET downvotes = downvotes + 1,
WHERE post=:post;
