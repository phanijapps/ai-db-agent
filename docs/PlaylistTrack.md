# PlaylistTrack Table

## Purpose
Manages many-to-many relationships between playlists and tracks.

## Columns
- `PlaylistId` (`INT NOT NULL`): Composite primary key, foreign key referencing `Playlist`.
- `TrackId` (`INT NOT NULL`): Composite primary key, foreign key referencing `Track`.

## Relationships
- Many-to-many relationship between `Playlist` and `Track`.