# Approved-tool usage protocol

The standard applied to every AI surface introduced into an enterprise program. Handing a user a Claude Pro account or a Microsoft 365 Copilot licence without this protocol is a program defect. This document is what "adoption monitoring" refers to on the surface.

## Applies to

- **Claude Pro** and Claude for Work / Team / Enterprise (Anthropic)
- **Perplexity Pro** and Perplexity Enterprise
- **ChatGPT** Plus / Team / Enterprise (OpenAI)
- **Microsoft 365 Copilot** (in Teams, Word, Excel, PowerPoint, Outlook)
- Azure AI Foundry-hosted agents
- Teams applications and MCP-connected agents delivered under the program
- Any additional approved AI surface

## The five standards

### 1. Approved-tool usage protocol

Every licensed surface has a documented standard covering:

- **Permitted use** — the workstreams and task types for which it may be used on program work.
- **Prohibited use** — data classes, workstreams, or task types where it may not be used (for example, unredacted personal data, confidential negotiation, legal privilege).
- **Retrievable context** — the segments of the client-owned program playbook it may retrieve from.
- **Approval requirement** — the point at which its output requires a named-human approval before it becomes a program commitment.
- **Attribution and provenance** — how source references and review status are attached to its output.

Draft each protocol before a licence is issued, not after.

### 2. Baseline before adoption claims

Adoption is measured against the client's own prior-program baseline across four dimensions:

- **Awareness** — do the target users know the tool exists, know what it is for, and know what it is not for?
- **Confidence** — can they operate it against the documented usage protocol without external help?
- **Fit** — is it in fact the right tool for the task, versus a peer surface already licensed?
- **Habit** — is use recurring in workflow, or triggered only by prompting from management or partners?

No outcome-uplift language ("this tool saves X hours") appears in program communications without a client-held baseline to compare against.

### 3. Fitness check on a fixed cadence

Every six weeks, each workstream produces a short adoption-fitness report using the same four-dimension format. The output is a prioritized roadmap — training gaps, protocol updates, licence adjustments — not an architecture rebuild. Consistency across workstreams is what makes the aggregate readable to program leadership.

### 4. Named-owner accountability

Each approved surface has three named owners:

- **Business owner** — accountable for permitted use and adoption progress.
- **Security owner** — accountable for retrieved context boundaries and provenance controls.
- **Review owner** — accountable for the approval requirements before outputs become commitments.

Renewals require evidence of use against the protocol. Active-licence headcount is not sufficient.

### 5. Signal stays client-held

Adoption evidence — usage logs, workflow signal, outcome data — is retained in the client tenant. Vendor-hosted assistant logs may supplement, but the sovereignty gate is that the client can operate the adoption dashboard without a vendor's cooperation. This is the Byline lesson carried into every adoption engagement.

## Deliverable checklist

Before an approved tool is added to a program:

- [ ] Protocol document signed by the business, security, and review owners
- [ ] Baseline captured across the four dimensions
- [ ] Fitness-check cadence scheduled and owned
- [ ] Client-held signal collection point identified and tested
- [ ] User communications ready in the client's own channels

## What this replaces

- Ad-hoc licence distribution without documented use cases
- Training webinars presented as adoption
- Vendor-hosted usage dashboards presented as the adoption source of truth
- Outcome-uplift claims without a client baseline

---

Cross-references: [`../DECISIONS.md`](./DECISIONS.md) items 6, 10, 15, 16 · [`../RESEARCH-SOURCES.md`](./RESEARCH-SOURCES.md) rows 3, 4, 5 · [`../MEETING-STRUCTURE.md`](./MEETING-STRUCTURE.md).
