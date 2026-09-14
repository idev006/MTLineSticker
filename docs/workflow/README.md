# MTLineSticker Production Workflow

**Version:** 1.2  
**Status:** Active  
**Scope:** End-to-end LINE sticker product creation, AI-assisted visual production, QA, handoff and release workflow.

This folder is the operational entry point for producing a sticker set from concept to LINE submission.

## Start here first

If you are a normal user/operator and want the easiest path, open these first:

1. [`START_HERE.md`](START_HERE.md)  
   Simple roadmap: what to do now, which tool to use, what files to attach, what state you need before the next step.

2. [`COPY_PASTE_PROMPT_LIBRARY.md`](COPY_PASTE_PROMPT_LIBRARY.md)  
   Ready-to-use prompts for Gem A, Character Sheet generation, Character revision, Gem B Hero, Hero correction, Full Production and approval records.

## Detailed documents

3. [`LINE_STICKER_END_TO_END_PIPELINE.md`](LINE_STICKER_END_TO_END_PIPELINE.md)  
   Canonical end-to-end process: Product Strategy → Gem A → Character Sheet → Product Owner Approval → Gem B Hero → Full Production → Engine/QA → LINE submission → post-release learning.

4. [`AI_TOOL_USAGE_GUIDE.md`](AI_TOOL_USAGE_GUIDE.md)  
   Which tool to use at each stage, what files to provide, what the AI is allowed to decide, what it must not decide, current runtime handoff bundles and copy-ready prompt patterns.

5. [`PRODUCTION_RUNBOOK_AND_GATES.md`](PRODUCTION_RUNBOOK_AND_GATES.md)  
   Operator runbook, mandatory states/gates, acceptance criteria, stop conditions, artifact checklist and recovery rules.

6. [`../gems/GEM_OPERATIONAL_PLAYBOOK.md`](../gems/GEM_OPERATIONAL_PLAYBOOK.md)  
   Practical Gem A / Gem B operating manual: deployment, Character Sheet style lock, authority hierarchy, Hero-first handoff, runtime attachments, state cheat sheet and recovery from common failures.

## Operating principle

The workflow is evidence-driven and gate-controlled. AI may propose, analyze and generate candidates, but Product Owner approval controls Character activation, Hero acceptance and release unlocks.

The Character Sheet is not only an identity reference; once approved it is a Character Visual SSOT. Its production style should therefore be correct before activation rather than deferred to Gem B.

The commercial North Star is not merely to complete 40 images. The set should be useful in real chats, distinctive, memorable, production-consistent and credible as a product people may choose to buy.

## UX principle for documentation

Documentation should reduce operator confusion. A user should be able to answer these five questions quickly:

1. Where am I in the pipeline?
2. What do I do next?
3. Which tool do I use?
4. Which files do I attach?
5. What can I copy-paste?

If a document adds complexity without helping one of those questions or protecting a critical gate/SSOT rule, prefer simplification.

## Authority

Repository SSOT and approved set/Character artifacts outrank conversational memory, AI assumptions and old project examples.

If this workflow conflicts with a more specific active SSOT document, the more specific active SSOT wins. Record the conflict instead of guessing.
