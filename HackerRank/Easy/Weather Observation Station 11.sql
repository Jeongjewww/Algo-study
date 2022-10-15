SELECT DISTINCT CITY FROM STATION
WHERE NOT REGEXP_LIKE (CITY, '^[AEIOU]', 'i') OR NOT REGEXP_LIKE (CITY, '[AEIOU]$', 'i');