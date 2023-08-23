-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMETER //

CREATE TRIGGER update_email 
BEFORE UPDATE on users 
FOR EACH ROW 
BEGIN 
	IF NEW.email <> OLD.email THEN
		SET NEW.valid_email = 0
	END IF;
END;
//

DELIMITER;

