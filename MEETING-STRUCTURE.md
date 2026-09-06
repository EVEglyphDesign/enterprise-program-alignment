# Contribution capture & meeting structure canon

The two disciplines that make the shared context usable by both people and AI tools. This is what the "Capture every contribution once. Cover every topic every time." section on the surface refers to.

## Part 1 — Contribution capture

Every person on the program has a durable record the tools consume the same way each time. The record is client-owned and lives in the program playbook, not in a consultant's private file or a vendor-hosted contact directory.

### Record schema

| Field | Required | Notes |
|---|---|---|
| Person ID | ✓ | Stable identifier that outlives email or role changes. |
| Display name | ✓ | Preferred display, plus legal name when different. |
| Organization | ✓ | Client, consulting firm, delivery partner, external SME. |
| Role and workstream | ✓ | Multiple workstreams allowed; primary marked. |
| Named accountabilities | ✓ | Deliverables, decisions, sign-offs the person owns. |
| Preferred channel | ✓ | For follow-up: WhatsApp, Teams, email, phone. |
| Time zone | ✓ | Scheduling and briefing preparation. |
| Approved tools | ✓ | Which AI surfaces the person is licensed to use for program work. |
| Retrievable context | ✓ | The classes of program material each approved tool may retrieve on their behalf. |
| Approvals given | ✓ | Structured record of what has been approved and when. |
| Decisions authored | ✓ | Backlink to decision-register entries. |
| Evidence contributed | ✓ | Backlink to evidence-register entries. |
| Actions owned | ✓ | Open and closed, with dates. |

### Why this shape

- Any approved AI tool can prepare a briefing for or about any participant from one record, in a consistent structure.
- Handovers retain authorship and rationale — not just filenames.
- No consultant becomes a single point of institutional memory.
- The record supports the approved-tool usage protocol: retrievable context per person per tool is checkable, not vibes-based.

## Part 2 — Meeting structure canon

Meetings follow a small set of standard structures. When an attendee is missing, the structure guarantees coverage: the tools fill the gap from the shared context, and the record explicitly notes what remains open.

### Every meeting produces

1. **Pre-meeting** — purpose, agenda, expected decisions, invited participants and their contribution slots, pre-read links.
2. **Attendance and absences** — who attended, who was absent, and the topics each absentee owned. Absence never quietly drops a topic.
3. **Decisions** — decision text, rationale, evidence link, decision-register ID, named approver.
4. **Actions** — owner, due date, workstream, dependencies — in a machine-readable form the tools can pick up without re-parsing minutes.
5. **Open questions and dependencies** — with the named next forum where each will be closed.

### Standard cadences

| Cadence | Frequency | Purpose | Standard agenda beats |
|---|---|---|---|
| **Workstream** | Weekly | Keep one workstream aligned | Decisions taken · blockers · evidence updates · RAID movement · adoption signal |
| **Fit-to-standard workshop** | Per workshop | Convert business-process discussion into program decisions | Agenda pack · process decisions · gap classification · action log · traceability update |
| **Program board** | Bi-weekly | Cross-workstream alignment for sponsors | Scope · risk · budget · cross-workstream dependencies · adoption fitness aggregate |
| **Adoption fitness** | Every six weeks | Adoption-monitoring protocol review | Awareness · confidence · fit · habit — per approved tool, per workstream |
| **Hypercare stand-up** | Daily (stabilization) | Coordinate go-live issues | Command-center view · issue triage · ownership · executive briefing input |

### Coverage-when-absent rule

When a participant is absent, three things happen automatically:

1. The topics they own remain on the agenda under their name.
2. Approved tools prepare the fallback context from the shared playbook so the discussion can continue.
3. Any decision that requires the absent person's named authority is explicitly recorded as **deferred**, not silently reassigned.

This is the mechanism by which meeting structure standardization delivers "content coverage even when the specific attendees are not there."

## Machine-readable output

Every meeting record lands in the program playbook in a structured form (YAML front-matter plus prose) so that:

- Approved AI tools produce briefings, status reports, and executive summaries from the same records without re-parsing minutes.
- Handover packs are assembled from durable records rather than reconstructed from chat scrollback.
- Adoption evidence (which meetings used which tools for preparation and follow-through) accumulates as a side effect, not as an extra task.

## What this replaces

- Free-form minutes stored in individual OneDrive folders
- Decisions recorded in Teams chat and forgotten
- Actions tracked in a spreadsheet the AI cannot read consistently
- "The meeting couldn't cover X because Y wasn't there"

---

Cross-references: [`../DECISIONS.md`](./DECISIONS.md) items 11, 12 · [`../ADOPTION-PROTOCOL.md`](./ADOPTION-PROTOCOL.md).
