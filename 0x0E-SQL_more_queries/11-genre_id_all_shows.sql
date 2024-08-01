-- list all shows with there genres
SELECT s.title, tg.genre_id
	FROM tv_shows AS s
		LEFT JOIN tv_show_genres AS tg
		ON s.id = tg.show_id

	ORDER BY s.title ASC,		-- Ordering as requested
		tg.genre_id ASC;
