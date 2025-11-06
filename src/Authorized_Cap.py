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
    """Count number of companies in each Authorized Capital category"""
    categories = {
        "<= 1L": 0,
        "1L to 10L": 0,
        "10L to 1Cr": 0,
        "1Cr to 10Cr": 0,
        "> 10Cr": 0
    }

    for row in data:
        cap = float(row["AuthorizedCapital"])  # directly access and convert

        if cap <= 1_00_000:
            categories["<= 1L"] += 1
        elif cap <= 10_00_000:
            categories["1L to 10L"] += 1
        elif cap <= 1_00_00_000:
            categories["10L to 1Cr"] += 1
        elif cap <= 10_00_00_000:
            categories["1Cr to 10Cr"] += 1
        else:
            categories["> 10Cr"] += 1

    return categories

# -----------------------------
# Plot function
# -----------------------------
def plot(categories):
    """Plot Authorized Capital histogram"""
    labels = list(categories.keys())
    values = list(categories.values())

    plt.bar(labels, values, color='orange', edgecolor='black')
    plt.xlabel("Authorized Capital")
    plt.ylabel("Number of Companies")
    plt.title("Histogram of Authorized Capital")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plots/authorized_capital_histogram.png", dpi=300)
    plt.show()

# -----------------------------
# Execute function
# -----------------------------
def execute():
    data = read("data/COMPANY_MASTER.csv")
    categories = calculate(data)
    plot(categories)

# Direct call
execute()
