# Customer Table

## Purpose
Stores information about customers.

## Columns
- `CustomerId` (`INT NOT NULL`): Primary key, unique identifier for a customer.
- `FirstName` (`VARCHAR(40) NOT NULL`): Customer's first name.
- `LastName` (`VARCHAR(20) NOT NULL`): Customer's last name.
- `Company` (`VARCHAR(80)`): Optional company name.
- `Address`, `City`, `State`, `Country`, `PostalCode`: Address details (`VARCHAR(70, 40, 40, 40, 10)`).
- `Phone`, `Fax`: Contact numbers (`VARCHAR(24)`).
- `Email` (`VARCHAR(60) NOT NULL`): Email address of the customer.
- `SupportRepId` (`INT`): Foreign key referencing the `Employee` table.

## Relationships
- Linked to `Employee` via `SupportRepId` (`FK_CustomerSupportRepId`).
- Indexed for faster lookups on `SupportRepId`.