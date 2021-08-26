import sqlalchemy

from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://ivaneto:nasharussia@localhost:5432/dz3')

con = engine.connect()

gen = (con.execute("""
SELECT genres_id, COUNT(performers_id) FROM GenresPerformers
GROUP BY genres_id
ORDER BY genres_id;
""").fetchall())

gen2 = (con.execute("""
SELECT name, COUNT(performers_id) FROM Genres g
JOIN GenresPerformers gp ON g.id = gp.genres_id
GROUP BY name;
""").fetchall())

count_track_19_20 = (con.execute("""
SELECT COUNT(t.id) FROM Album a
JOIN Track t ON a.id = t.album_id
WHERE a.year_of_release BETWEEN 2019 AND 2020;
""").fetchall())

avg_track = (con.execute("""
SELECT a.name, AVG(t.track_duration) FROM Album a
JOIN Track t ON a.id = t.album_id
GROUP BY a.name;
""").fetchall())

perf_none_20 = (con.execute("""
SELECT DISTINCT(p.name) FROM Performers p
JOIN AlbumPerformers ap ON p.id = ap.performers_id
JOIN Album a ON ap.album_id = a.id
WHERE a.year_of_release != 2020;
""").fetchall())

Collection_БИ_2 = (con.execute("""
SELECT DISTINCT(cot.name) FROM Performers p
JOIN AlbumPerformers ap ON p.id = ap.performers_id
JOIN Album a ON ap.album_id = a.id
JOIN Track t ON a.id = t.album_id
JOIN CollectionTrack ct ON t.id = ct.track_id
JOIN Collection_of_tracks cot ON ct.collection_of_tracks_id = cot.id
WHERE p.name = 'БИ-2';
""").fetchall())

zd_6 = (con.execute("""
SELECT a.name FROM GenresPerformers gp
JOIN Performers p ON gp.performers_id = p.id
JOIN AlbumPerformers ap ON p.id = ap.performers_id
JOIN Album a ON ap.album_id = a.id
WHERE p.id = ap.performers_id
GROUP BY a.name, ap.performers_id
HAVING COUNT(gp.genres_id) > 1;
""").fetchall())

track_not_included = (con.execute("""
SELECT t.name FROM Track t
LEFT JOIN CollectionTrack ct ON t.id = ct.track_id
WHERE ct.track_id IS NULL;
""").fetchall())

min_track_duration = (con.execute("""
SELECT p.name FROM Performers p
JOIN AlbumPerformers ap ON p.id = ap.performers_id
JOIN Album a ON ap.album_id = a.id
JOIN Track t ON a.id = t.album_id
WHERE t.track_duration = (SELECT MIN(track_duration) FROM Track)
GROUP BY p.name;
""").fetchall())

zd_9 = (con.execute("""
SELECT a.name FROM Album a
JOIN Track t ON a.id = t.album_id
GROUP BY a.name, t.album_id,t.id
HAVING MIN (SELECT COUNT(t.id) FROM );
""").fetchall())

# pprint(gen)
# pprint(gen2)
# pprint(count_track_19_20)
# pprint(avg_track)
# pprint(perf_none_20)
# pprint(Collection_БИ_2)
# pprint(zd_6)
# pprint(track_not_included)
# pprint(min_track_duration)
pprint(zd_9)

