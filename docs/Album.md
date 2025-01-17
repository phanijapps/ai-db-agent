# Album is a Postgers Database Table used Stores information about albums.

## Columns
- AlbumId (INT NOT NULL): Primary key, unique identifier for an album.
- Title (VARCHAR(160) NOT NULL): Title of the album.
- ArtistId (INT NOT NULL): Foreign key referencing Artist table.

## Relationships
- Linked to the Artist table through ArtistId (FK_AlbumArtistId).
- Indexed for faster lookups on ArtistId.