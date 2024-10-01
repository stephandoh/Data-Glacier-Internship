# Dataset Cleaning and Preprocessing Report

This document outlines the challenges encountered while preparing the dataset for analysis and the corresponding solutions applied to resolve them. The primary goal was to clean and preprocess the data to ensure accuracy and consistency for analysis.

## Challenges and Solutions

### 1. Language Barrier
   - **Problem**: The dataset contained column names in Spanish, making it difficult to interpret the data.
   - **Solution**: All column names were translated from Spanish to English to improve comprehension.

### 2. High Percentage of Missing Data
   - **Problem**: The columns `ult_fec_cli_1t` (latest date as primary customer) and `conyuemp` (spouse employee indicator) had over 90% missing data, making them ineffective for analysis.
   - **Solution**: These columns were removed from the dataset to prevent skewed analysis results.

### 3. Irrelevant Column
   - **Problem**: The column `Unnamed: 0` did not provide any useful information.
   - **Solution**: This column was dropped to streamline the dataset and remove unnecessary data.

### 4. Redundant Geographic Information
   - **Problem**: The columns `cod_prov` (province code) and `nomprov` (province name) provided redundant information, especially as the country-level data was more relevant.
   - **Solution**: These columns were removed to focus on the more pertinent geographic data.

### 5. Recency Overlap
   - **Problem**: The `fecha_alta` (signup date) column overlapped with the `antiguedad` (seniority) column in determining customer recency.
   - **Solution**: The `fecha_alta` column was removed, as the `antiguedad` column more effectively captured the required information.

### 6. Missing Values in Categorical Columns
   - **Problem**: The categorical columns `sexo` (gender) and `pais_residencia` (country of residence) contained missing values.
   - **Solution**: Missing values in these columns were replaced with the most frequent value (mode) to maintain data integrity.

### 7. Missing Values in Numerical Columns
   - **Problem**: The columns `renta` (income), `ind_nomina_ult1` (payroll product indicator), and `ind_nom_pens_ult1` (pension nomination product indicator) had missing values.
   - **Solution**: Missing values were replaced with the median value for these numerical columns, minimizing the impact of potential outliers.

### 8. Data Type Adjustments
   - **Problem**: Some columns had inappropriate data types, such as floats where integers were more suitable.
   - **Solution**: The data types were adjusted, converting columns like `ind_empleado` (employee indicator) and `indresi` (resident indicator) from float to integer.

### 9. Date Format Correction
   - **Problem**: The `fecha_dato` (data date) column was in an object format rather than a proper date format.
   - **Solution**: The `fecha_dato` column was converted to a date format for accurate temporal analysis.

### 10. Outliers in Age Column
   - **Problem**: The `age` column contained unrealistic outliers, with a maximum age of 116 and values above the upper bound of 92.
   - **Solution**: Outliers in the `age` column were capped at the upper bound of 92 to ensure realistic and meaningful values.

### 11. Negative Values in Seniority
   - **Problem**: The `antiguedad` (seniority) column had a nonsensical minimum value of -999999.
   - **Solution**: After investigation, outliers were capped, and the minimum value was set to 0 to ensure all values were reasonable.

---

By applying these cleaning steps, the dataset was made more consistent, interpretable, and ready for analysis. This preprocessing ensures the accuracy and reliability of insights drawn from the data.
