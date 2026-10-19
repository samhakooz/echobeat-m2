# Python algorithm modules (to be implemented)

Initial independent coding exercises:

1. Record two channels of timestamped events, e.g. `[(1000, "L"), (1250, "R"), (1500, "L")]`.
2. Convert the list to offsets from the first hit: `[0, 250, 500]`.
3. Detect and filter bounce on the **same input button** within 25 ms.
4. Sort and replay scheduled events without losing simultaneous L/R notes.
5. Calculate timing-error metrics after collecting real recordings.

Keep the logic independent of Pico hardware so you can test on your computer. Don't implement advanced AI until record/playback is reliable.
