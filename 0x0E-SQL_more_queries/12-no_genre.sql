-- get the shows that have no genres
SELECT s.title, tg.genre_id
	FROM tv_shows AS s
		LEFT JOIN tv_show_genres AS tg
		ON s.id = tg.show_id
	WHERE tg.show_id IS NULL
	ORDER BY s.title ASC, tg.genre_id ASC;
