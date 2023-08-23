-- script that creates a trigger that resets the attribute valid_email only when the email has been changed.

CREATE TRIGGER update_email AFTER UPDATE on users FOR EACH ROW UPDATE email SET valid_email = 0;
 
