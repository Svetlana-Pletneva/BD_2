import sqlalchemy

db = 'postgresql://pletneva:Z2012S1981@localhost:5432/music_site'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

album_1 = connection.execute("""
SELECT name, year FROM Album
    WHERE year = 2018
    """).fetchall()
print('Название и год выхода альбомов, вышедших в 2018 году: ', album_1)

long_track = connection.execute("""
SELECT title, track_time FROM Tracks
    ORDER BY track_time DESC
    LIMIT 1
    """).fetchall()
print('Название и продолжительность самого длительного трека: ', long_track)

time_track = connection.execute("""
SELECT title FROM Tracks
    WHERE track_time >= 3.5
    """).fetchall()
print('Название треков, продолжительность которых не менее 3.5 минуты: ', time_track)

collection_1 = connection.execute("""
SELECT name FROM Collection
    WHERE year BETWEEN 2018 AND 2020
    """).fetchall()
print('Название сборников, вышедших в период с 2018 по 2020 год включительно: ', collection_1)

artist_1 = connection.execute("""
SELECT name FROM Artist
    WHERE NOT name LIKE '%% %%'
    """).fetchall()
print('Исполнители, чье имя состоит из одного слова: ', artist_1)

track_2 = connection.execute("""
SELECT title FROM Tracks
    WHERE title ILIKE '%%my%%'
    """).fetchall()
print('Название треков, которые содержат слово "мой": ', track_2)