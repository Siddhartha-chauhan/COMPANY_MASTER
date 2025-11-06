# Company Master - Maharashtra

## Aim
The aim of this project is to **convert raw open data into insightful visualizations**, telling a story about the state of company registration in Maharashtra.

---

## Raw Data Sources
| Name | Source |
|------|--------|
| Company master data of Maharashtra | [Data.gov.in](https://data.gov.in/catalog/company-master-data) |

---

## Instructions

1. Download all required datasets from the source above.  
2. Initialize a **Python project** with a separate virtual environment.  
3. All your code should be in Python and **flake8-compliant**.  
4. This project has a **dedicated repository** on GitLab/GitHub.  
5. Include a `README.md` (this file) with instructions on running the project.

---

## Requirements
- Python 3.x  
- Packages: `matplotlib`, `numpy`, `pandas`  
- Optional: `jupyter` if you want to run notebooks  

Install dependencies via:
```bash
pip install -r requirements.txt
```

---

## Project Structure
```
Company_Master_Project/
│
├── data/           # CSV files (raw datasets)
├── plots/          # Generated plots
├── src/            # Python scripts for data analysis
├── venv/           # Virtual environment
├── README.md       # Project description and instructions
└── requirements.txt
```

---

## What the Program Does

The Python scripts in this project perform the following tasks:

1. **Read the data**  
   - Load CSV and other source files as Python dictionaries or pandas DataFrames.  

2. **Process the data**  
   - Slice, dice, accumulate, and transform the data for analysis.  

3. **Generate visualizations** using `matplotlib`:

---

### 1. Histogram of Authorized Capital
- Column: `AUTHORIZED_CAP`  
- Plot intervals:
  - `<= 1L`  
  - `1L to 10L`  
  - `10L to 1Cr`  
  - `1Cr to 10Cr`  
  - `> 10Cr`  
- The x-axis uses string labels as above.  
- Intervals are adjustable to maintain a balanced plot.  

---

### 2. Bar Plot of Company Registration by Year
- Column: `DATE_OF_REGISTRATION`  
- Extract the registration year and count the number of registrations per year.  
- Plot a bar chart of `Number of Registrations` vs. `Year`.

---

### 3. Company Registration in 2015 by District
- Only consider registrations from the year **2015**.  
- Determine the district from the **zip code** (at the end of the address).  
- Count registrations per district.  
- Plot a bar chart: `Number of Registrations` vs. `District`.  
- If the plot is unbalanced, consider displaying **top districts only**.

---

### 4. Grouped Bar Plot
- Aggregate registration counts over:  
  - `Year of registration`  
  - `Principal Business Activity`  
- Plot only the **top 5 Principal Business Activities** over the **last 10 years**.  

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/COMPANY_MASTER_PROJECT.git
cd COMPANY_MASTER_PROJECT
```

2. Activate your virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the analysis scripts from `src/`:
```bash
python src/Authorized_Cap.py
python src/company_registration_per_year.py
python src/Registration_2015_by_district.py
python src/grouped_bar.py
```

5. Generated plots will be saved in the `plots/` folder.





