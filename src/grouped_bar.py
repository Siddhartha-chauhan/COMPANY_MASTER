import csv
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# -----------------------------
# Read CSV function
# -----------------------------
def read(file_path, sep=','):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=sep)
        data = [row for row in reader]
    return data

# -----------------------------
# Calculate top categories per year
# -----------------------------
def calculate_top_per_year(data, start_year=2015, current_year=2025, top_n=5):
    year_category_counts = defaultdict(Counter)

    for row in data:
        date = row.get("CompanyRegistrationdate_date")
        category = row.get("CompanyIndustrialClassification")

        # Skip rows with missing date or category
        if not date or not category:
            continue

        date = date.strip()
        category = category.strip()
        if not date or not category:
            continue

        try:
            year = int(date[:4])
        except ValueError:
            continue

        if start_year <= year <= current_year:
            year_category_counts[year][category] += 1

    # Keep only top_n categories per year
    top_categories_per_year = {}
    for year, counts in year_category_counts.items():
        top_categories_per_year[year] = counts.most_common(top_n)

    return top_categories_per_year, list(range(start_year, current_year + 1))

# -----------------------------
# Plot grouped bar chart (x-axis = years)
# -----------------------------


def plot_grouped_bar(data, years):
    width = 0.15
    fig, ax = plt.subplots(figsize=(14, 6))

    # Get union of all industries for consistent colors across years
    all_industries = sorted(set(ind for year_data in data.values() for ind, _ in year_data))
    color_map = {ind: plt.cm.tab20(i) for i, ind in enumerate(all_industries)}  # fixed color per industry

    for i, year in enumerate(years):
        year_data = data.get(year, [])
        industries = [ind for ind, _ in year_data]
        counts = [count for _, count in year_data]

        # positions for bars within the year
        x_positions = [i + j*width for j in range(len(industries))]
        bars = ax.bar(x_positions, counts, width, color=[color_map[ind] for ind in industries])

        # Add count labels
        for bar, count in zip(bars, counts):
            ax.text(bar.get_x() + bar.get_width()/2, count + 1, str(count), ha='center', va='bottom', fontsize=8)

    # x-ticks in the middle of grouped bars
    mid_positions = [i + width*2 for i in range(len(years))]  # 5 bars per year → middle = 2
    ax.set_xticks(mid_positions)
    ax.set_xticklabels(years)
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Registrations")
    ax.set_title("Top 5 Company Categories per Year (Last 10 Years)")

    # Legend with correct colors
    patches = [mpatches.Patch(color=color_map[ind], label=ind) for ind in all_industries]
    ax.legend(handles=patches, title="Industries", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    os.makedirs("plots", exist_ok=True)
    plt.savefig("plots/grouped_bar_top_categories_per_year.png")
    plt.show()


# -----------------------------
# Execute function
# -----------------------------
def execute(file_path, top_n=5, start_year=2015, current_year=2025):
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    data = read(file_path)
    top_categories_per_year, years = calculate_top_per_year(data, start_year, current_year, top_n)
    plot_grouped_bar(top_categories_per_year, years)

# -----------------------------
# Usage
# -----------------------------
file_path = "data/COMPANY_MASTER.csv"  # adjust path if needed
execute(file_path, top_n=5)
