-- List all shows with associated genre_id from the hbtn_0d_tvshows database.
-- List shows with title and associated genre_id (or NULL if no genre)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
