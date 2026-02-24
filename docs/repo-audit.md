# Hobbies Repo — Content Audit

**Audit date**: 2026-02-24
**Auditor**: WRK-041 (claude-sonnet-4-6)
**Purpose**: Snapshot of actual content vs. scaffolding, to inform WRK-041 long-term plan.

---

## Summary

The repository contains a small core of genuine hobby content (~25 markdown files, ~42 binary
files) surrounded by a large volume of AI-agent framework scaffolding (~155 files) that adds no
value to a documentation-only repo. The scaffolding-to-content ratio is approximately 9:1 by file
count. The primary remediation goal is to remove the scaffolding entirely, leaving only the hobby
content and the minimal `.claude/` workspace-hub adapter.

---

## Actual Content — by Category

### gardening/

| File | Description | Quality |
|------|-------------|---------|
| fruit_mango.md | Picking guide for Atulfo and Haden varieties | Good — practical, specific |
| fruit_watermelon.md | Picking guide | Good — concise |
| veg_dosakai.md | Picking guide | Good — concise |
| veg_drumstick.md | Growing stub + picking placeholder | Stub — growing section incomplete |

**Gaps**: No growing guides, no seasonal calendar, no soil/zone notes.

---

### sports/swimming/

| File | Description | Quality |
|------|-------------|---------|
| freestyle.md | YouTube links for kicking and breathing | Stub — links only |
| training.md | Two URLs (USA Swimming officials, YouTube) | Stub — links only |
| healthy_practices.md | Team practice reminders (from club newsletter) | Good — practical |
| village_piranhas.md | Registration info for Village Piranhas swim club | Reference — seasonal |

**Swimmer logs** (`swimmers/`):

| File | Swimmer | Latest Data | Quality |
|------|---------|-------------|---------|
| bar.md | bar | 2023-08-08 | Active log; good structure |
| dpt.md | dpt | 2023-08-12 | Basic targets only |
| kanna.md | kanna | 2025-08-26 | Most recent (2025); includes water polo training |

**Gaps**: Technique notes absent from freestyle.md and training.md; no backstroke/breaststroke
coverage; competition schedule not documented; 2024 season data missing from most logs.

---

### sports/soccer/

| File | Description | Quality |
|------|-------------|---------|
| soccer.md | League account info | SECURITY ISSUE: contains plaintext credentials |
| literature/03. Laws of the Game (FIFA).pdf | FIFA rules | Reference |
| literature/18. Youth Football (FIFA).pdf | Youth football guide | Reference |
| literature/Football-Stories_compressed.pdf | Narrative | Reference |
| Videographer.pdf | Videographer info | Reference |

**Gaps**: No training drills, no league calendar, no narrative content. Credentials in soccer.md
must be redacted immediately.

---

### sports/cycling/

| File | Description | Quality |
|------|-------------|---------|
| specialized/2016_stumpjumper_0000051143_R3.pdf | Specialized Stumpjumper owner manual | Reference |

**Gaps**: No markdown content at all. Zero narrative or training notes.

---

### sports/tennis/

| File | Description | Quality |
|------|-------------|---------|
| acing_autism_VisualScheduleSteps.pdf | Aceing Autism visual schedule | Reference |
| Virtual Training FINAL.pptx.pdf | Virtual training PDF | Reference |

**Gaps**: No markdown content. Tennis interest is documented in sports.md but nothing is recorded
here.

---

### sports/volleyball/

| File | Description | Quality |
|------|-------------|---------|
| mission_impassibles/2025-10-06 team_members.xlsx | Team roster | Active data |
| mission_impassibles/2025-10-07 team_members.xlsx | Team roster (updated) | Active data |
| mission_impassibles/logo* | Team logo variants (PNG, SVG, PDF) | Design assets |
| mission_impassibles/_ss/ | Screenshot / design scratch files | Working files |
| mission_impassibles/logo_on_shirt.jpg | Shirt mockup | Design asset |
| mission_impassibles/new_customer_promo.png | Promo image | Design asset |

**Gaps**: No markdown content. Team assets exist but no narrative, schedule, or rules reference.

---

### sports/waterpolo/

Empty directory. No content.

---

### arts-music/

| File | Description | Quality |
|------|-------------|---------|
| theory/beginners.pdf | Carnatic music theory (beginners) | Reference |
| theory/carnatic_music_theory1.pdf | Carnatic music theory | Reference |
| tuition_2022_2023.pdf | Tuition records 2022-2023 | Records |

**Gaps**: No markdown content summarising PDFs. No practice log.

---

### autism/

| File | Description | Quality |
|------|-------------|---------|
| Medicaid Resources - English.pdf | Texas Medicaid reference | Reference |

**Gaps**: No markdown content. No IEP tracker, no community resources, no therapy log. Sports
inclusion resources (Aceing Autism links) are scattered in `sports/sports.md` and
`sports/tennis/` rather than aggregated here.

---

### cultural/

| File | Description | Quality |
|------|-------------|---------|
| bala_vihar.md | Schedule stub: "Sunday 8:30 AM; Registration at the class." | Stub |

**Gaps**: No curriculum notes, no event calendar, no instructor or contact info.

---

### sdev/ (Personal Development)

| File | Description | Quality |
|------|-------------|---------|
| 50_golden_rules.md | 50 life rules | Good content |
| visualization.md | Mental visualization link (Djokovic) | Stub — link only |
| 12_lessons_from_japan.pdf | PDF reference | Reference |
| good_reminders.pdf | PDF reference | Reference |
| growth_signs.pdf | PDF reference | Reference |
| how_to_speak.pdf | PDF reference | Reference |
| happy_inspired_motivated.jpeg | Image | Asset |
| stop_apologizing.jpeg | Image | Asset |

**Note**: Directory name `sdev/` is misleading (sounds like software development). Content is
life/personal development. Recommendation: rename to `personal-dev/` and decide if it belongs
here or in a separate repo.

---

### Root-level content files

| File | Description | Quality |
|------|-------------|---------|
| sports/sports.md | Activity overview (swimming, tennis, soccer, dance, etc.) | Active reference; family-specific |
| boy_scouts.jpeg | Boy Scouts image | Orphaned asset |

---

## Scaffolding Inventory (to remove)

| Directory / File Group | File Count (approx) | Recommendation |
|------------------------|---------------------|----------------|
| `.agent-os/` | ~55 | Remove entirely |
| `.claude/agents/` | ~65 | Remove entirely |
| `.claude/commands/` | ~30 | Remove entirely |
| `agents/` | ~9 | Remove entirely |
| `coordination/` | (empty or minimal) | Remove |
| `modules/` | (automation scripts) | Remove |
| `scripts/` | (automation scripts) | Remove |
| `src/`, `tests/`, `htmlcov/` | ~10 | Remove entirely |
| `data/`, `reports/`, `memory/`, `.benchmarks/`, `.drcode/` | varies | Remove |
| `slash/`, `agos` | 1–2 | Remove |
| Root Python scripts | 5 | Remove |
| Root config (`pyproject.toml`, `uv.toml`, `Makefile`) | 3 | Remove |
| Root agent docs (`AGENT_OS_COMMANDS.md`, etc.) | 4 | Remove |
| `docs/AI_AGENT_ORCHESTRATION.md`, `docs/HTML_REPORTING_STANDARDS.md` | 2 | Remove |
| `docs/api/`, `docs/guides/`, `docs/modules/` | ~15 | Remove |
| `.claude/CLAUDE.md` (500-line software ruleset) | 1 | Replace with 20-line PKM context |

**Estimated file reduction**: from ~222 files to ~80 files.

---

## Security Finding

`sports/soccer/soccer.md` contains plaintext credentials:
- Website username and password
- Player ID and Volunteer ID
- Email address
- Coach site credentials

**Action required (Phase 1, Task 1.1)**: Redact all credentials before next commit. Replace with
a comment directing to a password manager or `.env`-style local file excluded by `.gitignore`.
If repo history is to be sanitised, use `git filter-repo`.

---

## Next Steps

See `docs/roadmap.md` for the phased content-growth and cleanup plan.
