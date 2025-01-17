# Invoice Table

## Purpose
Stores information about invoices.

## Columns
- `InvoiceId` (`INT NOT NULL`): Primary key, unique identifier for an invoice.
- `CustomerId` (`INT NOT NULL`): Foreign key referencing `Customer`.
- `InvoiceDate` (`TIMESTAMP NOT NULL`): Date of the invoice.
- `BillingAddress`, `BillingCity`, `BillingState`, `BillingCountry`, `BillingPostalCode`: Billing details (`VARCHAR(70, 40, 40, 40, 10)`).
- `Total` (`NUMERIC(10,2) NOT NULL`): Total amount of the invoice.

## Relationships
- Linked to `Customer` via `CustomerId` (`FK_InvoiceCustomerId`).
- Indexed for faster lookups on `CustomerId`.