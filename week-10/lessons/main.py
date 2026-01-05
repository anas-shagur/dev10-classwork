import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split

mean_height_cm = 167.0
stddev_height_cm = 10.0
mean_neurons_in_brain = 86_000_000_000
stddev_neurons_in_brain = 8_000_000_000
n = 100

heights = np.random.normal(mean_height_cm, stddev_height_cm, n)
heights = np.round(heights, 2)

weights = 10 + 0.35 * heights + np.random.normal(0, 8, n)
weights = np.round(weights, 2)

neurons_in_brain = np.random.normal(
    mean_neurons_in_brain, stddev_neurons_in_brain, n
)
neurons_in_brain = np.round(neurons_in_brain)

human_df = pd.DataFrame(
    {
        "height_cm": heights,
        "weight_kg": weights,
        "neurons_in_brain": neurons_in_brain,
    }
)

normalized_data = normalize(
    human_df[["height_cm", "weight_kg", "neurons_in_brain"]], axis=0
)

human_df["height_normalized"] = normalized_data[:, 0]
human_df["weight_normalized"] = normalized_data[:, 1]
human_df["neurons_normalized"] = normalized_data[:, 2]

print(normalized_data)

print(human_df.head())
