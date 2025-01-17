# MediaType Table

## Purpose
Stores information about media types.

## Columns
- `MediaTypeId` (`INT NOT NULL`): Primary key, unique identifier for a media type.
- `Name` (`VARCHAR(120)`): Media type name.

## Relationships
- Referenced by the `Track` table.