# Research-MOOC-Computing-Analysis

## From Research Excellence to Teaching Excellence: Gauging Impact of Influential Research Universities on MOOC Platforms

This repository contains the datasets, documentation, and analysis resources used in the study of influential Computing researchers, university-level research strength, and Computing-related MOOC provision.

The study connects research excellence with online teaching presence by examining influential Computing researchers, their institutional affiliations, Computing subdisciplines, and the MOOC offerings of universities on major online learning platforms.

---

## Research Overview

The study investigates the relationship between research strength and online teaching presence in the Computing domain.

The analysis consists of two main components:

1. Identification and analysis of influential Computing researchers.
2. Analysis of Computing-related MOOCs offered by universities.

The two datasets are subsequently compared at the university and Computing-subdiscipline levels.

---

## Datasets

### 1. Computing Researcher Dataset

The researcher dataset is based on the Stanford/Ioannidis Top 2% Scientists dataset.

The dataset was filtered to identify researchers associated with the Computing domain and organized according to their Computing subfields and institutional affiliations.

The final processed researcher dataset contains Computing-related researcher records and supporting summaries for institutional, country, and subfield-level analysis.

### Bibliometric Indicators

The researcher analysis uses four bibliometric indicators:

- Publication Count (PC)
- Citation Count (CC)
- H-index (HI)
- Significant Research Contribution (SRC)

### Researcher Dataset Processing

The researcher data were processed to:

1. Identify Computing-related researchers.
2. Extract the required bibliometric indicators.
3. Organize researchers according to Computing subfields.
4. Associate researchers with their institutions.
5. Apply logarithmic transformation to bibliometric indicators.
6. Normalize the transformed indicators.
7. Calculate researcher influence scores.
8. Identify influential researchers.
9. Aggregate influential researchers by institution and Computing subfield.

### Researcher Dataset File

`data/researcher/Computing_Top2Percent_Researchers_2024.xlsx`

---

## 2. MOOC Dataset

The MOOC data were obtained from the following Kaggle dataset:

https://www.kaggle.com/datasets/kararhaitham/courses

The source dataset contains course information from online learning platforms.

The course data were processed using Python to identify Computing-related courses and their corresponding Computing subfields.

### MOOC Data Processing

The MOOC data were processed to:

1. Extract the course records.
2. Clean and standardize the course information.
3. Identify Computing-related courses.
4. Classify courses into Computing subfields.
5. Standardize provider and organization information.
6. Prepare the data for university-level analysis.
7. Aggregate Computing MOOCs by institution and subfield.

### MOOC Dataset File

`data/mooc/Coursera_EdX_Computing_Only.xlsx`

---

## Computing Subfields

The analysis uses the following Computing subdisciplines:

- Artificial Intelligence & Image Processing
- Networking & Telecommunications
- Software Engineering
- Computation Theory & Mathematics
- Computer Hardware & Architecture
- Information Systems
- Medical Informatics
- Distributed Computing

---

## Researcher Influence Analysis

The researcher analysis uses four bibliometric indicators:

- Publication Count (PC)
- Citation Count (CC)
- H-index (HI)
- Significant Research Contribution (SRC)

The indicators are transformed using:

`log10(X + 1)`

The transformed indicators are normalized to a 0–100 scale using the maximum transformed value.

An initial equal-weight influence score is calculated from the normalized indicators.

Mutual Information is then used to derive data-driven indicator weights for the final ResRank analysis.

The final researcher score is calculated as a weighted combination of the normalized bibliometric indicators.

Researchers above the defined influence threshold are classified as influential researchers.

---

## Institutional Analysis

After identifying influential researchers, the researchers are grouped according to their institutional affiliations.

The institutional analysis examines:

- Number of influential researchers
- Computing subfield distribution
- Institutional research strength
- Country-level distribution
- Subfield-specific institutional strength

The analysis focuses on higher education institutions and excludes non-university entities where institutional aggregation is required.

---

## MOOC Institutional Analysis

The Computing MOOC dataset is analyzed at the university/institution level.

The analysis examines:

- Total Computing MOOCs
- MOOC provision by institution
- Computing subfield distribution
- Institution–subfield relationships

The results are used to identify universities with substantial Computing-related MOOC provision.

---

## Research–MOOC Alignment

The final stage connects the two analytical components.

Researcher-based institutional strength is compared with university-level Computing MOOC provision.

The comparison is performed across the defined Computing subdisciplines to examine whether institutions with strong concentrations of influential Computing researchers also demonstrate substantial Computing-related MOOC provision.

---

## Repository Structure

```text
Research-MOOC-Computing-Analysis/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── researcher/
│   │   └── Computing_Top2Percent_Researchers_2024.xlsx
│   │
│   └── mooc/
│       └── Coursera_EdX_Computing_Only.xlsx
│
├── docs/
│
├── src/
│   ├── researcher_analysis/
│   ├── mooc_analysis/
│   └── visualization/
│
└── results/
    ├── tables/
    └── figures/
