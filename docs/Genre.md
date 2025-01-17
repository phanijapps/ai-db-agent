# Genre Table

## Purpose
Stores information about music genres.

## Columns
- `GenreId` (`INT NOT NULL`): Primary key, unique identifier for a genre.
- `Name` (`VARCHAR(120)`): Genre name.

## Relationships
- Referenced by the `Track` table.