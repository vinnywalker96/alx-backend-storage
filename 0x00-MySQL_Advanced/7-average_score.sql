-- Calculates Average

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT)
BEGIN
	DECLARE avg_score DECIMAL(10, 2)
	SELECT AVG(score) INTO avg_score
	FROM score
	WHERE id = user_id;

	UPDATE users SET average_score = avg_score
	WHERE id = user_id
END //
DELIMITER ;
