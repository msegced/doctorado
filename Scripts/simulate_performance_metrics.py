import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)
n_runs = 1000

# Simulated metrics for Baseline and Ontology-Based DT
data = {
    'checkin_baseline': np.random.normal(loc=6.8, scale=1.2, size=n_runs),
    'checkin_dt': np.random.normal(loc=4.5, scale=0.9, size=n_runs),
    'efficiency_baseline': np.random.normal(loc=71.3, scale=4.8, size=n_runs),
    'efficiency_dt': np.random.normal(loc=85.4, scale=3.2, size=n_runs),
    'satisfaction_baseline': np.random.normal(loc=78.6, scale=5.1, size=n_runs),
    'satisfaction_dt': np.random.normal(loc=88.7, scale=3.7, size=n_runs)
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Summary statistics
summary = {
    'Metric': ['Avg. Check-In Time', 'Staff Efficiency Score', 'Guest Satisfaction Index'],
    'Baseline Mean ± Std': [
        f"{df['checkin_baseline'].mean():.2f} ± {df['checkin_baseline'].std():.2f}",
        f"{df['efficiency_baseline'].mean():.2f} ± {df['efficiency_baseline'].std():.2f}",
        f"{df['satisfaction_baseline'].mean():.2f} ± {df['satisfaction_baseline'].std():.2f}"
    ],
    'DT Mean ± Std': [
        f"{df['checkin_dt'].mean():.2f} ± {df['checkin_dt'].std():.2f}",
        f"{df['efficiency_dt'].mean():.2f} ± {df['efficiency_dt'].std():.2f}",
        f"{df['satisfaction_dt'].mean():.2f} ± {df['satisfaction_dt'].std():.2f}"
    ],
    'Improvement (%)': [
        f"{(1 - df['checkin_dt'].mean() / df['checkin_baseline'].mean()) * 100:.1f}%",
        f"{(df['efficiency_dt'].mean() / df['efficiency_baseline'].mean() - 1) * 100:.1f}%",
        f"{(df['satisfaction_dt'].mean() / df['satisfaction_baseline'].mean() - 1) * 100:.1f}%"
    ]
}

summary_df = pd.DataFrame(summary)
print(summary_df)

# Optionally, save to CSV
summary_df.to_csv("..\\Data\\dt_simulation_summary.csv", index=False)
df.to_csv("..\\Data\\dt_simulation_data.csv", index=False)

