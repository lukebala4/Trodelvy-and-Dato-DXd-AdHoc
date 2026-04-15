# Ways of Working with an AI Coding Agent

A guide to the practices, conventions, and project structure that have emerged from building software with Claude Code (and similar AI coding agents). Drop this into a new project's `docs/` and reference it from `CLAUDE.md`.

These aren't theoretical — they come from building a production iOS app over several weeks of daily human-agent collaboration. Adapt what's useful, discard what doesn't fit.

---

## Language and tone

- **US American** throughout all code, comments, documentation, and agent communication. Set this once and enforce it — agents default to US English and will drift without a clear instruction.  
- **London timezone (Europe/London)** for all timestamps in WORKLOG.md and elsewhere. Agents default to US timezones or UTC — state your timezone explicitly in CLAUDE.md or they'll guess wrong.  
- Be direct in instructions. Agents respond better to "Do X" than "Could you maybe try X?".

---

## Structuring a project

- Use agile principles when possible  
- Create end to end working systems from an early stage, using mocks, shims, stubs. Then iterate on progressively more functional systems.  
- Look at highest risk items early on, and design spikes that can reduce uncertainty  
- Find ways to do automated testing rather than relying on human manual testing. Remember that an agent can do a lot of "manual" testing.

---

## Project documentation

### README.md

Keep a good README from day one. It's the front door for anyone (human or agent) encountering the project. It should contain:

- **What the project is** — one paragraph, plain language  
- **Prerequisites** — every tool needed, with install commands  
- **Setup** — clone, install, build, run — a fresh checkout to working app in copy-pasteable steps  
- **Environment variables** — what's needed, where to get keys, with a `.env.example` to copy  
- **Project structure** — a short directory tree with one-line descriptions

Update the README whenever the setup process changes. A stale README wastes everyone's time.

### CLAUDE.md (agent instructions)

This is the agent's briefing document — project-specific rules that override default behaviour. It lives in the repo root (required by Claude Code). Include:

- Project overview and tech stack  
- Working rules (language, package manager, testing approach, commit style)  
- Key constraints and known limitations  
- File structure overview  
- Anything the agent repeatedly gets wrong — add a rule for it

Think of it as onboarding notes for a new team member who is extremely capable but has no context. Be explicit about things a human colleague would "just know".

### architecture.md

A living design document in `docs/`. Covers:

- The user flow (what the app does, screen by screen)  
- Technical strategy and key decisions (why this approach, not that one)  
- System boundaries and constraints

Write it before you start building and update it as the design evolves. The agent reads this to understand *why* things are the way they are, not just *what* they are.

### roadmap.md

A task list in `docs/` with clear status markers:

\> Status: \[\~\] \= In Progress | \[ \] \= Pending | \[x\] \= Completed | \[\!\] \= Blocked

Rules:

- **Never do work that isn't tracked in the roadmap** — add a task first if needed  
- Mark tasks `[~]` when starting, `[x]` when done  
- Group tasks into phases. When a phase is complete, archive the detail to a `roadmap-history.md` and replace it with a one-line summary  
- The roadmap is the single source of truth for what's been done, what's in progress, and what's next

This prevents the agent from going off-piste and gives you an audit trail.

### WORKLOG.md

A timestamped running log of major activities, decisions, and investigation results. This is the most important document for multi-session work.

**Why it exists:** Chat context compacts. Findings, decisions, and dead ends from previous sessions are lost unless you write them down. The worklog is the agent's long-term memory.

Format:

\#\# YYYY-MM-DD (session N — brief theme)

\- \*\*HH:MM\*\* — What happened, what was decided, why

\- \*\*HH:MM\*\* — Investigation result: X doesn't work because Y, chose Z instead

Rules:

- **Always update WORKLOG.md** when: completing a significant task, reaching a decision (especially with non-obvious rationale), or finishing an investigation  
- **Consult WORKLOG.md at the start of every session** before doing anything else  
- Entries are summary form — enough to reconstruct context, not a transcript  
- Commit and push worklog updates freely — they are always safe to push

---

## Repository organisation

Keep the root clean. Only these belong at the top level:

- `README.md`, `CLAUDE.md`, `WORKLOG.md`  
- Package manager config (`package.json`, lockfile, etc.)  
- Tool config files that must live in root (`.eslintrc`, `tsconfig.json`, etc.)

Everything else goes in directories with clear purpose. The specifics depend on the project, but some directories should always exist:

- **`docs/`** — all documentation: architecture, roadmap, roadmap history, spikes, design specs. This is non-negotiable; don't scatter markdown files across the repo  
- **`scripts/`** — build and utility scripts, organised into subdirectories by purpose as they grow (e.g. `scripts/data/`, `scripts/audio/`)  
- **`__tests__/` or equivalent** — test files, matching your framework's conventions  
- **`assets/`** — static resources (images, fonts, fixtures, data files)  
- **`e2e/`** — end-to-end test flows (if applicable)

Beyond these, organise source code however suits the framework (e.g. `src/`, `app/`, `components/`, `services/`). The key principle is: a new person should be able to guess where a file lives without being told.

When the repo grows, do a periodic tidyup. It's worth writing a spike document honestly critiquing the current structure before reorganising — it forces you to think about *why* things are where they are, not just shuffle files around.

### Multi-agent pattern

If you use multiple specialist agents (e.g. a UX design agent alongside the main engineering agent), organise by topic for humans, not by agent. Each agent's working files (briefs, task trackers) should be clearly labelled as agent metadata (e.g. `AGENT-BRIEF.md`, `design-roadmap.md`), but filed alongside the deliverables they relate to.

---

## Git and GitHub

### Repository visibility

**Always create private repos** unless explicitly asked to make it public. Default to private — it's easy to make something public later, impossible to undo a leak.

### Commits

- **Atomic commits** with descriptive messages as work progresses  
- Use [conventional commit](https://www.conventionalcommits.org/) style: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `perf:`, `chore:`  
- Commit message should explain *why*, not just *what* — the diff shows the what  
- Commit frequently. Small, focused commits are easier to review and revert  
- The agent should commit documentation updates (worklog, roadmap) without asking — these are always safe

### Branching

For most solo/small-team agent-assisted work, **developing on main is fine** — the agent commits frequently with good messages, and you can always revert. Don't add process overhead that doesn't earn its keep.

Use feature branches when:

- The change is risky or experimental and you might want to abandon it  
- Multiple people are working on the repo concurrently  
- You want a PR review before merging

When you do use PRs, keep them focused with a clear description and test plan.

### Large files

- Use **Git LFS** for ML models, large binaries, and anything over a few MB  
- Add LFS tracking patterns early — retrofitting is painful  
- Remember that CI/CD systems clone from git, so anything gitignored won't be in remote builds (this has bitten us: model files were gitignored and the production build had no ML model)

### Tags and releases

If the project produces something deployable (an app, a service, a package):

- Tag releases with semver: `v0.1.0-build.9`  
- Show version and build number somewhere visible to users (e.g. settings footer, CLI `--version`)  
- Document the full build-to-release pipeline in `docs/building-and-releasing.md`

For libraries, scripts, or exploratory projects, this may not apply — use your judgement.

---

## Testing

### Red-green TDD

Write a failing test first, confirm it fails meaningfully, then implement. This isn't a suggestion — it's the working method.

1. Write the test. Run it. Confirm it fails for the *right reason* (not a syntax error or import failure)  
2. Write the minimum code to make it pass  
3. Refactor if needed, re-run tests

This discipline catches misunderstandings early and produces code that's testable by design.

### Test layers

Structure tests in layers:

| Layer | What | Tool | Runs on |
| :---- | :---- | :---- | :---- |
| Unit / component | Logic, hooks, UI components | Jest \+ testing library | Node (CI-friendly) |
| E2E / UI | User flows, screen transitions | Maestro (or similar) | Simulator / device |
| Native / integration | Platform-specific features | XCTest (or platform equivalent) | Real device |

**Never use screenshots, AppleScript, coordinate clicking, or screen capture to test UI.** These approaches are brittle, require macOS permissions, and rely on coordinate guessing. Use proper UI testing tools that work through the accessibility layer.

### Coverage

- Set a coverage floor (e.g. 75%) but don't chase 100%  
- Coverage gaps should be in the right places: native glue code, SDK initialisation, thin UI chrome  
- Prioritise testing business logic, hooks, and services

---

## Spikes (investigations)

When you hit a question that needs investigation before you can commit to an approach, write a spike document in `docs/spikes/`.

A spike is a time-boxed investigation with a written deliverable. Format:

\# Spike: \[Title\]

\> Created: YYYY-MM-DD

\> Status: Planning | In Progress | Decided | Implemented

\#\# Problem

What question are we trying to answer? What's wrong with the current state?

\#\# Options considered

| Option | Pros | Cons |

|--------|------|------|

\#\# Decision

What we chose and why.

\#\# Implementation notes

Anything the implementer needs to know.

Spikes are valuable because:

- They force structured thinking before coding  
- They document *why* a decision was made, not just *what*  
- Future sessions can read the spike instead of re-investigating  
- They prevent the agent from jumping straight to implementation on ambiguous problems

Log the spike outcome in WORKLOG.md as well.

---

## Scripting and tooling

### Python for scripts

Use Python for build scripts, data processing, and utility tooling. It's readable, well-supported by agents, and handles data manipulation well.

- **Use `uv`** for all Python dependency management — never `pip install` globally  
- `uv run --with <package> script.py` for one-off runs  
- Keep scripts organised by purpose: `scripts/audio/`, `scripts/data/`, `scripts/models/`  
- Each script directory can have its own README if the scripts aren't self-explanatory

### No global installs

Never install anything globally. This applies to:

- Python packages (use `uv`, not global `pip`)  
- Node packages (use `pnpm exec` or `npx`, not global installs)  
- System tools should be documented in the README prerequisites

The reason: global installs create invisible dependencies. A fresh checkout should work with only the documented prerequisites.

### Package management

Pick one package manager and enforce it. For Node projects, specify it in CLAUDE.md and never let the agent switch. We use `pnpm` — never `npm` or `yarn`.

For packages with native components, use the framework's install command (e.g. `npx expo install` for Expo) rather than the generic package manager, to get compatible versions.

---

## Environment variables and secrets

- Provide a `.env.example` with every required variable, commented with where to get the value  
- `.env` is gitignored — never commit secrets  
- Document the dual requirement: local `.env` for development, platform-specific secrets for CI/CD builds (e.g. EAS environment variables)  
- If analytics or error reporting silently fails when env vars are missing, add a startup check or log a warning — silent failure means you don't know your production build is broken until it's too late

---

## Working with the agent effectively

### Things we've learned

1. **Be explicit about what you don't want.** Agents are eager to help and will add error handling, docstrings, refactoring, and "improvements" beyond what was asked. Set boundaries in CLAUDE.md: "Don't add features beyond what was asked. A bug fix doesn't need surrounding code cleaned up."  
     
2. **Platform-specific gotchas need documenting.** If something only works on real hardware (not the simulator), or a permission requires a restart, write it down. The agent will try the broken path every time unless told not to.  
     
3. **The agent should tell you to run builds, not run them itself** (unless you've explicitly said otherwise). Long-running commands in the agent's terminal block the conversation.  
     
4. **Archived context matters.** When a phase of work is complete, archive the detail but keep a one-line summary. The agent needs to know what was done, not re-read every task.  
     
5. **Correct the agent once, then make it a rule.** If the agent makes a mistake, don't just fix it — add a rule to CLAUDE.md so it doesn't happen again. CLAUDE.md is the accumulated wisdom of every correction.  
     
6. **Use the agent's memory system.** Feedback memories (what to do / not do), project memories (current state of ongoing work), and reference memories (where to find things in external systems) persist across sessions. Corrections should become memories.  
     
7. **Periodic repo hygiene is worth it.** After a burst of fast development, pause to review the repo structure, clean up dead files, and ensure documentation matches reality. Write a spike critiquing the current state before reorganising.  
     
8. **Multi-agent work needs coordination.** If using specialist agents (design, testing, etc.), their deliverables should be integrated into the main docs structure, not left in agent-specific directories.

---

## Checklist for a new project

- [ ] Create `README.md` with prerequisites, setup, and structure  
- [ ] Create `CLAUDE.md` with project overview, working rules, and constraints  
- [ ] Create `docs/architecture.md` with design and technical strategy  
- [ ] Create `docs/roadmap.md` with initial phases and tasks  
- [ ] Create `WORKLOG.md` with the first session entry  
- [ ] Set up `.env.example` and `.gitignore`  
- [ ] Configure Git LFS if large files are expected  
- [ ] Set up the test framework and write the first test  
- [ ] Confirm the build-from-scratch path works (clone → install → run)

