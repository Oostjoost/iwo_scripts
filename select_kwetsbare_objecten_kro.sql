-- Join KRO aanzien van 4 regio's tot 1 tabel
CREATE TABLE kro.kro_nw4 AS
SELECT * FROM kro.aanzien_r10;

INSERT INTO kro.kro_nw4 
SELECT * FROM kro.aanzien_r11

INSERT INTO kro.kro_nw4 
SELECT * FROM kro.aanzien_r12

INSERT INTO kro.kro_nw4 
SELECT * FROM kro.aanzien_r13

-- Join KRO gebruik van 4 regio's tot 1 tabel
CREATE TABLE kro.kro_nw4_gebruik AS
SELECT * FROM kro.gebruik_r10;

INSERT INTO kro.kro_nw4_gebruik 
SELECT * FROM kro.gebruik_r11

INSERT INTO kro.kro_nw4_gebruik 
SELECT * FROM kro.gebruik_r12

INSERT INTO kro.kro_nw4_gebruik 
SELECT * FROM kro.gebruik_r13

-- Create de kwetsbare objecten tabel
CREATE TABLE iwo.kwetsbare_objecten AS
SELECT a.bronsleutel, a.geom::geometry(Point, 28992), bouwbest, '87' as icon, 'niet_zelfredzaam' AS icon_name from kro.kro_nw4_aanzien a
LEFT JOIN kro.kro_nw4_gebruik g ON a.bronsleutel = g.aanzien_id
WHERE a.bouwbest ~* 'verzorging' OR a.bouwbest ~* 'ziek' OR a.bouwbest ~* 'gehand*'
UNION
SELECT a.bronsleutel, a.geom::geometry(Point, 28992), bouwbest, '86' as icon, 'ziekenhuis' AS icon_name from kro.kro_nw4_aanzien a
LEFT JOIN kro.kro_nw4_gebruik g ON a.bronsleutel = g.aanzien_id
WHERE a.bouwbest ~* 'ziek'
UNION
SELECT a.bronsleutel, a.geom::geometry(Point, 28992), 'cel', '84' as icon, 'cel_politie' AS icon_name from kro.kro_nw4_aanzien a
LEFT JOIN kro.kro_nw4_gebruik g ON a.bronsleutel = g.aanzien_id
WHERE a.bouwbest ~* 'gevang' OR act1omschr = 'Politie'
UNION
SELECT g.aanzien_id, g.geom::geometry(Point, 28992), 'brzo', 'PRB' as icon, 'brzo' AS icon_name from kro.kro_nw4_aanzien a
RIGHT JOIN kro.kro_nw4_gebruik g ON a.bronsleutel = g.aanzien_id
WHERE g.omschrijving = 'BRZO' 