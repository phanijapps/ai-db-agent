# Artist is a postgres db table that stores information about artists. It is referenced by Album table.

## Columns
- ArtistId (INT NOT NULL): Primary key, unique identifier for an artist.
- Name (VARCHAR(120)): Name of the artist.

## Relationships
- Referenced by the Album table.