-- Creates an index idx_name_first on the first latter of name 
-- in the table names

CREATE INDEX idx_name_first ON names(name(1));
