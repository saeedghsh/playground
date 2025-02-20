# source: https://www.youtube.com/watch?v=pAMgUB51XZA
import numpy as np
import matplotlib.pyplot as plt

sequence = [1, 1]
while len(sequence) < 1000:
    n = len(sequence)  # NOTE: if adding +1 here, the path would be stable from the beginning
    gcd = np.gcd(n, sequence[-1])
    print(gcd)
    if gcd == 1:
        sequence.append(sequence[-1] + n + 1)
    else:
        sequence.append(int(sequence[-1] / gcd))

plt.plot(sequence, "k.")
plt.show()
