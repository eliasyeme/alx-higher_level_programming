-- Lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Each record will display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
-- The database name will be passed as an argument of the mysql command
SELECT
    title,
    name
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY
    title ASC,
    name ASC;