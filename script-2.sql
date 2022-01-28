create table if not exists Genre (
	genre_id serial primary key,
	name varchar (40) not null
	
);

create table if not exists Artist (
	artist_id serial primary key,
	name varchar(40) unique not null
);	

create table if not exists Album (
	album_id serial primary key,
	name varchar(100) not null,
	year integer not null
);

create table if not exists Tracks (
	track_id serial primary key,
	title text not null,
	track_time integer,
	album_id integer references album(album_id)
);

create table if not exists Collection (
	collection_id serial primary key,
	name varchar (100) not null,
	year integer not null
);

create table if not exists ArtistGenre (
	id serial primary key,
	artist_id integer not null references artist(artist_id),
	genre_id integer not null references genre(genre_id)
);

create table if not exists ArtistAlbum (
	id serial primary key,
	artist_id integer not null references artist(artist_id),
	album_id integer not null references album (album_id)
);

create table if not exists TrackCollection (
	id serial primary key,
	track_id integer not null references tracks(track_id),
	collection_id integer not null references collection(collection_id)
);






