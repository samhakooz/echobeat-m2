
import tkinter as tk
import time

# Store our robot's rhythm
events = []
recording = False
playing = False
first_hit = None

# Create the window
root = tk.Tk()
root.title("EchoBeat M2")
root.geometry("440x320")
root.configure(bg="#171b24")


def flash(drum):
    if drum == "L":
        pad = left_pad
        color = "#3399FF"      # Bright blue when hit
        original = "#1E3A8A"   # Dark blue normally
    else:
        pad = right_pad
        color = "#FF4444"      # Bright red when hit
        original = "#991B1B"   # Dark red normally

    pad.config(bg=color)
    root.after(120, lambda: pad.config(bg=original))


def hit(drum):
    global first_hit

    if playing:
        return

    flash(drum)

    if recording:
        now = time.perf_counter()

        if first_hit is None:
            first_hit = now

        elapsed = round((now - first_hit) * 1000)
        events.append((elapsed, drum))

        status.config(
            text=f"Recorded {drum} at {elapsed} ms"
        )


def start_recording():
    global events, recording, first_hit

    if playing:
        return

    events = []
    first_hit = None
    recording = True
    status.config(text="Recording... Play a rhythm!")


def stop_recording():
    global recording
    recording = False
    status.config(text=f"Saved {len(events)} hits")


def playback_hit(drum):
    flash(drum)
    status.config(text=f"Playing: {drum}")


def playback_done():
    global playing
    playing = False
    status.config(text="Playback complete!")


def playback():
    global playing

    if recording:
        stop_recording()

    if playing or not events:
        return

    playing = True

    for timestamp, drum in events:
        root.after(
            timestamp,
            lambda d=drum: playback_hit(d)
        )

    root.after(events[-1][0] + 300, playback_done)


# Title
title = tk.Label(
    root, text="ECHOBEAT M2",
    font=("Arial", 20, "bold"),
    fg="white", bg="#171b24"
)
title.pack(pady=15)

# Drum pads
frame = tk.Frame(root, bg="#171b24")
frame.pack(pady=10)

left_pad = tk.Button(
    frame, text="LEFT DRUM\n(A)",
    width=15, height=5,
    bg="#1E3A8A", fg="white",
    command=lambda: hit("L")
)
left_pad.pack(side="left", padx=10)

right_pad = tk.Button(
    frame, text="RIGHT DRUM\n(L)",
    width=15, height=5,
    bg="#991B1B", fg="white",
    command=lambda: hit("R")
)
right_pad.pack(side="left", padx=10)

# Recording controls
controls = tk.Frame(root, bg="#171b24")
controls.pack(pady=10)

tk.Button(
    controls, text="Record",
    command=start_recording
).pack(side="left", padx=5)

tk.Button(
    controls, text="Stop",
    command=stop_recording
).pack(side="left", padx=5)

tk.Button(
    controls, text="Play",
    command=playback
).pack(side="left", padx=5)

status = tk.Label(
    root, text="Ready to play",
    fg="white", bg="#171b24"
)
status.pack(pady=5)

# Keyboard controls
root.bind("<KeyPress-a>", lambda e: hit("L"))
root.bind("<KeyPress-l>", lambda e: hit("R"))

root.mainloop()
