# Ontology-Based Digital Twin for Hospitality Front-Desk Systems

This repository contains the full dataset, simulation code, and semantic artifacts used in the research paper titled:  
**“An Ontology-Based Digital Twin Framework for Human-Centered Hospitality Operations”**.

---

## 📁 Structure

```text
├── Data/
│   ├── dt_simulation_data.csv
│   ├── dt_comparison_data.csv
│   ├── ablation_study_data.csv
│   └── ...
├── Scripts/
│   ├── simulate_performance_metrics.py
│   ├── simulate_comparison_dt.py
│   ├── simulate_ablation_study.py
├── Ontology/
│   ├── hotel_ontology.owl
│   ├── reasoning_rules.swrl
│   └── queries.sparql
├── README.md
```

---

## 🧑‍💻 Requirements

Make sure Python is installed (v3.8+ recommended). Then install required libraries:
```bash
pip install numpy pandas matplotlib seaborn
```
## 🚀 Running the Simulations
1. Baseline vs. DT Performance Metrics
Simulates check-in times, efficiency, and guest satisfaction.
```bash
python Scripts/simulate_performance_metrics.py
```
2. Generic vs. Ontology-Based DT
Generates task assignment, match accuracy, and rule coverage data.
```bash
python Scripts/simulate_comparison_dt.py
```
3. Ablation Study
Simulates variants with/without Ontology, Reasoning, and Personalization layers.
```bash
python Scripts/simulate_ablation_study.py
```

Each script outputs:

* Raw .csv files for analysis
* Summary tables (mean ± std)
* Optional graphs (can be enabled)

## 📚 Semantic Artifacts
* hotel_ontology.owl: OWL 2.0 ontology defining the semantic model.
* reasoning_rules.swrl: Inference rules using SWRL.
* queries.sparql: Sample SPARQL queries used for reasoning.

## 📄 License
Released under the MIT License. See LICENSE for details.

## 📬 Contact
For questions or collaborations, please contact:
msegura@ugr.es

