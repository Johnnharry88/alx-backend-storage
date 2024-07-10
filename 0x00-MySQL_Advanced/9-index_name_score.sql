-- Creates an index_name_first_score on table names and 
-- first letter of score name

CREATE INDEX idx_name_first_score ON names(name(1), score);
