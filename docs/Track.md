# Track Table

## Purpose
Stores information about music tracks.

## Columns
- `TrackId` (`INT NOT NULL`): Primary key, unique identifier for a track.
- `Name` (`VARCHAR(200) NOT NULL`): Track name.
- `AlbumId` (`INT`): Foreign key referencing `Album`.
- `MediaTypeId` (`INT NOT NULL`): Foreign key referencing `MediaType`.
- `GenreId` (`INT`): Foreign key referencing `Genre`.
- `Composer` (`VARCHAR(220)`): Composer name.
- `Milliseconds` (`INT NOT NULL`): Track duration in milliseconds.
- `Bytes` (`INT`): Track size in bytes.
- `UnitPrice` (`NUMERIC(10,2) NOT NULL`): Track price.

## Relationships
- Linked to `Album`, `MediaType`, and `Genre`.
- Referenced by `InvoiceLine` and `PlaylistTrack`.