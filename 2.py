import sqlalchemy

db = 'postgresql://pletneva:Z2012S1981@localhost:5432/music_site'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

artist_in_genre = connection.execute("""
SELECT name, COUNT(artist_id) FROM Genre
    JOIN ArtistGenre ON Genre.genre_id = ArtistGenre.genre_id
    GROUP BY genre.name
    """).fetchall()
print('Количество исполнителей в каждом жанре', artist_in_genre)

track_in_album = connection.execute("""
SELECT year, COUNT(track_id) FROM Album
    JOIN Tracks ON Album.album_id = Tracks.album_id
    WHERE year BETWEEN 2019 AND 2020
    GROUP BY album.year
    """).fetchall()
print('Количество треков, вошедших в альбомы 2019-2020 годов:', track_in_album)

avg_time_track = connection.execute("""
SELECT album.name, AVG(track_time) FROM Tracks
    JOIN Album ON Album.album_id = Tracks.album_id
    GROUP BY album.name
    """).fetchall()
print('Средняя продолжительность треков по альбомам:', avg_time_track)

artist_without_album2020 = connection.execute("""
SELECT name FROM artist
    WHERE NOT artist.artist_id = (
    SELECT artist.artist_id FROM artist
    JOIN artistalbum ON artist.artist_id = artistalbum.artist_id
    JOIN album ON artistalbum.album_id = album.album_id
    WHERE album.year = 2020) 
    """).fetchall()
print('Исполнители, не выпустившие альбомы в 2020году:', artist_without_album2020)

collection_with_The_Beatles = connection.execute("""
SELECT collection.name FROM collection
    JOIN trackcollection ON collection.collection_id = trackcollection.collection_id
    JOIN tracks ON trackcollection.track_id = tracks.track_id
    JOIN album ON tracks.album_id = album.album_id
    JOIN artistalbum ON album.album_id = artistalbum.album_id
    JOIN artist ON artistalbum.artist_id = artist.artist_id
    WHERE artist.name = 'The Beatles'
    """).fetchall()
print('Названия сборников в которых присутствует The Beatles:', collection_with_The_Beatles)

albums_with_artist_some_genres = connection.execute("""
SELECT album.name FROM artistgenre
    JOIN artist ON artistgenre.artist_id = artist.artist_id
    JOIN artistalbum ON artist.artist_id = artistalbum.artist_id
    JOIN album ON artistalbum.album_id = album.album_id
    GROUP BY album.name
    HAVING COUNT(artistgenre.artist_id) > 1
    """).fetchall()
print('Названия альбомов в которых присутствует исполнители более 1 жанра:', albums_with_artist_some_genres)

tracks_not_in_collection = connection.execute("""
SELECT tracks.title FROM tracks
    LEFT JOIN trackcollection ON tracks.track_id = trackcollection.track_id
    GROUP BY tracks.title
    HAVING COUNT(trackcollection.track_id) = 0
    """).fetchall()
print('Наименование треков, которые не входят в сборники:', tracks_not_in_collection)

artist_with_min_track = connection.execute("""
SELECT artist.name FROM artist 
    JOIN artistalbum ON artist.artist_id = artistalbum.artist_id
    JOIN album ON artistalbum.album_id = album.album_id
    JOIN tracks ON album.album_id = tracks.album_id
    WHERE track_time = (
    SELECT MIN(track_time) FROM tracks)
    """).fetchall()
print('Исполнитель, написавший самый короткий трек:', artist_with_min_track)

min_album = connection.execute("""
SELECT album.name FROM album
    JOIN tracks ON album.album_id = tracks.album_id
    GROUP BY album.name
    HAVING COUNT(tracks.album_id) = (
    SELECT tracks.album_id FROM tracks
    JOIN album ON tracks.album_id = album.album_id
    GROUP BY tracks.album_id LIMIT 1) 
    """).fetchall()
print('Название альбомов, содержащих наименьшее количество треков:', min_album)