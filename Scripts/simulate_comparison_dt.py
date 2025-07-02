import numpy as np
import pandas as pd

# Set random seed
np.random.seed(123)
n_runs = 1000

# Simulated metrics
data = {
    'assignment_time_generic': np.random.normal(loc=2.69, scale=0.4, size=n_runs),
    'assignment_time_ontology': np.random.normal(loc=2.09, scale=0.3, size=n_runs),
    'match_accuracy_generic': np.random.normal(loc=68.4, scale=6.1, size=n_runs),
    'match_accuracy_ontology': np.random.normal(loc=89.9, scale=4.5, size=n_runs)
}

df = pd.DataFrame(data)

# Manual and inferred rule counts are fixed (non-simulated)
rule_counts = {'Generic DT': 12, 'Ontology-Based DT': 34}

# Summary statistics
summary = {
    'Metric': ['Avg. Task Assignment Time (s)', 'Contextual Match Accuracy (%)', 'Service Rule Coverage (#rules)'],
    'Generic DT': [
        f"{df['assignment_time_generic'].mean():.2f} ± {df['assignment_time_generic'].std():.2f}",
        f"{df['match_accuracy_generic'].mean():.2f} ± {df['match_accuracy_generic'].std():.2f}",
        f"{rule_counts['Generic DT']} (manual)"
    ],
    'Ontology-Based DT': [
        f"{df['assignment_time_ontology'].mean():.2f} ± {df['assignment_time_ontology'].std():.2f}",
        f"{df['match_accuracy_ontology'].mean():.2f} ± {df['match_accuracy_ontology'].std():.2f}",
        f"{rule_counts['Ontology-Based DT']} (inferred)"
    ],
    'Improvement (%)': [
        f"{(1 - df['assignment_time_ontology'].mean() / df['assignment_time_generic'].mean()) * 100:.1f}%",
        f"{(df['match_accuracy_ontology'].mean() / df['match_accuracy_generic'].mean() - 1) * 100:.1f}%",
        f"{(rule_counts['Ontology-Based DT'] / rule_counts['Generic DT'] - 1) * 100:.1f}%"
    ]
}

summary_df = pd.DataFrame(summary)
print(summary_df)

# Save outputs
summary_df.to_csv("..\\Data\\dt_comparison_summary.csv", index=False)
df.to_csv("..\\Data\\dt_comparison_data.csv", index=False)
