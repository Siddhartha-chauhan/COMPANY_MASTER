import csv
import matplotlib.pyplot as plt

# -----------------------------
# Read function
# -----------------------------
def read(file_path, sep=','):
    """Read CSV file and return list of dicts"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=sep)
        data = [row for row in reader]
    return data

# -----------------------------
# Calculate function
# -----------------------------
def calculate(data):
    """Count how many companies registered each year"""
    year_counts = {}

    for row in data:
        date = row.get("CompanyRegistrationdate_date", "")
        if date:
            year = date[:4]  # extract first 4 chars (YYYY)
            if year.isdigit():
                year_counts[year] = year_counts.get(year, 0) + 1

    return dict(sorted(year_counts.items()))  # sort by year

# -----------------------------
# Plot function
# -----------------------------
def plot(year_counts):
    """Plot bar chart of company registrations per year"""
    years = list(year_counts.keys())
    counts = list(year_counts.values())

    plt.figure(figsize=(10, 5))
    plt.bar(years, counts, color='gold', edgecolor='black')
    plt.xlabel("Year of Registration")
    plt.ylabel("Number of Companies")
    plt.title("Company Registrations by Year")

    # Show only every 2nd or 3rd year on x-axis (to avoid clutter)
    plt.xticks(ticks=range(0, len(years), max(1, len(years)//15)), 
               labels=[years[i] for i in range(0, len(years), max(1, len(years)//15))],
               rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig("plots/company_registrations_by_year.png")
    plt.show()

# -----------------------------
# Execute function
# -----------------------------
def execute():
    data = read("data/COMPANY_MASTER.csv")
    year_counts = calculate(data)
    plot(year_counts)

# Direct call
execute()
