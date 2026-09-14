# MTLineSticker Production Workflow

**Version:** 1.0  
**Status:** Active  
**Scope:** End-to-end LINE sticker product creation, AI-assisted visual production, QA, handoff and release workflow.

This folder is the operational entry point for producing a sticker set from concept to LINE submission.

## Documents

1. [`LINE_STICKER_END_TO_END_PIPELINE.md`](LINE_STICKER_END_TO_END_PIPELINE.md)  
   Canonical end-to-end process: Product Strategy → Gem A → Character Sheet → Product Owner Approval → Gem B Hero → Full Production → Engine/QA → LINE submission → post-release learning.

2. [`AI_TOOL_USAGE_GUIDE.md`](AI_TOOL_USAGE_GUIDE.md)  
   Which tool to use at each stage, what files to provide, what the AI is allowed to decide, what it must not decide, and copy-ready prompt patterns.

3. [`PRODUCTION_RUNBOOK_AND_GATES.md`](PRODUCTION_RUNBOOK_AND_GATES.md)  
   Operator runbook, mandatory states/gates, acceptance criteria, stop conditions, artifact checklist and recovery rules.

## Operating principle

The workflow is evidence-driven and gate-controlled. AI may propose, analyze and generate candidates, but Product Owner approval controls Character activation, Hero acceptance and release unlocks.

The commercial North Star is not merely to complete 40 images. The set should be useful in real chats, distinctive, memorable, production-consistent and credible as a product people may choose to buy.

## Authority

Repository SSOT and approved set/Character artifacts outrank conversational memory, AI assumptions and old project examples.

If this workflow conflicts with a more specific active SSOT document, the more specific active SSOT wins. Record the conflict instead of guessing.
