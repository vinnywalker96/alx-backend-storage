-- Calculates Average

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT)
BEGIN
	SELECT AVG(score) INTO average_score FROM corrections;
END //
DELIMITER ;
