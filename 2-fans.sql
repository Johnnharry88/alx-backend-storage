-- A SQL script that ranks country based on origins of bands

SELECT origin, SUM(fans) AS nb_fans
	FROM metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC;
