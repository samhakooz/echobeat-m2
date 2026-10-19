
import time

events = []
start_time = None

print("EchoBeat M2 — Rhythm Recorder")
print("Type L or R, then press Enter. Type Q to stop.")

while True:
    drum = input("Drum: ").strip().upper()

    if drum == "Q":
        break

    if drum not in ("L", "R"):
        print("Invalid input. Choose L or R.")
        continue

    current_time = time.perf_counter()

    if start_time is None:
        start_time = current_time

    elapsed_ms = round((current_time - start_time) * 1000)
    events.append((elapsed_ms, drum))

    print(f"Recorded {drum} at {elapsed_ms} ms")

print("\nYour recorded rhythm:")
print(events)
