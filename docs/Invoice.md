# Invoice Table
Stores information about completed sales and invoices. Invoices are the completed sales to customers.

## Columns
- `InvoiceId` (`INT NOT NULL`): Primary key, unique identifier for an invoice.
- `CustomerId` (`INT NOT NULL`): Foreign key referencing `Customer`.
- `InvoiceDate` (`TIMESTAMP NOT NULL`): Date of the invoice.
- `BillingAddress`, `BillingCity`, `BillingState`, `BillingCountry`, `BillingPostalCode`: Billing details (`VARCHAR(70, 40, 40, 40, 10)`).
- `Total` (`NUMERIC(10,2) NOT NULL`): Total amount of the invoice completed on the sale

## Relationships
- Linked to `Customer` via `CustomerId` (`FK_InvoiceCustomerId`).
- Indexed for faster lookups on `CustomerId`.