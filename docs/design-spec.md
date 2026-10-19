# EchoBeat M2 — mechanical design specification v0.1

## Coordinate system
Origin = center of base. +X = right, +Y = back, +Z = up. All dimensions in **mm**.

| Feature | X | Y | Z | Notes |
|---|---:|---:|---:|---|
| Base | 0 | 0 | bottom 0, top 6 | 230 W × 190 D × 6 thick, with ribs if needed |
| Left drum pad center | -56 | -30 | top surface 24 | 58 Ø; printed shell, replaceable head |
| Right drum pad center | +56 | -30 | top surface 24 | 58 Ø; try different materials/thicknesses |
| Left servo output shaft | -56 | +40 | axis 56 | Shaft points sideways along X |
| Right servo output shaft | +56 | +40 | axis 56 | Shaft points sideways along X |
| Left input button | -56 | -75 | mounted as needed | 12×12 mm tactile switch, printed plunger optional |
| Right input button | +56 | -75 | mounted as needed | 12×12 mm tactile switch, printed plunger optional |
| Record / play button | 0 | -75 | mounted as needed | third 12×12 mm switch |

## Beater geometry (starting CAD measurements)
- Servo center/pivot target: y +40, z 56
- Pad center: y -30; pad upper face z 24
- Striker tip radius: approx 4 mm; center at impact around z 28
- Effective arm length from axle to center of striker: **75 mm**, adjust ±3 mm using a slotted tip bracket
- Starting resting orientation: approx 8° downward from horizontal toward front
- Starting contact orientation: approx 22° downward; this gives a tip center near y -29.6, z 28.2 mm
- Therefore the measured predicted tip-to-pad vertical drop from rest is about 19 mm
- **Those are geometric targets, not servo PWM positions**; actual motor neutral, horn indexing, and flex must be calibrated before running.

## Mechanical component list
1. Flat base plate 230×190×6 mm (A1 build area compatible; add ribs and mounting slots).
2. Left and right 58 mm Ø hollow drum shells, approx 18 mm shell height plus ~2 mm head, top at 24 mm above bottom datum.
3. Interchangeable 58 mm Ø pad heads; start with 2 mm PETG/PLA; test two thicknesses or cushionings for distinct tones.
4. Two mirrored servo towers; fix shaft axes at target positions but **measure your actual SG92R servo before finalizing mounting holes**.
5. Two lightweight arms 75 mm effective reach; initial 6 mm wide × 4 mm thick beam as a prototype, fitted to included servo horns using horn hardware (do not rely on a press-fit spline).
6. Two replaceable ~8 mm Ø soft striker tips (small rubber bumpers; no sharp or heavy tips).
7. Front button panel, rear Pico and power compartment, cable clips, and non-slip feet.

## Print assumptions
- PLA or PETG for chassis; PLA arms can be first prototype.
- Start with 0.20 mm layers; use 3 walls on towers and arms; print arms flat.
- No required support on flat arm/base parts; tower geometry should be designed for support-free printing where possible.
- Do not print the entire assembly first. Validate ONE servo, ONE arm, ONE drum head with a cardboard/printed jig.

## Risks and mitigations
- **Missed/double strikes**: adjust travel, add soft tip, allow servo recovery time; test slow rhythms first.
- **Servo gear wear**: make arm lightweight, keep soft limit clearance, avoid hard stalled contact against drum.
- **Weak sound**: treat heads as interchangeable experiments, not assumed percussion-quality drums.
- **Timing variation**: measure real impacts from recorded audio and compensate lead time in software.
- **Pinch points**: guard servo horns and keep hands clear of moving arms while active.
- **Dimensions not fitting exact servo**: model from measured unit; keep mounts slotted/adjustable.

## Design decision log
- Chose two independent arms so rhythms can have two simultaneous channels.
- Chose buttons over microphones initially: deterministic input is easier to debug and avoids extra sensor conditioning.
- Chose Pico 2 W because MicroPython works offline now, Wi-Fi permits a future browser UI.
- Chose replaceable pad heads so mechanical acoustics can be tested without changing the whole design.
