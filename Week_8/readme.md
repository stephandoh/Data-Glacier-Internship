# Customer Segmentation Project

## 1. Project Overview
XYZ Bank aims to enhance its marketing campaign by delivering personalized Christmas offers to its customers. The goal is to target specific customer segments with relevant offers rather than rolling out a generic offer for everyone. ABC Analytics Company has been approached to assist with customer segmentation, with the requirement to group customers into no more than 5 segments for efficiency.

## 2. Problem Description
XYZ Bank wants to optimize its marketing strategy by delivering tailored offers to distinct customer segments. The bank seeks to uncover hidden patterns in customer behavior to facilitate this segmentation process effectively.

## 3. Data Understanding
### Dataset Context
- **Customer Demographics and Attributes**: Includes unique customer identifiers, country of residence, gender, and age.
- **Customer Relationship and Status**: Contains employment status, new customer indicators, relationship duration, and relationship types.
- **Financial Products and Services**: Comprises indicators for customer activity, gross income, and various financial products held by the customer.
- **Temporal Aspects**: Tracks key dates related to customer contracts and status.

### Data Types
- **Categorical Data**: Examples include customer demographics and relationship status.
- **Numerical Data**: Includes discrete data (e.g., age) and continuous data (e.g., gross income).
- **Date/Time Data**: Contains important date-related variables that are essential for analyzing customer engagement over time.

## 4. Challenges and Solutions
### Language Barrier
- **Problem**: Column names were in Spanish.
- **Solution**: Translated column names to English.

### High Percentage of Missing Data
- **Problem**: Columns `ult_fec_cli_1t` and `conyuemp` had over 90% missing data.
- **Solution**: Removed these columns from the dataset.

### Irrelevant Column
- **Problem**: The column `Unnamed: 0` was not useful.
- **Solution**: Dropped this column.

### Redundant Geographic Information
- **Problem**: Columns `cod_prov` and `nomprov` provided redundant data.
- **Solution**: Removed these columns to focus on relevant geographic data.

### Recency Overlap
- **Problem**: The `fecha_alta` column was unnecessary for recency analysis.
- **Solution**: Dropped the `fecha_alta` column.

### Missing Values in Categorical Columns
- **Problem**: Missing values in `sexo` and `pais_residencia`.
- **Solution**: Replaced missing values with the most frequent values in those columns.

### Missing Values in Numerical Columns
- **Problem**: Missing values in `renta`, `ind_nomina_ult1`, and `ind_nom_pens_ult1`.
- **Solution**: Replaced missing values with median values for these columns.

### Data Type Adjustments
- **Problem**: Several columns had inappropriate data types.
- **Solution**: Changed data types from float to int where appropriate.

### Date Format Correction
- **Problem**: The `fecha_dato` column was in object format.
- **Solution**: Converted `fecha_dato` to a date data type.

### Outliers in Age Column
- **Problem**: The age column had outliers above 92.
- **Solution**: Capped all outliers in the age column at 92.

### Negative Values in Seniority
- **Problem**: The `antiguedad` column had a minimum value of -999999.
- **Solution**: Capped outliers in this column to a minimum value of 0.

## 5. Conclusion
This project aims to provide XYZ Bank with effective customer segmentation strategies to enhance their marketing efforts through personalized offers. By addressing data quality issues and employing effective analysis techniques, the bank can achieve more targeted marketing campaigns.
