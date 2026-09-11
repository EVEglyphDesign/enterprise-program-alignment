# Working with AI surfaces — a practitioner's protocol

> **DRAFT — UNDER REVIEW. NOT ATTRIBUTED.**
> This wording has not been reviewed or approved by the practice lead. No part of it is
> canon, and no part of it is published in anyone's name, until the practitioner whose
> method it describes has read it and frozen the words. Until then it is an
> EVEglyphDesign working draft, offered for correction rather than for circulation.

Published by [EVEglyphDesign](https://eveglyphdesign.github.io/enterprise-program-alignment/) as a working draft.

A short, copyable protocol for people doing real programme work with AI surfaces — the
assistants, copilots and chat tools already sitting inside your organisation. It is written
for the practitioner, not the platform team. Take it, change the names, use it.

---

## Who this is for

You run a workstream, a stage gate, a finance close, a migration, a PMO. You have been
given an AI surface and no rules for it, or rules written for a security review rather
than for Tuesday morning. This is the working version.

It assumes nothing about which tool you use. The protocol is what makes the output usable;
the tool is interchangeable.

---

## The one rule

**The protocol decides, not the tool.**

An AI surface is a contributor. Every other contributor to a programme operates under
stated terms: what they may see, what they must show, what they may not decide, and where
they work. Give the surface the same four terms and its output can enter the record. Leave
them unstated and everything it produces has to be re-verified by hand, which costs more
than not using it.

---

## The four terms

### 1. What it may see

Decide access per task, not once per platform.

- Classify the material **at the moment you capture it**, not before you publish it. Retro-classification never happens.
- Retrieval is need-to-know. A surface that can read everything will eventually quote the one thing that should not have left the room.
- Personal data, unpublished financials, employee matters, counterparty terms and anything under NDA start outside the boundary and are only brought in deliberately.
- If you cannot say which documents a surface can reach, it is not ready to be used on programme work.

### 2. What it must show

An answer without provenance is not evidence. It is a suggestion.

Require three things on every output you intend to keep:

| Field | Why |
|---|---|
| **Source** | Which document, system or extract it came from |
| **Date** | What the position was as of when |
| **Approver** | Which named person accepted it |

If an answer cannot carry those three, it may still be useful for thinking. It does not go
into a gate paper, a specification or a decision log.

### 3. What it may not do

No commitment, no operational action, no write-back to a system of record without a named
human approval on the file.

That means: it does not send the message, post the journal, release the order, update the
master data or close the item. It drafts, it assembles, it reconciles, it flags. The last
step is a person, by name, on a date.

### 4. Where it runs

Prefer your own tenant, on your own account, under your own retention terms. Where that is
not possible, know exactly where the processing happens and what the provider retains and
trains on. If you are being charged for model processing, it should be visible and separate
— a cost you can see, not a cost folded into someone's hours.

---

## The working checklist

Before you use an AI surface on a piece of programme work, answer these in under a minute.

- [ ] What class of information does this task touch, and is that class permitted here?
- [ ] Where is the source of truth, and am I pointing the surface at it rather than at a copy?
- [ ] Will I be able to show the source, the date and the approver for what comes back?
- [ ] Which part of this is judgement, and have I kept it?
- [ ] Who approves the result, and do they know they are the approver?
- [ ] Where does the output land so the next person finds it — the record, or my laptop?

Six questions. If any answer is "I don't know", that is the finding, and it is worth more
than the task you were about to do.

---

## Point it at the dull work

The return is largest where programmes reliably lose weeks, and smallest where judgement
is the actual work.

**Good targets**

- **Reconstruction** — rebuilding a current-state position from material the organisation already holds, instead of interviewing it back into existence.
- **Reconciliation** — testing definitions, ledgers and process descriptions against each other at full volume rather than by sample.
- **Fit and gap** — scoring what is already owned against what is being proposed, before anything is bought.
- **Evidence assembly** — drafting gate papers, specifications and test evidence from the approved record, ready for human review rather than human assembly.

**Poor targets**

- Deciding scope, priority or risk acceptance.
- Anything where the value is that a specific accountable person thought about it.
- Anything you cannot check. If you would not be able to tell that the answer was wrong, do not use the answer.

---

## What must not change

Acceleration is only credible if the gates it feeds are unchanged.

- **Decision rights stay with named accountable people.** Scope, priority, risk acceptance and benefit claims are theirs.
- **The gate still gates.** A phase closes on reviewed evidence and named approval, at the same standard as before.
- **Custody stays with the organisation.** The decision record, the definitions and the evidence remain yours and remain portable.
- **Accountability is human.** No approval, no commitment and no operational instruction is ever attributed to a tool.

---

## Then the harder half: adoption

Most AI programmes are declared delivered and quietly unused. Four questions tell you the
truth faster than any usage dashboard:

1. **Do the intended users know it exists?** Named people, in named roles, told plainly what it answers.
2. **Do they trust the answer?** Provenance is what earns this. Nothing else does.
3. **Is it useful for real work?** It has to beat the current habit — the shared drive, the side spreadsheet, the person who always knows.
4. **Do they come back unprompted?** Return use without a reminder is the one signal that cannot be staged.

When the answer is no, diagnose it with the people who did not use it. More training and a
louder announcement is not a diagnosis. Retire what nobody reuses rather than reprinting it
each phase, and give every adoption gap a named owner and a date, like any other risk.

---

## A protocol block you can paste

Drop this into your team charter, your programme handbook or the README of your own
repository, and fill in the four blanks.

```text
AI SURFACE PROTOCOL — <team or programme>

May see:      <classes of information permitted, and the boundary they sit in>
Must show:    source, date and named approver on any output entering the record
May not do:   commit, act operationally, or write back to a system of record
              without a named human approval on the file
Runs in:      <tenant / account / region, and who holds the retention terms>

Accountable approver: <name, role>
Reviewed:             <date>  ·  Next review: <date>
```

Review it on a date, not on an incident.

---

## Why this is short

A protocol nobody reads is a protocol nobody follows. This one fits on two pages on
purpose. If it needs an exception, write the exception down and date it — that is how the
protocol stays honest, and how the next person understands why you did it that way.

---

*Draft for review. Not for circulation, and not attributed, until the wording is frozen.*
*Background and the fuller programme model: [Enterprise Program Alignment](https://eveglyphdesign.github.io/enterprise-program-alignment/).*
