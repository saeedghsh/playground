# pylint: disable=all
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Constants
n = 400  # Upper limit of the range
sample_size = 2400  # Number of samples
num_runs = 1000  # Number of iterations


def find_longest_continuous_repetition(array):
    max_repeated_count = 0
    current_count = 0
    current_sample = None

    for sample in array:
        if sample == current_sample:
            current_count += 1
        else:
            if current_count > max_repeated_count:
                max_repeated_count = current_count
            current_sample = sample
            current_count = 1

    # Final check for the last sequence
    if current_count > max_repeated_count:
        max_repeated_count = current_count

    return max_repeated_count


def find_longest_gap(array):
    last_index = {}
    max_gap = 0

    for index, sample in enumerate(array):
        if sample in last_index:
            gap = index - last_index[sample]
            if gap > max_gap:
                max_gap = gap
        last_index[sample] = index

    return max_gap


def find_most_repeated_sample_count(array):
    counter = Counter(array)
    most_repeated_count = counter.most_common(1)[0][1]
    return most_repeated_count


# Lists to store results from each run
longest_gaps = []
longest_sequences = []
most_repetitions = []

for _ in range(num_runs):
    # Generate the sampled array
    sampled_array = np.random.randint(0, n, sample_size)

    # Find longest continuous repetition
    longest_sequence = find_longest_continuous_repetition(sampled_array)

    # Find longest gap between two consecutive appearances of the same sample
    longest_gap = find_longest_gap(sampled_array)

    # Find most repeated sample count
    most_repeated_count = find_most_repeated_sample_count(sampled_array)

    # Append results to lists
    longest_gaps.append(longest_gap)
    longest_sequences.append(longest_sequence)
    most_repetitions.append(most_repeated_count)

# Calculate statistics
mean_longest_gap = np.mean(longest_gaps)
stddev_longest_gap = np.std(longest_gaps)
mean_longest_sequence = np.mean(longest_sequences)
stddev_longest_sequence = np.std(longest_sequences)
mean_most_repetitions = np.mean(most_repetitions)
stddev_most_repetitions = np.std(most_repetitions)

# Print statistics
print("Statistics over 10,000 runs:")
print(f"Longest Gap - Mean: {mean_longest_gap}, Std Dev: {stddev_longest_gap}")
print(f"Longest Sequence - Mean: {mean_longest_sequence}, Std Dev: {stddev_longest_sequence}")
print(f"Most Repetitions - Mean: {mean_most_repetitions}, Std Dev: {stddev_most_repetitions}")

# Plot histograms of the results
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.hist(longest_gaps, bins=20, color="blue", alpha=0.7)
plt.title("Longest Gaps")
plt.xlabel("Gap Length")
plt.ylabel("Frequency")

plt.subplot(1, 3, 2)
plt.hist(longest_sequences, bins=20, color="green", alpha=0.7)
plt.title("Longest Sequences")
plt.xlabel("Sequence Length")
plt.ylabel("Frequency")

plt.subplot(1, 3, 3)
plt.hist(most_repetitions, bins=20, color="magenta", alpha=0.7)
plt.title("Most Repetitions")
plt.xlabel("Repetition Count")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
