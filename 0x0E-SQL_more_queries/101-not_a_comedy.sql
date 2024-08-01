-- list shows that have the comedy genre
SELECT s.title
	FROM tv_shows AS s
	WHERE s.id NOT IN (
		SELECT s.id	
			FROM tv_shows AS s
				LEFT JOIN tv_show_genres AS sg
				ON s.id = sg.show_id

				LEFT JOIN tv_genres AS g
				ON sg.genre_id = g.id
			WHERE g.name = 'Comedy')
	ORDER BY s.title ASC;
