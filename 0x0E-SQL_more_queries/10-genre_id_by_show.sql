-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, genre_id FROM tv_shows AS shows
INNER JOIN tv_show_genres AS genres
ON shows.id = genres.show_id
ORDER BY title, genre_id;
