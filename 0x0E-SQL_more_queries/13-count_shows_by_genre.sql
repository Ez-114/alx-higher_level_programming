-- list all genres and the number of shows linked to each.
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
	FROM tv_genres AS g
		INNER JOIN tv_show_genres AS sg
		ON g.id = sg.genre_id
	GROUP BY g.name
	ORDER BY number_of_shows DESC;
