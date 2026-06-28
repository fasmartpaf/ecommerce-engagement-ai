# Enhancing User Engagement in E-Commerce Through an Advanced AI Framework

**Implementation & Results — Fareena Afzal (MSSE)**

This repository contains the **implementation and results** of an MSSE research project on understanding and predicting customer engagement in e-commerce using statistical analysis, machine learning, and customer segmentation. It holds the code, dataset, generated figures, and machine-readable results — the artifacts behind the analysis.

---

## Overview

The research analyzes customer shopping behavior to:

- Understand purchasing patterns across demographics, products, and seasons
- Predict customer engagement using supervised machine learning
- Discover hidden customer segments through unsupervised clustering
- Identify the key drivers of engagement using explainable AI

The work is organized into three analytical stages: **(1)** exploratory statistical analysis, **(2)** machine-learning–based engagement prediction, and **(3)** customer segmentation with feature-importance analysis.

## Dataset

The analysis uses a customer shopping-behavior dataset (`shopping_behavior.csv`) of retail transactions. Each record describes one customer and includes:

Customer ID, Age, Gender, Item Purchased, Category, Purchase Amount (USD), Location, Size, Color, Season, Review Rating, Subscription Status, Discount Applied, Previous Purchases, Payment Method, and Frequency of Purchases.

## Methodology and Results

### Stage 1 — Statistical Analysis
Distribution analysis of every numeric and categorical variable, plus a correlation heatmap of purchasing-behavior variables. See `figures/stage1_statistics/` and `results/stage1_statistics/`.

### Stage 2 — Engagement Prediction (Machine Learning)
An engagement score was derived from customer activity and used as a prediction target. Four classifiers were trained and compared:

| Model | Accuracy |
|---|---|
| Decision Tree | 79% |
| Random Forest | 83% |
| Logistic Regression | 82% |
| K-Nearest Neighbors | 80% |

Confusion matrices, the model-accuracy comparison, and the Random Forest feature-importance plot are in `figures/stage2_ml/`; numeric results are in `results/stage2_ml/`.

> Note: Random Forest achieved the highest accuracy (83%), followed by Logistic Regression (82%) and KNN (80%), with Decision Tree at 79%.

### Stage 3 — Customer Segmentation
Clustering grouped customers into distinct engagement segments, profiled by age, purchase amount, review rating, previous purchases, and engagement score. Cluster scatter plots, distributions, and feature-importance heatmaps are in `figures/stage3_segmentation/`; cluster profiles and insights are in `results/stage3_segmentation/`.

## Repository Structure

```
.
├── README.md
├── LICENSE
├── data/
│   └── shopping_behavior.csv            # Primary dataset
├── code/                                # Analysis & artifact-generation scripts
├── figures/                             # All figures, by stage
│   ├── stage1_statistics/
│   ├── stage2_ml/
│   └── stage3_segmentation/
├── results/                             # Machine-readable results (XML), by stage
│   ├── stage1_statistics/
│   ├── stage2_ml/
│   └── stage3_segmentation/
└── reports/                             # Research summaries & figure captions
```

## License

Released under the MIT License — see [`LICENSE`](LICENSE).
