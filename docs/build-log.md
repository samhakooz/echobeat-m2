# Engineering build log

Use a new entry on every build day. Record decisions and failures, not only successful demos.

## 2026-10-19 — Design drafted (not tested)
**Goal:** Define a unique mechanically simple two-arm robotic drummer and measurable success criteria.

**Decisions:** use Pico 2 W + SG92R servos, mechanical drum heads, three tactile buttons, and MicroPython. Make the first experiment recording/playback accuracy.

**Evidence:** initial drawings in `hardware/`; bill of materials in `docs/bom.md`.

**Next experiment:** Python rhythm-event recorder on PC (no hardware required).

---

## [DATE] — [SHORT TITLE]
**Hypothesis:**

**What I built or coded:**

**Results with actual numbers:**

**What failed:**

**What I changed and why:**

**Screenshots/video/commit link:**

**Next experiment:**
### Milestone 1D — Rhythm Storage
**Date:** October 19, 2026

**Status:** Completed

**What I built:**
- Added the ability to save recorded drum patterns as JSON files.
- Added the ability to load previously saved rhythms.
- Successfully replayed a saved rhythm after closing and reopening the program.

**Testing:**
- Recorded a rhythm using the virtual drum pads.
- Saved the rhythm to `rhythm.json`.
- Closed and reopened the application.
- Loaded the saved rhythm and successfully replayed it.

**What I learned:**
- How to save and retrieve data using Python's JSON module.
- How to use file operations to preserve data between program sessions.

**AI assistance:**
- Used ChatGPT for code examples, explanations, and implementation guidance.
- Tested the functionality using Thonny.

**Result:** Rhythm saving, loading, and playback worked successfully.
