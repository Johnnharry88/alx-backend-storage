-- Creats stored procedure ComputeAverageWeightedScoreForUsers

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users AS us,
		(SELECT u.id, SUM(c.score * p.weight) / SUM(p.weight) AS avg_weight
		FROM users AS u JOIN corrections AS c ON u.id = c.user_id
		JOIN projects AS p ON c.project_id = p.id
		GROUP BY u.id) AS x
	SET us.average_score = x.avg_weight
	WHERE us.id = x.id;
END $$
DELIMITER ;
