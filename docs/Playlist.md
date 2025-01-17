# Playlist Table

## Purpose
Stores information about playlists.

## Columns
- `PlaylistId` (`INT NOT NULL`): Primary key, unique identifier for a playlist.
- `Name` (`VARCHAR(120)`): Playlist name.

## Relationships
- Linked to `PlaylistTrack`.