# Figma Design Harness — Claude Code

A **deterministic design** harness for Figma: an explicit, auditable, and repeatable
process for building screens and design systems in Figma using Claude Code + specialized
subagents, connected to Figma via MCP. Nothing is built without a human-approved plan;
no design decision is left implicit.

---

## What this project is (and the problem it solves)

Real-world design systems accumulate inconsistency over time: duplicated components,
loose naming conventions, tokens used differently in similar places. When you try to
automate screen creation with AI on top of such a foundation, two risks emerge:

1. **Component hallucination** — the model "thinks" an element is similar enough to
   another and reuses it incorrectly, or creates a new component when an equivalent
   already existed.
2. **Loss of coherence across screens** — in a multi-screen journey, each screen may
   solve the same type of element differently because there is no memory between builds.

This harness addresses this with four principles:

- **Separation of decision vs. execution** — whoever decides what to build (planning
  agents, read-only) is never the one who builds it (execution agents, write to Figma).
  Between the two, there is always a human approval checkpoint.
- **Mandatory classification before building** — every wireframe element is classified
  as DIRECT REUSE / NEW VARIANT / NEW COMPONENT / MIGRATE FROM LEGACY, with discarded
  candidates listed in the plan. This is what prevents silent duplication.
- **Immutable legacy** — each client has two Figma files: the **Legacy** (old, messy,
  read-only, used as reference) and the **Production** file (new, clean, the only
  write destination). No agent ever writes to the Legacy file.
- **Memory in versioned files** — decisions, learnings, and design system state live
  in `.md` files in the repository, not in the "memory" of a conversation. Every
  correction today becomes a rule that prevents the same mistake tomorrow.

Read `arquitetura-harness-figma.md` for the complete reasoning behind each design
decision. This README is the operational guide; the universal process rules are in
`CLAUDE.md`.

---

## Use cases — "I'm in this situation, which module do I use?"

| Situation | Module / path |
|---|---|
| New client arrived with a messy legacy Figma, never mapped | **Onboarding** (Flow 1) — once per client |
| I'm designing a new journey/screen from a wireframe + user story | **Production** (Flow 3) — the day-to-day cycle |
| The new screen needs a component that only exists in the legacy file | **Preflight** (Flow 2) — triggered by the interpreter plan (`MIGRATE FROM LEGACY`), before building |
| I want to proactively migrate priority legacy components without waiting for demand | Manual **Preflight**, from `migration-backlog.md` |
| A new journey involves rebuilding a screen that already exists in the legacy (e.g., the Home screen) | **Production** with a screenshot of the legacy screen as wireframe — see `migration/MIGRATION.md` |
| I suspect someone on the client's team edited Figma outside the harness | **`auditor`** — sync check (recommended at the start of every session) |
| I serve multiple clients on the same corporate Figma account | One directory per client in `projects/`, with `PROJECT.md` declaring the files — isolation is by configuration |

---

## The three modules and their 10 agents

The harness is divided into three modules (scopes) with different cadences and risk
profiles. Each module has its own agents, and all follow the same rule: **no agent
triggers another** — coordination always passes through the main session (you + Claude
in the root conversation), which decides when to delegate and when to request human
approval.

### Module 1 — Onboarding (once per client · read-only in Figma)

Maps an unknown legacy Figma file and transforms it into documentation that the other
modules can reference. Runs at the start of each new client (or, rarely, on a re-scan
if the legacy has changed significantly).

| Agent | When it runs | What it does | Never does |
|---|---|---|---|
| `onboard-scanner` | 1st — legacy never mapped | Scans the Legacy file in two passes (cheap visual → surgical structural) and produces the raw inventory | Judge, decide, write to Figma |
| `onboard-analyst` | 2nd — inventory ready | Cross-references the inventory, identifies suspected duplicates/inconsistencies, and formulates objective questions for the human | Decide on its own |
| `onboard-writer` | 3rd — all questions answered | Generates `design-system/tokens/*.md`, `components/*.md` (`Status: under review`), `design.md` (visual identity) + `migration-backlog.md` | Write to Figma; run with pending questions |

Between the analyst and the writer there is a mandatory human step: negotiating the
questions one at a time, recorded in `onboarding-decisions.md`.

### Module 2 — Preflight (on demand, incremental · writes to the Production file)

Migrates components from the legacy to the Production file, **one at a time, when a
real demand requires them** — never in batch (big-bang). It is also the module where
the Production file is created on the first run for a client (the FILE itself is created
manually — the agent creates the page structure). "Migrate" here means **rebuilding
from scratch** following `COMPONENT_STANDARDS.md`, using the legacy only as a visual
reference — never copying the problematic structure.

| Agent | When it runs | What it does | Never does |
|---|---|---|---|
| `preflight-planner` | Element marked `MIGRATE FROM LEGACY`, or manual backlog prioritization | Reads the component in the Legacy and proposes the reconstruction, highlighting visual drift risks for approval | Reconstruct, write to Figma |
| `preflight-builder` | Reconstruction plan approved | Rebuilds in the Production file (creates the page structure on the client's 1st run; the only agent that creates variables/tokens) | Write to Legacy; decide to migrate something outside what was approved |

After reconstruction, the `documenter` (from the Production module) promotes the
component: `Status: under review` → `Status: active`.

### Module 3 — Production (day to day · writes to the Production file)

The recurring cycle: transforming wireframe + user story into screens built in Figma,
with components reused or created in a controlled way.

| Agent | When it runs | What it does | Never does |
|---|---|---|---|
| `interpreter` | Start of every new journey/screen | Reads wireframe + user story + design system and proposes the plan, classifying each element (reuse/variant/new/migrate) with discarded candidates visible | Write to Figma; decide alone in ambiguity |
| `builder` | Plan approved, one invocation per screen | Executes the plan exactly via MCP; receives the updated `journey-state.md` to maintain coherence across screens | Reinterpret the plan; continue after partial failure; write to harness files |
| `validator` | ALL screens in the journey are ready | Compares the result against the user story, the wireframe, cross-screen coherence, and the visual identity (`design.md`); generates `validation-report.md` (uses Opus — fine semantic judgment) | Correct or modify anything |
| `documenter` | Journey approved by validator + human | Promotes `_draft/` components → official and approved frames → "Current Screens" page; registers new tokens | Document/promote before validation |
| `auditor` | Start of each work session (or under suspicion) | Checks technical consistency of the Production file against the documented `design-system/`: hardcoded values, naming, duplicates, token drift | Auto-correct |

The production flow order is fixed and exists for a reason: the `documenter` comes last
because formalizing a component before semantic validation would propagate an
interpretation error to all future journeys.

```
interpreter → [human approval] → (preflight, if needed) →
builder (per screen) → validator (full journey) →
[human approval] → documenter
```

---

## Repository structure

```
figma-harness/
├── CLAUDE.md                   # universal rules — read first
├── arquitetura-harness-figma.md # the "why" behind each design decision
├── onboarding/ONBOARDING.md    # onboarding module process
├── preflight/PREFLIGHT.md      # preflight module process
├── migration/MIGRATION.md      # light variation: migrate a legacy screen
├── mcp-figma/plugin/           # LEGACY: figma-mcp-go plugin
│   │                           (previous MCP — remove after 1st
│   │                            real journey on the new server)
├── .claude/agents/             # the 10 subagents
│   ├── interpreter.md / builder.md / documenter.md / auditor.md /
│   │   validator.md                                  → production
│   ├── onboard-scanner.md / onboard-analyst.md /
│   │   onboard-writer.md                             → onboarding
│   └── preflight-planner.md / preflight-builder.md   → preflight
├── skills/                     # reusable procedures
└── projects/
    └── [client-name]/          # one directory per client/project
        ├── PROJECT.md          # Legacy and Production file keys
        ├── design-system/      # documented tokens + components
        ├── memory/             # decisions, learnings, changelog
        └── journeys/           # one folder per built journey
```

Everything that is **engine** (rules, agents, skills) is shared across clients;
everything that is **content** (design system, memory, journeys) is isolated inside
`projects/[client]/` and never leaks to another client.

See `projects/_EXAMPLE_CLIENT/` as a template for creating a new project, and
`projects/_SANDBOX_TEST/` as a pre-filled fixture (10-agent smoke test) for reference.

---

## Initial setup (once per machine/installation)

### 1. Figma Personal Access Token

Create a token in Figma → Settings → Security → Personal access tokens
(suggested description: `Figma Console MCP`), with the scopes: **File
content (Read)**, **File versions (Read)**, **Variables (Read)**,
**Comments (Read/write)**. The token (`figd_...`) only powers **READ**
via REST — writes on the canvas go through the bridge plugin, which is why
scopes are read-only. Copy it immediately: it won't be shown again. The
`.env.example` serves as reference for other integrations; **never** commit
`.env` or the token.

### 2. Connect the Figma MCP — `figma-console-mcp`

This harness uses https://github.com/southleft/figma-console-mcp
(replaced `figma-mcp-go` on 2026-07-11, after a complete smoke test —
see `smoke-test-figma-console-mcp.md`). Hybrid architecture:
**read via REST** by `fileUrl`/`fileKey`, without Figma Desktop — this is
how the Legacy file is read, without ever receiving the plugin — and
**write via Desktop Bridge plugin** running on the target file.

```bash
claude mcp add figma-console -s user \
  -e FIGMA_ACCESS_TOKEN=figd_YOUR_TOKEN_HERE \
  -e ENABLE_MCP_APPS=true \
  -- npx -y figma-console-mcp@latest
```

> ⚡ **Scope `-s user` (or `-s local`), NEVER `-s project`** — the
> registration carries the token, and `-s project` would write to `.mcp.json`,
> which is versioned. Consequence: each new machine needs to re-run this
> command; nothing in the repository restores the registration.

The first check (`claude mcp list`) may fail while `npx` downloads the
package — once cached, it shows `figma-console ... ✔ Connected`.

**Desktop Bridge Plugin (required for WRITE; read does not require it):**
1. The server materializes the plugin at
   `~/.figma-console-mcp/plugin/manifest.json` on the first run
2. Figma Desktop: **Plugins → Development → Import plugin from
   manifest** → point to that file
3. Open the **Production** file and run the plugin (**Plugins →
   Development → Figma Desktop Bridge**) — it connects automatically via
   WebSocket (ports 9223–9232). Development plugins need to be run at
   the start of each work session
4. **NEVER run the plugin on the Legacy file** — the absence of the bridge
   is what makes writing to the Legacy architecturally impossible (see
   `CLAUDE.md`, security rule)
5. Figma Desktop: official build for Windows (current environment, native)
   and macOS. On Linux, only write requires a workaround (VM/Wine) — read
   via REST works on any OS

**Troubleshooting — "Can't call X in read-only mode":** the Figma tab is in
**Dev Mode** (icon `</>`, shortcut `Shift+D`) — the Plugin API blocks writes
in that state, for any plugin. Switch to Design mode.

The confirmed capabilities and quirks of the server (timeout ≠ failure, token
sync, reading Auto Layout via `figma_execute`, etc.) are in `CLAUDE.md`,
section "MCP Connection with Figma". The 10 agents use the prefix
`mcp__figma-console__*`, migrated based on the smoke test in
`projects/_SANDBOX_TEST/`. What still has `[FILL IN]`/`[VALIDATE]` markers
is what is inherently per-client: the `PROJECT.md` of each new project (copied
from `_EXAMPLE_CLIENT`) and some points listed under "Out of scope" below.

> Transition note: the previous server (`figma-mcp-go`) remains registered in
> `.mcp.json`, and its vendored plugin in `mcp-figma/plugin/`, only as a
> fallback — no agent uses it anymore. Remove both once the first real journey
> completes on the new server.

### 3. Create a new project/client

```bash
cp -r projects/_EXAMPLE_CLIENT projects/client-name
```

Fill in, in this order:
1. `projects/client-name/PROJECT.md` — at minimum the **File-key** of the
   Legacy (just the file link — the key is in the URL). This is what the
   agents use to read the Legacy via REST and what the security rule uses to
   verify the write target. The Production block stays empty until the file
   is created in the first preflight (file creation is manual — the agent
   only creates the page structure)
2. Run onboarding (see below) before any production work

---

## Flow 1 — Onboarding (once per client)

```
"Use the onboard-scanner on the client-name project"
  → generates onboarding-inventory.md

"Use the onboard-analyst"
  → generates onboarding-questions.md

[ answer the questions, one at a time ]
  → answers become onboarding-decisions.md

"Use the onboard-writer"
  → generates design-system/tokens/*.md, components/*.md
    (Status: under review), design.md (project visual identity)
    + migration-backlog.md
```

Details: `onboarding/ONBOARDING.md`

## Flow 2 — Preflight (on demand, incremental)

Normally triggered automatically by the production flow (below), when the
`interpreter` marks an element as `MIGRATE FROM LEGACY`. Can also be run
manually from `migration-backlog.md`:

```
"Use the preflight-planner for the Button/Primary component"
  → proposes reconstruction plan

[ human approval ]

"Use the preflight-builder with the approved plan"
  → rebuilds in the Production file (on the 1st run: you create the file
    manually and run the plugin on it; the agent creates the pages)

"Use the documenter to promote Button/Primary"
  → Status: under review → active
```

Details: `preflight/PREFLIGHT.md`

## Flow 3 — Production (day to day)

1. Create `projects/client-name/journeys/journey-name/`
2. `user-story.md` with the user story (template included)
3. `wireframe/` with images exported from Miro (or a screenshot of a legacy
   screen, if it's a migration — see `migration/MIGRATION.md`)

```
"Use the interpreter for the journey-name journey"
  → plan with per-element classification: DIRECT REUSE / NEW
    VARIANT / NEW COMPONENT / MIGRATE FROM LEGACY

[ human approval ]

[ if MIGRATE FROM LEGACY: run Flow 2 for those items before proceeding ]

"Use the builder to build screen 1"
  → repeat per screen; builder receives the updated journey-state.md
    at each new screen (update is the main session's responsibility,
    not the builder's)

"Use the validator to validate the full journey"
  → generates journeys/journey-name/validation-report.md

[ human approval ]

"Use the documenter to promote this journey's components and
screens to Current Screens"
```

Run the `auditor` periodically (recommended: at the start of each work
session on the project) to check sync with the real Production file.

Details: `CLAUDE.md`

### Wireframe format accepted today

PDF or image exported from Miro (or any tool), one per screen, in `wireframe/`.
A direct MCP connection to Miro was evaluated and consciously deferred — see
`CLAUDE.md`, section "Out of scope".

---

## Production file page structure

```
Foundations / Components / Patterns / Docs / Archive  → design system
🎯 Current Screens   → current version of each screen, always
🗂️ Journeys          → history, one page per journey
```

Components rebuilt by preflight live in **Components**.
Screens are always loose-copy duplicated frames, never a component/instance —
that is reserved for actual design system elements (Button, Card, etc.). See
`CLAUDE.md` for the complete mechanism.

---

## Points consciously left out of scope (v1)

- Automated rollback of Figma operations
- Multiple approvers / per-client approval flow
- Responsiveness / breakpoints (field provided in the template, no process yet)
- Direct MCP connection with Miro
- `[VALIDATE]` Automatic asset portability (icons, images) between the Legacy
  and Production files — confirm in practice as soon as preflight runs with
  a component that depends on an asset

If any of these becomes a real need, revisit the reasoning before implementing
— several of these decisions have trade-offs already discussed.
