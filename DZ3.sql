CREATE TABLE IF NOT EXISTS Genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Performers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS GenresPerformers (
	genres_id INTEGER REFERENCES Genres(id),
	performers_id INTEGER REFERENCES Performers(id),
	CONSTRAINT GenresPerformers_pk PRIMARY KEY (genres_id, performers_id)
);

CREATE TABLE IF NOT EXISTS Album (
	id SERIAL PRIMARY KEY,
	name VARCHAR(80) NOT NULL,
	year_of_release INTEGER
);

CREATE TABLE IF NOT EXISTS Track (
	id SERIAL PRIMARY KEY,
	name VARCHAR(80) NOT NULL,
	track_duration INTEGER,
	album_id INTEGER REFERENCES Album(id)
);

CREATE TABLE IF NOT EXISTS AlbumPerformers (
	album_id INTEGER REFERENCES Album(id),
	performers_id INTEGER REFERENCES Performers(id),
	CONSTRAINT AlbumPerformers_pk PRIMARY KEY (album_id, performers_id)
);

CREATE TABLE IF NOT EXISTS Collection_of_tracks (
	id SERIAL PRIMARY KEY,
	name VARCHAR(80) NOT NULL,
	year_of_release INTEGER
);

CREATE TABLE IF NOT EXISTS CollectionTrack (
	collection_of_tracks_id INTEGER REFERENCES Collection_of_tracks(id),
	track_id INTEGER REFERENCES Track(id),
	CONSTRAINT CollectionTrack_pk PRIMARY KEY (collection_of_tracks_id, track_id)
);