DECLARE a DATE DEFAULT '1982-01-01';
select *
FROM `tetramumbai.summer`
WHERE year = extract(year from a);
