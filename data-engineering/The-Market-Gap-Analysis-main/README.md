# Sugar Trap: Market Gap Analysis

## A. Executive Summary

This project analyses a 500,000-row sample of the Open Food Facts dataset to identify nutritional opportunities for a new healthy-snacking product line. Using thresholds of more than 12g of protein and less than 4.31g of sugar per 100g, the analysis identified 83,328 qualifying products across all categories. Within the Snacks category, 6,190 out of 55,836 products met these criteria, representing 11.09% of snack products analysed. Although Dairy had the highest opportunity rate (34.69%), Snacks was selected as the strategic focus because it directly aligns with the client's healthy-snacking objective. The analysis also identified Milk, Wheat/Gluten and Soy as the most frequent ingredient keyword matches among qualifying products.

---

## B. Project Links

Notebook: (https://github.com/JennyRJ/AmaliTech-DEG-Project-based-challenges/blob/main/data-engineering/The-Market-Gap-Analysis-main/notebooks/01_Sugar_Trap_Analysis.ipynb)

Dashboard: (https://amalitech-deg-project-based-challenges-k2mi4rbk88czxcitfskdm3.streamlit.app/)

Presentation: (https://github.com/JennyRJ/AmaliTech-DEG-Project-based-challenges/blob/main/data-engineering/The-Market-Gap-Analysis-main/presentation/Sugar_Trap_Market_Gap_Presentation.pdf)

Optional Video Walkthrough: N/A

---

## C. Technical Explanation

### Data Cleaning

A sample of 500,000 rows was extracted from the Open Food Facts dataset using DuckDB. Empty product names were treated as missing values, and rows without product names were removed. Nutritional values outside the 0–100g per 100g range were treated as invalid and converted to missing values. Products with missing sugar or protein values were excluded from the nutritional analysis rather than having their values imputed. The resulting dataset contained 445,136 products with usable sugar and protein values.

### Candidate's Choice

An additional bar chart was created to compare the number of products meeting the high-protein, low-sugar criteria across the seven product categories. This complements the opportunity-rate analysis by showing the actual number of qualifying products in each category, helping the client compare existing product availability when considering potential areas for new product development.
