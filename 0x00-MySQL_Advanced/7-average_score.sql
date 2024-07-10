-- Creates a stored proceedure ComputeAverageForUser that 
-- computes and stores average score for a student

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE sum_of_scores INT DEFAULT 0;
	DECLARE count_project INT DEFAULT 0;

	SELECT SUM(score)
	    INTO sum_of_scores
	    FROM corrections
	    WHERE corrections.user_id = user_id;
	SELECT COUNT(*)
	    INTO count_project
	    FROM corrections
	    WHERE corrections.user_id = user_id;

	UPDATE users
	    SET users.average_score = IF(count_project = 0, 0, sum_of_scores / count_project)
	    WHERE users.id = user_id;
END $$
DELIMITER ;
