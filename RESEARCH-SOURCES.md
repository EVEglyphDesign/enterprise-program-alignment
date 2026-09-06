# Research sources — Enterprise Program Alignment CISO evidence room

Access date for all sources: **2026-09-05**. Verify each URL is current before external publication.

| # | Source | Issuer | Type | URL | Executive summary | Program implication |
|---|--------|--------|------|-----|-------------------|---------------------|
| 1 | How to Protect Trade Secrets | WIPO | Standards / guidance | [wipo.int/en/web/trade-secrets/protection](https://www.wipo.int/en/web/trade-secrets/protection) | Trade-secret protection depends on commercially valuable information staying confidential and on reasonable measures — access limits, confidentiality markings, agreements, employee awareness. | Repository custody alone does not create trade-secret protection. Documented handling, access control, and awareness support — but do not guarantee — that status. |
| 2 | Definition of a Trade Secret — 18 U.S.C. § 1839 | U.S. Congress | Legal | [uscode.house.gov](https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title18-section1839&num=0&edition=prelim) | U.S. law covers business and technical compilations, methods, processes, and programs when the owner takes reasonable measures and the information has economic value from secrecy. | Reasonable measures are the operative phrase. Program controls should be defensible against that standard. |
| 3 | AI Risk Management Framework 1.0 | NIST | Framework | [nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) | Shared vocabulary and lifecycle for managing AI risks across govern, map, measure, and manage functions. | The four functions map naturally onto the operating model (govern the playbook, map program context, measure adoption, manage change). |
| 4 | Generative AI Profile — AI 600-1 | NIST | Framework profile | [nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | Connects generative-AI governance to organizational risk. Calls for monitoring sensitive-data exposure, testing, content provenance. | Directly supports the adoption-monitoring protocol and the provenance requirements for generated program work. |
| 5 | Securing Data Used to Train and Operate AI | CISA · NSA · FBI (joint) | Government guidance | [cisa.gov/resources-tools/resources/ai-data-security-best-practices-securing-data-used-train-operate-ai-systems](https://www.cisa.gov/resources-tools/resources/ai-data-security-best-practices-securing-data-used-train-operate-ai-systems) | Data security and integrity across the AI lifecycle are necessary for trustworthy outcomes, including sensitive, proprietary, and mission-critical data. | **Reference-model anchor** for the bi-directional SAP semantic layer / sovereign model position: both directions operate against a client-controlled data boundary with documented provenance. |
| 6 | Guidelines for Secure AI System Development | UK NCSC · CISA | Government guidance | [ncsc.gov.uk/collection/guidelines-secure-ai-system-development](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) | Security across design, development, deployment, and operation — including systems built on external models and APIs. | Supports the "additive integration" position: security discipline extends to systems built on top of vendor models, not only to models themselves. |
| 7 | ISO/IEC 42001 AI Management Systems | ISO/IEC | Standard | [iso.org/standard/42001](https://www.iso.org/standard/42001) | Organization-wide management system for AI policy, responsibility, risk, data governance, monitoring, and continual improvement. | Provides the certifiable structure clients can align adoption governance to. |
| 8 | Lost in the Middle | Liu et al. — TACL | Peer-reviewed research | [aclanthology.org/2024.tacl-1.9](https://aclanthology.org/2024.tacl-1.9/) | Long context alone is not reliable: model performance drops when relevant information sits in the middle of a long input window. | Directly supports the "structured, current, selectively retrieved context is preferable to indiscriminately sending entire repositories into model windows" position. |

## Sources referenced elsewhere in the surface but not in the evidence grid

- **Retrieval-Augmented Generation** — Lewis et al. (NeurIPS 2020). [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401). Foundational retrieval-with-generation pattern behind selective, provenance-preserving context reasoning.

## Wording discipline reminders

- **Trade secrecy:** never claim automatic protection from repository custody. Use "supports — not guarantees — reasonable measures."
- **Context quality:** never claim "more context is always better." Prefer "structured, current, selectively retrieved."
- **SAP trademarks:** descriptive only; no implied endorsement or partnership.
- **CISA / NIST / NCSC / ISO material:** general information, not legal advice; not an endorsement of the program by the issuing organization.
