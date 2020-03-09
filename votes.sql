-- $ sqlite3 votes.db < votes.sql

PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
DROP TABLE IF EXISTS votes;
CREATE TABLE votes (
	id INTEGER PRIMARY KEY,
	post_id INTEGER,
	up_vote INTEGER,
	down_vote INTEGER,
	sub_id, VARCHAR
	UNIQUE(id)
);

INSERT INTO votes(id, post_id, up_votes, down_votes, sub_id) VALUES(1, 30, 3, 0, 'news');
INSERT INTO votes(id, post_id, up_votes, down_votes, sub_id) VALUES(2, 45, 3, 0, 'memes')
INSERT INTO votes(id, post_id, up_votes, down_votes, sub_id) VALUES(3, 22, 3, 0, 'ask')
INSERT INTO votes(id, post_id, up_votes, down_votes, sub_id) VALUES(4, 23, 3, 0, 'AMA')
INSERT INTO votes(id, post_id, up_votes, down_votes, sub_id) VALUES(5, 44, 3, 0, 'advice')
COMMIT;
