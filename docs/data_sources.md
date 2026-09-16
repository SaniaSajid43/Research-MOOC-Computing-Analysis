# Data Sources

## 1. Researcher Dataset

The researcher dataset is based on the Stanford/Ioannidis Top 2% Scientists dataset. The dataset was used to identify influential researchers in the Computing domain and to analyze their institutional affiliations and Computing subdisciplines.

The researcher records were filtered to retain Computing-related researchers and the following bibliometric indicators were used:

- Publication Count (PC)
- Citation Count (CC)
- H-index (HI)
- Significant Research Contribution (SRC)

Source:
https://doi.org/10.17632/btchxktzyw/8

## 2. MOOC Dataset

The MOOC dataset was obtained from the Kaggle Courses dataset and was used for the analysis of Computing-related courses offered through online learning platforms.

Source:
https://www.kaggle.com/datasets/kararhaitham/courses

The MOOC data were extracted and prepared using Python-based data processing scripts. The resulting course records were cleaned, standardized, and used for university-level and Computing subdiscipline analysis.

## Data Processing

The research dataset and MOOC dataset were processed separately before the final analysis.

For the researcher dataset, the processing included:

1. Identification of Computing-related researchers.
2. Selection of the required bibliometric indicators.
3. Data cleaning and validation.
4. Logarithmic transformation of bibliometric indicators.
5. Normalization of the transformed indicators.
6. Calculation of researcher influence scores.
7. Identification of influential researchers.
8. Aggregation by university and Computing subdiscipline.

For the MOOC dataset, the processing included:

1. Extraction of the course data using Python.
2. Data cleaning and standardization.
3. Identification of Computing-related courses.
4. Standardization of institution and platform information.
5. Assignment of Computing subdisciplines.
6. Aggregation of courses by institution and subdiscipline.

## Reproducibility

The Python scripts used for data extraction and analysis are included in this repository. The original datasets are referenced through their respective sources rather than redistributed where redistribution rights are not established.
