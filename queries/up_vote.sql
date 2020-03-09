UPDATE votes
SET upvotes = upvotes + 1,
WHERE post=:post;

