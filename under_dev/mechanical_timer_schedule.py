"""Simulate a stack of mechanical timers with binary outputs."""

import matplotlib.pyplot as plt
import numpy as np


def make_schedule(on_ranges, resolution_minutes=15):
    """
    Return a binary array (length N = 24 h / resolution) for one timer dial.
    on_ranges - list of (start, end) times in decimal hours, end exclusive.
    """
    slots = 24 * 60 // resolution_minutes
    ar = np.zeros(slots, dtype=int)
    for start, end in on_ranges:
        i0 = int(start * 60 // resolution_minutes)
        i1 = int(end * 60 // resolution_minutes)
        ar[i0:i1] = 1
    return ar


def stack_period(schedules, repeat_factor=2):
    """
    Simulate a stack of mechanical timers until `repeat_factor` x natural period.
    Returns (outputs_matrix, total_slots_simulated, dial_length).
    """
    n_plugs = len(schedules)
    dial_len = len(schedules[0])
    pointers = [0] * n_plugs
    seen = {}
    history = [[] for _ in range(n_plugs)]

    step = 0
    period = None
    stop_step = float("inf")  # temporarily set to a large number

    while step < stop_step:
        state = tuple(pointers)

        if period is None:
            if state in seen:
                period = step - seen[state]
                stop_step = repeat_factor * period
                print(f"Detected period: {period} slots; extending to {stop_step}")
            else:
                seen[state] = step

        # Evaluate outputs
        upstream = 1
        for i in range(n_plugs):
            out = int(upstream & schedules[i][pointers[i]])
            history[i].append(out)
            upstream = out

        # Advance dials
        pointers[0] = (pointers[0] + 1) % dial_len
        for i in range(1, n_plugs):
            if history[i - 1][-1] == 1:
                pointers[i] = (pointers[i] + 1) % dial_len

        step += 1

    outputs = np.array(history)
    return outputs, step, dial_len


def plot_outputs(outputs: np.ndarray, resolution: int, title: str = None):
    slots = outputs.shape[1]
    _, ax = plt.subplots(figsize=(14, 3))

    ax.imshow(outputs, aspect="auto", interpolation="nearest")
    ax.set_yticks(range(outputs.shape[0]))
    ax.set_yticklabels([f"Plug {i}" for i in range(outputs.shape[0])])

    # X-axis: hours
    slot_to_hour = lambda i: i * resolution / 60
    max_hours = slots * resolution / 60
    n_ticks = min(20, slots)
    ticks = np.linspace(0, slots - 1, n_ticks, dtype=int)
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{slot_to_hour(i):.0f}h" for i in ticks])
    ax.set_xlabel("Time (hours)")

    if title is None:
        title = f"Cascaded Timer Outputs - full period ({max_hours:.0f} hours)"
    ax.set_title(title)

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# EXAMPLE CONFIGURATION  (same as earlier demo)
# ------------------------------------------------------------
resolution_minutes = 20  # in minutes - the length of each interval in the dial
# plug_cfgs = [
#     make_schedule([(6, 10), (18, 22)], resolution_minutes),  # Plug 0
#     make_schedule([(7.5, 9.25), (19, 20.5)], resolution_minutes),  # Plug 1
#     make_schedule([(8, 11)], resolution_minutes),  # Plug 2
# ]
plug_cfgs = [
    make_schedule([(0, 12)], resolution_minutes),  # Plug 0
    make_schedule([(0, 12)], resolution_minutes),  # Plug 1
]

outputs, period_slots, dial_len = stack_period(plug_cfgs, repeat_factor=2)
period_days = period_slots * resolution_minutes / 60 / 24


print(f"Full repeating period: {period_slots} slots " f"= {period_days:.1f} days")
plot_outputs(outputs, resolution_minutes)
