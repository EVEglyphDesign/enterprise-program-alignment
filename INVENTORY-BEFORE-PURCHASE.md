# Inventory before purchase

The standard applied to strategy planning and forecasting on every enterprise program. Recommending a third-party AI or data purchase before the client's existing estate has been documented and fairly tested is a program defect, not a procurement one — every unplanned licence adds a new consumption protocol to draft, a new signal to reconcile, and adoption drag the program will pay for later. This document is what "Inventory first" refers to on the public surface.

## Why this is a program discipline, not a procurement one

Most enterprise clients already own more AI, data, and workflow capability than an incoming program realises. When strategy or forecasting rushes to a third-party recommendation:

- Context leaves the client's approved surfaces.
- A new trade-secret consumption protocol has to be drafted for the new tool.
- The client-held adoption signal now has to reconcile two sources instead of one.
- Renewal budgets absorb a cost that was never tested against the surfaces the client already pays for.

Doing the inventory first is cheaper than doing it after the invoice, and it is what makes forecasts defensible.

## The existing estate to inventory

Not exhaustive, but the categories that recur across enterprise clients:

- **Microsoft** — Microsoft 365, Teams, SharePoint, OneDrive, Microsoft 365 Copilot (including Copilot agents), Power Platform (Power Automate, Power Apps, Power BI, Copilot Studio), Purview, Azure AI Foundry, Fabric, Entra ID.
- **SAP** — Joule, SAP Build (including Build Code and Build Process Automation), SAP Datasphere, SAP Analytics Cloud, BTP-hosted services, existing extension frameworks.
- **Data & governance** — existing data warehouse or lakehouse, catalog and lineage tooling, DLP, records management.
- **Collaboration & workflow** — existing ticketing, project, knowledge, and intranet surfaces.
- **AI surfaces already licensed** — Claude for Work, ChatGPT Enterprise, Perplexity Enterprise, previously licensed agent frameworks (LangChain, LangGraph, LangFuse), any Foundry- or MCP-connected agents.
- **Under-used but licensed** — the surfaces the client is paying for and not using. These are the highest-leverage entries in the inventory.

## The five standards

### 1. Documented existing-tool inventory

Before any strategy or forecast recommends a purchase, the program produces a written inventory covering, per capability:

- **Surface and edition** — the specific tool and licence tier in play.
- **Owner** — business owner and security owner.
- **Licence status** — active, dormant, expiring, renewal date, seat utilisation.
- **Integration points** — what it already connects to inside the client's estate.
- **Governance status** — what the client's legal and security teams have already approved it for.

The inventory is a living document, not a slide.

### 2. Fit test against existing surfaces first

Each proposed workstream capability is tested against the existing inventory using a small, timeboxed proof — a fair test with a documented result, not a slide claim. Only capabilities that fail a fair test on existing surfaces move to a third-party proposal. A "fair test" means:

- The existing surface is configured competently for the task.
- Any refined trade-secret records the test needs are available.
- The test is scoped to a real program workflow, not a demo.
- The result is recorded — pass, partial, or fail, with evidence.

### 3. Documented gap and defensible increment

A third-party proposal names, in one document:

- The **specific gap** the existing estate cannot meet.
- The **surfaces tested** and the test results.
- The **trade-secret refinement** and **consumption protocol** the new surface would need.
- The **incremental value** against the existing renewal budget — not against a green field.
- The **exit criteria** if the incremental value does not materialise.

"Nice-to-have" purchases fail this standard by construction.

### 4. Forecasting reflects the existing estate

Program forecasts and business cases start from the existing capability baseline and existing renewal spend. When new tooling is proposed, the forecast includes:

- Licence cost.
- Integration cost.
- Trade-secret refinement cost.
- Adoption cost (protocol drafting, baseline, fitness cadence, named owners).
- Reconciliation cost against the client-held signal.

Presenting only the licence line is a defect.

### 5. Named-owner accountability for the inventory

The inventory has:

- A **business owner** accountable for accuracy.
- A **security owner** accountable for the governance status column.
- A **review owner** accountable for keeping the fit-test evidence current.

The inventory is refreshed on the same six-week fitness cadence as trade-secret refinement and adoption — so strategy and procurement never run against a stale picture.

## Deliverable checklist

Before a third-party AI or data purchase is proposed to the client:

- [ ] Existing-tool inventory current within the last six weeks
- [ ] Fair fit test recorded on the closest existing surface(s)
- [ ] Gap document naming what the existing estate cannot meet
- [ ] Consumption protocol drafted for the new surface (see [`TRADE-SECRET-REFINEMENT.md`](./TRADE-SECRET-REFINEMENT.md))
- [ ] Business case includes integration, refinement, and adoption cost
- [ ] Named owners for the new surface identified before purchase

## What this replaces

- Third-party recommendations made from a demo, not from a test.
- Business cases built on the licence line alone.
- Forecasts that assume the existing estate is empty.
- Purchases proposed before the client's own governance status on the new surface is known.
- Procurement carrying the reasoning that should have lived in program strategy.

---

Cross-references: [`./DECISIONS.md`](./DECISIONS.md) items 9, 10, 13, 14, 15 · [`./TRADE-SECRET-REFINEMENT.md`](./TRADE-SECRET-REFINEMENT.md) · [`./MEETING-STRUCTURE.md`](./MEETING-STRUCTURE.md).
