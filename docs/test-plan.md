# EchoBeat validation plan

## Experiment question
How closely does a two-servo robot reproduce human-input note timing, and does a measured servo-response offset improve it?

## Software-only tests before hardware
- Empty recording should not play stray notes.
- A 3-note recording should normalize timestamps from first note (e.g., [1000, 1500, 2000] → [0, 500, 1000] ms).
- Two notes with the same time but different channels should both survive.
- Input bounce inside 25 ms should not become an extra beat.
- Events should play chronologically with their original channel.
- A stop button must interrupt replay.

## Hardware acceptance tests
- Button press recognized once each in 20 slow taps.
- Both arms move without hitting the mounting towers or each other.
- No servo buzz/hard stall when holding rest position.
- Single strokes produce audible contact and recover before next stroke.
- Play 16-note sequences at 60, 80, 100 BPM; test three patterns at each speed.

## Measurements
For each note, record target timestamp (software log) and observed acoustic impact (record phone or computer audio, mark transient). Pair hits to targets. Report **median absolute error in ms** and missed / double hits, by BPM and arm. Log command timestamps separately so you don't confuse command scheduling with physical impact.

Suggested early **goals**, not predicted results: ≥90% correct audible single hits and <100 ms median impact error on slow patterns. If unsuccessful, document why and change the design.

| Date | BPM | Pattern | Target notes | Audible hits | Median error (ms) | What changed |
|---|---:|---|---:|---:|---:|---|
| TBD | 60 | alternating | 16 | TBD | TBD | Initial baseline |
| TBD | 80 | alternating | 16 | TBD | TBD | Timing compensation |
| TBD | 100 | mixed | 16 | TBD | TBD | Faster sequence |
