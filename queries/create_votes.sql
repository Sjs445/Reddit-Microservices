-- :name create_votes :insert
INSERT INTO votes(id, up_votes, down_votes)
VALUES(:id, 0, 0)