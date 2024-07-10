-- Creates a trigger that resets attribute valid_email

DROP TRIGGER IF EXISTS validator_email;
DELIMITER $$ 
CREATE TRIGGER validator_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	ELSE
		SET NEW.valid_email = NEW.valid_email;
	END IF;
END $$
DELIMITER ;
