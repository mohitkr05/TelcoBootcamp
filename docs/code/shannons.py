import numpy as np
import matplotlib.pyplot as plt

def channel_capacity(B, S, N):
  """Calculates the channel capacity in b/s.

  Args:
    B: The bandwidth in Hz.
    S: The signal power in W.
    N: The noise power in W.

  Returns:
    The channel capacity in b/s.
  """

  return B * np.log2(1 + S / N)

# Define the range of values to plot.
SNRs = np.linspace(0, 20, 100)

# Calculate the channel capacity for each SNR.
channel_capacities = channel_capacity(1e6, 1, SNRs)

# Plot the channel capacity.
plt.plot(SNRs, channel_capacities, label='Channel Capacity')
plt.xlabel('SNR (dB)')
plt.ylabel('Channel Capacity (b/s)')
plt.legend()
plt.grid(True)
plt.show()