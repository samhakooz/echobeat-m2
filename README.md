# EchoBeat M2 — Mechanical Two-Arm Rhythm Robot

> **Status: Concept / not built or tested.** This repository is a design and documentation starting point, not a copied robot kit or a proven hardware design.

## The challenge
Can a low-cost, custom-designed, two-arm desktop robot reproduce rhythms a human inputs, and can software calibration improve **actual audible hit timing**?

## What I'm creating
Two custom 3D-printed beater arms driven by micro servos strike two replaceable drum surfaces. Three buttons let a user input left/right notes and start or stop recording. A Raspberry Pi Pico 2 W records timestamps, then commands the servos to replay the pattern. Later firmware will compensate for servo response time and optionally generate rhythmic variations.

## Planned version 1 features
- Two independent beaters, left and right
- Two input buttons, one record/play button
- Record a sequence of up to 16 notes at first (increase later)
- Replay notes with the original time intervals
- Physical reset/off by disconnecting power; servo motion range limited in software
- Documented measurement of *sound* timing, not just motor command timing

## Hardware and geometry
- Target envelope: **230 mm W × 190 mm D × ≤90 mm H**
- Two 58 mm diameter drum pads with centers 112 mm apart
- Beater reach: 75 mm from servo axle to striker center (adjustable ±3 mm)
- See [design spec](docs/design-spec.md), [top view](hardware/top-view.svg), [side view](hardware/side-view.svg) and [BOM](docs/bom.md)
- Geometry is a **CAD starting specification**; print a one-arm prototype before committing to full dimensions.

## Proposed measurements
A 16-note rhythm at 60, 80, and 100 BPM; compare the input event timestamps against actual impact timestamps extracted from phone/laptop audio or slow motion. Report median absolute timing error, missed hits, unintended double hits, and any timing change after calibration. Targets, not claims: >90% hit success and <100 ms median error for slow patterns.

## Milestones
- [ ] 00 — Create this GitHub repository and engineering log
- [ ] 01 — Run Python-only rhythm timestamp tests on laptop
- [ ] 02 — Set up MicroPython and read the three buttons
- [ ] 03 — Drive one servo with safe angles; confirm external 5 V supply
- [ ] 04 — Prototype one arm and one pad, revise CAD
- [ ] 05 — Assemble two arms, pads and base
- [ ] 06 — Implement two-channel record/replay
- [ ] 07 — Measure physical hit delay and add compensation
- [ ] 08 — Film a demo and publish results and lessons

## Repo navigation
- [`docs/design-spec.md`](docs/design-spec.md): dimensions and design decisions
- [`docs/bom.md`](docs/bom.md): exact model suggestions and US parts budget
- [`docs/wiring.md`](docs/wiring.md): pin map and power separation
- [`docs/build-log.md`](docs/build-log.md): weekly dated engineering log
- [`docs/ai-usage.md`](docs/ai-usage.md): transparency log for AI assistance
- [`docs/test-plan.md`](docs/test-plan.md): tests and success criteria
- `hardware/`: editable CAD files **to be authored by me**, plus preliminary diagrams
- `src/`: Python rhythm algorithms (to be written)
- `firmware/`: MicroPython for Pico (to be written)
- `tests/`: automated test cases and results (to be written)
- `media/`: build photos and demo video (to be added)

## Ownership and documentation
This is my own mechanical configuration and program. Component-level guides and APIs may be consulted and credited; I will not present outside CAD or AI-generated code that I don't understand as my own unassisted work. See [AI usage](docs/ai-usage.md).

## Notes
Do not claim successful performance until hardware has been built and measured. Costs and hardware availability can change. Low-voltage servo wiring should be checked before energizing.
