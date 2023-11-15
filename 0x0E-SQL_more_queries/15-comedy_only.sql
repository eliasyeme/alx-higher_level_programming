-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy id can be different
-- Each record will display: tv_shows.title
-- Results is sorted in ascending order by the show title
-- The database name will be passed as an argument of the mysql command
SELECT
    title
FROM
    tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE
    tv_genres.name = 'Comedy'
GROUP BY
    title
ORDER BY
    title ASC;