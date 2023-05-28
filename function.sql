CREATE OR REPLACE FUNCTION GET_SONGS RETURN SYS_REFCURSOR
AS
    result_cursor SYS_REFCURSOR;
BEGIN
    OPEN result_cursor FOR
    SELECT s.song_id, s.song_name, a.artist_name, au.author_name, al.album_name, g.genre_name, s.song_url, s.song_thumb
    FROM Songs s left JOIN Artists a on  s.artist_id = a.artist_id 
                left join Authors au on s.author_id = au.author_id 
                left join Albums al on s.album_id = al.album_id 
                left join Genres g on s.song_id = g.genre_id;
    
  RETURN result_cursor;
END;

CREATE OR REPLACE FUNCTION GET_ARTISTS RETURN SYS_REFCURSOR
AS
    result_cursor SYS_REFCURSOR;
BEGIN
    OPEN result_cursor FOR
    SELECT a.artist_id, artist_name, artist_avt, artist_bio, count(s.song_name)
    FROM Artists a INNER join Songs s on a.artist_id = s.artist_id
    GROUP BY a.artist_id, artist_name, artist_avt, artist_bio;
    
  RETURN result_cursor;
END;

CREATE OR REPLACE PROCEDURE add_user(access_token USERS.ACCESS_TOKEN%TYPE) AS
BEGIN
  INSERT INTO USERS VALUES(user_seq.nextval, access_token);
  Commit;
END;

CREATE OR REPLACE FUNCTION GET_USER(access_token USERS.ACCESS_TOKEN%TYPE) RETURN BOOLEAN AS
account USERS%ROWTYPE;
BEGIN
  SELECT * INTO account FROM USERS WHERE users.access_token = access_token;
  EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RETURN FALSE;
  RETURN TRUE;
END;

ALTER TABLE SONGS ADD CONSTRAINT FK_SONGS_AUTHOR_ID
FOREIGN KEY (AUTHOR_ID) REFERENCES AUTHORS (AUTHOR_ID);

ALTER TABLE SONGS ADD CONSTRAINT FK_SONGS_ARTIST_ID
FOREIGN KEY (ARTIST_ID) REFERENCES ARTISTS (ARTIST_ID);

ALTER TABLE SONGS ADD CONSTRAINT FK_SONGS_ALBUM_ID
FOREIGN KEY (ALBUM_ID) REFERENCES ALBUMS (ALBUM_ID);

ALTER TABLE SONGS ADD CONSTRAINT FK_SONGS_GENRE_ID
FOREIGN KEY (GENRE_ID) REFERENCES GENRES (GENRE_ID);

ALTER TABLE ALBUMS ADD CONSTRAINT FK_ALBUMS_ARTIST_ID
FOREIGN KEY (ARTIST_ID) REFERENCES ARTISTS (ARTIST_ID);

delete from songs;
delete from authors;
delete from artists;
delete from albums;
delete from genres;

select * from songs;
select * from authors;
select * from artists;
select * from albums;
select * from genres;

commit;

CREATE OR REPLACE FUNCTION GET_SONGS_BY_ARTIST(art_id NUMBER) RETURN SYS_REFCURSOR
AS
    result_cursor SYS_REFCURSOR;
BEGIN
    OPEN result_cursor FOR
    SELECT s.song_id, s.song_name, a.artist_name, au.author_name, al.album_name, g.genre_name, s.song_url, s.song_thumb
    FROM Songs s left JOIN Artists a on  s.artist_id = a.artist_id 
                left join Authors au on s.author_id = au.author_id 
                left join Albums al on s.album_id = al.album_id 
                left join Genres g on s.song_id = g.genre_id
    WHERE s.artist_id = art_id;
    
  RETURN result_cursor;
END;

declare
 result_cursor SYS_REFCURSOR;
begin
    result_cursor := GET_SONGS_BY_ARTIST(1);
    for i i
end;