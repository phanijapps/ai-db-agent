# InvoiceLine Table

## Purpose
Stores information about individual lines in an invoice.

## Columns
- `InvoiceLineId` (`INT NOT NULL`): Primary key, unique identifier for an invoice line.
- `InvoiceId` (`INT NOT NULL`): Foreign key referencing `Invoice`.
- `TrackId` (`INT NOT NULL`): Foreign key referencing `Track`.
- `UnitPrice` (`NUMERIC(10,2) NOT NULL`): Price per unit.
- `Quantity` (`INT NOT NULL`): Quantity sold.

## Relationships
- Linked to `Invoice` and `Track` via `InvoiceId` and `TrackId`.
- Indexed for faster lookups on `InvoiceId` and `TrackId`.