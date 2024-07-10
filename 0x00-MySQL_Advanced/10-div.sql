-- Creates a function SafeDiv that divides a by b
-- and returns the ans or returns 0 if b = o

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
	DECLARE res FLOAT DEFAULT 0;

	IF b != 0 THEN
		SET res = a / b;
	ELSE
		SET res = 0;
	END IF;
	RETURN res;
END $$
DELIMITER ;
