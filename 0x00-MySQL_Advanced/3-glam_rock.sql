-- script that lists all bands with Glam rock as their main style

SELECT
    band_name,
    IFNULL(
        CASE
            WHEN split = 1 THEN (YEAR(formed) + 1) - YEAR(split)
            ELSE 2022 - YEAR(formed)
        END,
        0
    ) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;

