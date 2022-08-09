-- Q1
SELECT quarter FROM scoring GROUP BY HAVING SUM(points) > 10;

-- Q2
SELECT team, SUM(points) FROM players, scoring 
    WHERE name = players GROUP BY team;