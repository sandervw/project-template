# Kickoff agenda

A question bank, not a script. Ask what applies to this project, skip what doesn't, and add what the idea needs. **CEO** marks questions only the CEO decides; for the rest the CTO recommends and the CEO confirms.

## 1. Product

1. **CEO.** Who is it for, and what job does it do for them?
2. **CEO.** What does the MVP include, and what is explicitly out?
3. **CEO.** How does the user reach it: web, desktop, phone, CLI, API, a physical device, a model endpoint, a file?
4. **CEO.** What must be true for the MVP to count as a success?
5. **CEO.** Does a user need an account, and what can they do without one?

## 2. Core domain

1. What are the core concepts and their names (the first draft of the glossary)?
2. Which rules must always hold (invariants)?
3. Must results be deterministic or reproducible (seeds, versions, fixtures)?
4. Where are the natural seams between contexts?

## 3. Each part (repeat per part from the parts map)

1. Language and runtime, and why.
2. Framework or main library, with its connected libraries and services.
3. Where it runs: a browser, a server, serverless, an edge, a microcontroller, a GPU, a laptop.
4. Development flow: the local loop, hot reload or flashing, simulators, sample data.
5. What it costs to run at MVP scale and at ten times that.
6. How reversible the choice is, and what it rules out.

## 4. Data

1. What is stored, where, and who owns each record?
2. Schema and migrations: how changes ship without losing data.
3. Files, media, models, or datasets: where they live and how they are versioned.
4. Backups, retention, and deletion.

## 5. Interfaces and integrations

1. Which outside services does it talk to (auth, email, payments, storage, sensors, model APIs)?
2. For each: a hosted service or self-run, the fallback, and the lock-in.
3. Which MCP servers and plugins help agents work with those services?

## 6. Testing

1. **The black box.** What surface does the user touch, and what tool drives it: a browser (Playwright), a CLI runner, an API client, a hardware-in-the-loop rig or simulator, an evaluation set?
2. Where do black-box tests run: a local build, a per-branch preview, a device?
3. **Integration tests.** Which boundaries need them: storage, outside services, hardware drivers, model inference?
4. Which properties no black-box test can observe, if any, deserve a unit test (determinism, numerical accuracy)?
5. What can agents not judge (look, sound, feel, model quality), and how does the CEO review it?

## 7. Tooling and agents

1. Linters and formatters per language, and whether simple-code needs a language pack.
2. The import-boundary tool for the architecture check.
3. Which engineer agents the project needs, one per major part.
4. Package manager, lockfiles, and pinned versions.

## 8. Operations

1. **CEO.** Name, domain, and which accounts the project lives under.
2. Environments: local, preview per branch, production; or build artifacts and releases.
3. How it deploys or ships: CI/CD, app stores, firmware updates, model registry.
4. Secrets: where they live and how agents set them without seeing them.
5. Observability: logs, errors, metrics, alerts.
6. **CEO.** Merge policy: what merges when green, and what waits for the CEO.
7. **CEO.** Public or private repository, and when that changes.

## 9. Money and legal

1. **CEO.** Pricing model, if any: free, subscription, one-time, usage.
2. **CEO.** Payment provider, or a merchant of record.
3. **CEO.** Licenses for dependencies, assets, models, and the output users make.
4. **CEO.** Terms, privacy, and any regulated data.
