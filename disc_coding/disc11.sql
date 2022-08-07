-- Q3
SELECT name FROM records WHERE supervisor = "Oliver Warbucks";

-- Q4
SELECT * FROM records WHERE name = supervisor;

-- Q5
SELECT name FROM records WHERE salary > 50000 ORDER BY name;

-- Q6
SELECT m.day, m.time FROM records AS r, meetings AS m WHERE r.division = m.division 
        AND r.supervisor = "Oliver Warbucks";   

-- Q7
SELECT e.name FROM records AS e, records AS s WHERE e.supervisor = s.name AND e.division != s.division;

-- Q8
SELECT d.name From records as d, records AS m WHERE d.supervisor = m.name AND m.name != m.supervisor;

-- Q9
SELECT supervisor, SUM(salary) FROM records GROUP BY supervivor;

-- Q10
SELECT m.day FROM records AS e, meetings AS m WHERE e.division = m.division GROUP BY m.day HAVING COUNT(*) < 5;

-- Q11
SELECT e1.division FROM records AS e1, records AS e2 WHERE e1.name != e2.name AND e1.division = e2.division 
GROUP BY e1.division HAVING MAX(e1.salary + e2.salary) < 100000;
