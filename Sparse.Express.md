# The Laws of Sparse Express

## The Primary Laws

1. All Sparse Express Framework Laws must adhere to the Laws defined in `Sparse.md`. `No Exceptions.`
2. All Express specific Sparse Laws must be specified within this file. `No Exceptions.`

## Express Specific Laws

3. Express apps must be structured into three distinct layers: Web (routes/controllers), Service (business logic), and Data (database interactions). `No Exceptions.`
4. All controllers must perform three tasks only: extract input, call the service layer, and return output. `No Exceptions.`
5. Each resource must have its own router file. `No Exceptions.`
6. All services must receive dependencies through constructor parameters (dependency injection) or factory functions. `No Exceptions.`
7. All business logic must reside in the service layer, not attached to domain models or controllers. `No Exceptions.`
8. All route handlers must be asynchronous functions using async/await, and all must be wrapped to catch rejected promises. `No Exceptions.`
9. All errors must propagate to a centralized error handling middleware at the bottom of the middleware stack. `No Exceptions.`
10. All input validation must happen in a dedicated middleware using a schema validation library. `No Exceptions.`
11. App and Server must be separated into different files. `No Exceptions.`
12. Any concern which applies to multiple routes must be implemented as middleware. `No Exceptions.`
13. The following Middleware must execute in the following order: security, parsing, logging, authentication, routing, error handling. `No Exceptions.`
14. Middleware may invoke services, but must not implement business logic itself. `No Exceptions.`
15. All environment-specific configuration must be managed using environment variables and a configuration module. `No Exceptions.`

`No Exceptions.`
