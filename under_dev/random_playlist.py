# pylint: disable=all
import numpy as np
from collections import Counter

song_count = 400  # 10  # # samples (30 hours long playlist, with songs of about 4-5)
time_length = 2400  # 100  # steps # sample size (listened to it for about 40 weeks and 5 hours per week, so 200 hours or 12K minutes or about 2400 played songs)

sampled_array = np.random.randint(0, song_count, time_length)  # playlist_random_sequence

# Finding the most continuously repeated sample
max_repeated_sample = None
max_repeated_count = 0
current_sample = None
current_count = 0
max_repeated_start_index = None
max_repeated_end_index = None
current_start_index = 0

for index, sample in enumerate(sampled_array):
    if sample == current_sample:
        current_count += 1
    else:
        if current_count > max_repeated_count:
            max_repeated_count = current_count
            max_repeated_sample = current_sample
            max_repeated_start_index = current_start_index
            max_repeated_end_index = index - 1
        current_sample = sample
        current_count = 1
        current_start_index = index

# Final check for the last sequence
if current_count > max_repeated_count:
    max_repeated_count = current_count
    max_repeated_sample = current_sample
    max_repeated_start_index = current_start_index
    max_repeated_end_index = len(sampled_array) - 1

# Finding the longest gap between two consecutive appearances of the same sample
last_index = {}
max_gap = 0
sample_with_max_gap = None
max_gap_start_index = None
max_gap_end_index = None

for index, sample in enumerate(sampled_array):
    if sample in last_index:
        gap = index - last_index[sample]
        if gap > max_gap:
            max_gap = gap
            sample_with_max_gap = sample
            max_gap_start_index = last_index[sample]
            max_gap_end_index = index
    last_index[sample] = index


# Counting occurrences of each sample
counter = Counter(sampled_array)

# Finding the most repeated sample
most_repeated_sample = counter.most_common(1)[0][0]
most_repeated_indices = [
    index for index, sample in enumerate(sampled_array) if sample == most_repeated_sample
]

# Finding the least repeated sample (ties are resolved by the first occurrence in the list)
least_repeated_count = min(counter.values())
least_repeated_samples = [
    sample for sample, count in counter.items() if count == least_repeated_count
]
least_repeated_sample = least_repeated_samples[0]
least_repeated_indices = [
    index for index, sample in enumerate(sampled_array) if sample == least_repeated_sample
]

###### printing

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BRIGHT_RED = "\033[91m"
RESET = "\033[0m"

# Print the sampled array with coloring
for index, sample in enumerate(sampled_array):
    if max_repeated_start_index <= index <= max_repeated_end_index:
        color = GREEN
    elif index == max_gap_start_index or index == max_gap_end_index:
        color = BRIGHT_RED
    elif sample == most_repeated_sample:
        color = MAGENTA
    elif sample == least_repeated_sample:
        color = CYAN
    else:
        color = BLACK
    print(f"{color}{sample}{RESET}", end=" ")

print("\n")

print("Sampled Array:", sampled_array)
print("Most Continuously Repeated Sample:", max_repeated_sample)
print("Repetition Count:", max_repeated_count)
print("Repetition Start Index:", max_repeated_start_index)
print("Repetition End Index:", max_repeated_end_index)
print("Sample with Longest Gap:", sample_with_max_gap)
print("Longest Gap Length:", max_gap)
print("Longest Gap Start Index:", max_gap_start_index)
print("Longest Gap End Index:", max_gap_end_index)
print("Most Repeated Sample:", most_repeated_sample)
print("Most Repeated Indices:", most_repeated_indices)
print("Least Repeated Sample:", least_repeated_sample)
print("Least Repeated Indices:", least_repeated_indices)
