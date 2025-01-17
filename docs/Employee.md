# Employee Table

## Purpose
Stores information about employees.

## Columns
- `EmployeeId` (`INT NOT NULL`): Primary key, unique identifier for an employee.
- `LastName`, `FirstName` (`VARCHAR(20) NOT NULL`): Employee's name.
- `Title` (`VARCHAR(30)`): Job title.
- `ReportsTo` (`INT`): Foreign key referencing another `Employee`.
- `BirthDate`, `HireDate` (`TIMESTAMP`): Dates of birth and hiring.
- `Address`, `City`, `State`, `Country`, `PostalCode`: Address details (`VARCHAR(70, 40, 40, 40, 10)`).
- `Phone`, `Fax` (`VARCHAR(24)`): Contact numbers.
- `Email` (`VARCHAR(60)`): Email address.

## Relationships
- Self-referential relationship for hierarchical reporting (`FK_EmployeeReportsTo`).
- Indexed for faster lookups on `ReportsTo`.