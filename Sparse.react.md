# The Laws of Sparse React

## The Primary Laws

1. All Sparse React Laws must adhere to the Laws defined in `Sparse.md`. `No Exceptions.`
2. All React specific Sparse Laws must be specified within this file. `No Exceptions.`

## React Specific Laws

3. Ever feature which requires both UI and external dependencies must be split into three layers: components/, hooks/, and services/. `No Exceptions.`
4. Components must be JSX views only, no data fetching, no business logic. `No Exceptions.`
5. Hooks must contain all stateful logic, side effects, and fetch requests via TanStack. `No Exceptions.`
6. Services must be pure synchronous business logic: no React imports. `No Exceptions.`
7. All object schemas must be defined in a dedicated types/ folder. `No Exceptions.`
8. All .tsx files must export a single component, named after the file. `No Exceptions.`
9. All react components which require properties must declare props using an interface at the top of the file, named `[ComponentName]Props`. `No Exceptions.`
10. Always destructure and pass props explicitly for your own components: never use `...rest` parameters. `No Exceptions.`
11. All components must use function components with hooks: no class components. `No Exceptions.`
12. If an event handler does more than a single function call, it must be extracted into a separate function. `No Exceptions.`
13. Every mapped element must have a stable, unique key derived from data, never array indexes. `No Exceptions.`
14. useEffect must only be used for external systems: data fetching, subscriptions, timers. `No Exceptions.`
15. Replace internal useEffect cases with derived state, memoization, or tanstack. `No Exceptions.`
16. Components must use no more than one level of ternary operators for conditional rendering. `No Exceptions.`

`No Exceptions.`
