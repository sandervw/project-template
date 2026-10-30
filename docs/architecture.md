# Architecture

Terms follow [the glossary](glossary.md). Sections 1 and 6 are binding; change them in the same PR as the code that needs it. The boundary check enforces them.

## 1. Contexts, shells, and boundaries

A functional core with adapter shells.

| Context (`core/`) | Owns |
|---|---|
| `[context]/` (core domain) | [the rules and concepts it owns] |

| Upstream | Downstream | What crosses |
|---|---|---|
| [Context] | [Context or shell] | [types and functions from its public entry point] |

No other context imports another. A shell calls contexts in turn and passes plain values; it makes no rule of its own. A new arrow or a new context changes this section.

| Shell | Runs in | Imports | Does |
|---|---|---|---|
| `[shell]/` | [runtime] | [libraries], core | [what it adapts] |

**Rules.** [The boundary tool, its config file, and its command.] Core imports nothing outside `core/` except [allowed pure libraries], and never touches I/O, the clock, randomness, or global state. No `utils`, `helpers`, `manager`, `common`, or `data` modules.

## 2. Data flows

- **[Flow]:** [where it starts, which contexts and shells it passes through, where it ends.]

## 3. Domain model

- **[Aggregate or value]:** [fields, invariants, and the operations that change it.]

## 4. Storage

[What is stored where, its shape, ownership, and how migrations ship.]

## 5. Interfaces

[The public surface: routes, commands, protocols, or messages, with their checks and error shape.]

## 6. Folder layout

One folder per context, one public entry point each; the rest is private.

```
[layout]
```

## 7. Security

[Assets, trust boundaries, auth, ownership checks, input parsing, secrets, and test-key rules.]

## 8. Risks

- **[Risk].** [Fallback.]
