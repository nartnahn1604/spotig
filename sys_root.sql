CREATE TABLE AUTHORS(
    AUTHOR_ID INT NOT NULL PRIMARY KEY,
    AUTHOR_NAME VARCHAR2(100),
    AUTHOR_BIO VARCHAR2(2000),
    AUTHOR_AVT VARCHAR2(100)
);

CREATE TABLE SONGS (
    SONG_ID INT NOT NULL PRIMARY KEY,
    AUTHOR_ID INT,
    ARTIST_ID INT,
    ALBUM_ID INT,
    SONG_NAME VARCHAR2(1000),
    GENRE_ID INT,
    SONG_URL VARCHAR2(2000)
);

alter table songs
add SONG_THUMB varchar2(2000);

alter table Albums
add ALBUM_THUMB VARCHAR2(2000);

CREATE TABLE ARTISTS(
    ARTIST_ID INT NOT NULL PRIMARY KEY,
    ARTIST_NAME VARCHAR2(100),
    ARTIST_AVT VARCHAR2(100),
    ARTIST_BIO VARCHAR2(2000)
);

CREATE TABLE ALBUMS(
    ALBUM_ID INT NOT NULL PRIMARY KEY,
    ALBUM_NAME VARCHAR2(200),
    ARTIST_ID INT
);

CREATE TABLE GENRES(
    GENRE_ID INT NOT NULL PRIMARY KEY,
    GENRE_NAME VARCHAR2(200)
);

create table users(
    user_id int not null primary key,
    access_token varchar2(4000)
);

CREATE SEQUENCE user_seq
  START WITH 1
  INCREMENT BY 1;

insert into authors values(aut_seq.nextval, 'Kh?c Vi?t', 'Nghe si 8x ...', 'them public key vo day');

insert into songs values(song_seq.nextval, 1, 1, null, 'Tim lai bau troi', null, '0lO9wECCROX9NMHOgvjQ9M', null);

insert into artists values(art_seq.nextval, 'Tuan Hung', null, null);

insert into albums values(alb_seq.nextval, 'Tim lai bau troi', 1, null);


