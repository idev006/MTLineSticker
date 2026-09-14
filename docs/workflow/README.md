# MTLineSticker Production Workflow

**Version:** 1.1  
**Status:** Active  
**Scope:** End-to-end LINE sticker product creation, AI-assisted visual production, QA, handoff and release workflow.

This folder is the operational entry point for producing a sticker set from concept to LINE submission.

## Documents

1. [`LINE_STICKER_END_TO_END_PIPELINE.md`](LINE_STICKER_END_TO_END_PIPELINE.md)  
   Canonical end-to-end process: Product Strategy → Gem A → Character Sheet → Product Owner Approval → Gem B Hero → Full Production → Engine/QA → LINE submission → post-release learning.

2. [`AI_TOOL_USAGE_GUIDE.md`](AI_TOOL_USAGE_GUIDE.md)  
   Which tool to use at each stage, what files to provide, what the AI is allowed to decide, what it must not decide, current runtime handoff bundles and copy-ready prompt patterns.

3. [`PRODUCTION_RUNBOOK_AND_GATES.md`](PRODUCTION_RUNBOOK_AND_GATES.md)  
   Operator runbook, mandatory states/gates, acceptance criteria, stop conditions, artifact checklist and recovery rules.

4. [`../gems/GEM_OPERATIONAL_PLAYBOOK.md`](../gems/GEM_OPERATIONAL_PLAYBOOK.md)  
   Practical Gem A / Gem B operating manual: deployment, Character Sheet style lock, authority hierarchy, Hero-first handoff, runtime attachments, state cheat sheet and recovery from common failures.

## Operating principle

The workflow is evidence-driven and gate-controlled. AI may propose, analyze and generate candidates, but Product Owner approval controls Character activation, Hero acceptance and release unlocks.

The Character Sheet is not only an identity reference; once approved it is a Character Visual SSOT. Its production style should therefore be correct before activation rather than deferred to Gem B.

The commercial North Star is not merely to complete 40 images. The set should be useful in real chats, distinctive, memorable, production-consistent and credible as a product people may choose to buy.

## Authority

Repository SSOT and approved set/Character artifacts outrank conversational memory, AI assumptions and old project examples.

If this workflow conflicts with a more specific active SSOT document, the more specific active SSOT wins. Record the conflict instead of guessing.
