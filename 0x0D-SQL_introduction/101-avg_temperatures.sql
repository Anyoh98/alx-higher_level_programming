-- Script that imports a table and displays the avergae temp in fahrehnheit
SELECT `city`, AVG(`value`) AS `avg_temp`
from `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
