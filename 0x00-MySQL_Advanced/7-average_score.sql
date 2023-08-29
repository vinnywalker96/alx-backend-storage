-- Calculates Average

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT)
BEGIN
	DECLARE average_score DECIMAL(10, 2)
	SELECT AVG(score) INTO average_score FROM corrections WHERE id = user_id LIMIT 1;
END //
DELIMITER ;
