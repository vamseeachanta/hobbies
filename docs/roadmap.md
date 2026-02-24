# Hobbies Repo — Roadmap

**Last updated**: 2026-02-24
**Status**: Approved (WRK-041)
**Spec**: `workspace-hub/specs/modules/hobbies-long-term-plan.md`

---

## Vision

A clean, browsable family knowledge base that captures practical gardening wisdom, sports training
notes, arts and cultural references, and personal-development content — with zero software or
agent-framework scaffolding.

---

## Phase 1 — Security and Cleanup (target: 2026-03-31)

Priority: high. Execute in one focused session.

- [ ] Redact credentials from `sports/soccer/soccer.md`
- [ ] Remove `.agent-os/`, `.claude/agents/`, `.claude/commands/`
- [ ] Remove `agents/`, `coordination/`, `modules/`, `scripts/`, `src/`, `tests/`, `htmlcov/`
- [ ] Remove root Python scripts, `pyproject.toml`, `uv.toml`, `Makefile`
- [ ] Remove agent-doc files at repo root (`AGENT_OS_COMMANDS.md`, `MANDATORY_SLASH_COMMAND_ECOSYSTEM.md`, `COMMANDS.md`, `AGENTS.md`)
- [ ] Remove `data/`, `reports/`, `memory/`, `.benchmarks/`, `.drcode/`, `agos`, `slash/`
- [ ] Remove scaffolding from `docs/` (`AI_AGENT_ORCHESTRATION.md`, `HTML_REPORTING_STANDARDS.md`, `api/`, `guides/`, `modules/`)
- [ ] Replace `.claude/CLAUDE.md` 500-line software ruleset with 20-line PKM context

---

## Phase 2 — Identity and Structure (target: 2026-03-31)

Execute immediately after Phase 1.

- [ ] Rewrite `README.md` with purpose statement and category index
- [ ] Create `docs/repo-audit.md` (this audit — done 2026-02-24)
- [ ] Decide fate of `sports/waterpolo/` (empty; recommend remove)
- [ ] Commit `docs/roadmap.md` (this file)

---

## Phase 3 — Active Category Content (target: 2026-05-31)

Triggered by season: swim season (May-August) and garden season (March-June) are natural entry
points.

### Gardening

- [ ] Add growing guides to `fruit_mango.md` (Houston Zone 9a, container/ground notes)
- [ ] Complete `veg_drumstick.md` growing section
- [ ] Create `gardening/seasonal-calendar.md` — monthly Houston gardening tasks

### Swimming

- [ ] Update `swimmers/bar.md`, `swimmers/dpt.md`, `swimmers/kanna.md` with 2025/2026 season data
- [ ] Create `swimming/competition-schedule.md` — Village Piranhas meet format
- [ ] Expand `freestyle.md` with technique notes (not just links)
- [ ] Create `swimming/stroke-reference.md` — backstroke, breaststroke, butterfly basics
- [ ] Expand `training.md` from URL stub to structured progression guide

### Autism Resources

- [ ] Create `autism/README.md` — resource index by type
- [ ] Create `autism/iep-tracker.md` — IEP goal template by school year
- [ ] Create `autism/community-resources.md` — Houston therapy and community programs
- [ ] Create `autism/sports-inclusion.md` — aggregate Aceing Autism and other sports links

---

## Phase 4 — Secondary Category Content (target: ongoing)

Execute on an as-needed basis, not on a deadline.

### Soccer

- [ ] Sanitise `soccer.md` post-Phase 1 and add general team/league reference
- [ ] Create `soccer/training-drills.md` — youth player drill reference
- [ ] Create `soccer/league-guide.md` — FFPS structure and season calendar

### Cultural

- [ ] Expand `bala_vihar.md` from 2-line stub (curriculum, events, contacts)
- [ ] Create `cultural/arya-samaj.md`
- [ ] Create `cultural/festivals.md` — family Hindu festival calendar

### Arts / Music

- [ ] Create `arts-music/carnatic-basics.md` — key concepts from theory PDFs
- [ ] Create `arts-music/tuition-log.md` — lesson and practice log

### Volleyball

- [ ] Create `volleyball/mission_impassibles/README.md` — team overview and roster format
- [ ] Create `volleyball/rules-reference.md` — recreational volleyball rules

### Personal Development

- [ ] Decide if `sdev/` stays here or moves to a separate repo; rename to `personal-dev/` if kept
- [ ] Create `personal-dev/reading-list.md` — books referenced in PDFs with brief notes
- [ ] Create `personal-dev/practices.md` — aggregate visualization, golden rules, growth notes

---

## Phase 5 — Long-Term Options (deferred, no date)

Revisit only if daily-use patterns justify investment:

- [ ] Evaluate static site generation (Jekyll / Hugo) for family browsing
- [ ] Evaluate GitHub Pages deployment
- [ ] Evaluate splitting `autism/` into a dedicated repository
- [ ] Add `index.md` aggregating all category landing pages

---

## Category Health Targets

| Category | Current | Target (Phase 3+) |
|----------|---------|-------------------|
| gardening | Fair | Good — growing guides + seasonal calendar |
| swimming | Good | Very good — full technique + current logs |
| soccer | Poor | Fair — sanitised + drills reference |
| cycling | Poor | Fair — at least one markdown summary |
| tennis | Poor | Fair — aggregate autism-sports content |
| volleyball | Fair | Good — team README + rules reference |
| waterpolo | Poor | Remove if no activity |
| arts-music | Poor | Fair — carnatic basics + tuition log |
| autism | Poor | Good — IEP tracker + community resources |
| cultural | Poor | Good — expanded Bala Vihar + festivals |
| personal-dev | Fair | Good — reading list + practices aggregated |

---

## Routing Note

Per WRK-041: low strategic value; deprioritised. Phases 1 and 2 are the minimum viable
deliverable. Phases 3 and 4 are opportunistic. Phase 5 is deferred indefinitely.
