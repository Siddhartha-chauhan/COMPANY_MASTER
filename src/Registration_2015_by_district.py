import csv
import re
from collections import Counter
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ READ FUNCTION
# -----------------------------
def read(file_path, sep=','):
    """Read CSV file and return list of dicts"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=sep)
        return [row for row in reader]


# -----------------------------
# 2️⃣ CALCULATE FUNCTION
# -----------------------------
def calculate(company_data, zipcode_data, year='2015'):
    """Count how many companies registered in a given year per district"""

    # Step 1: Map ZIP codes → Districts
    zip_to_district = {}
    for row in zipcode_data:
        zip_code = row["ZipCode"].replace(" ", "")  # remove spaces if any
        district = row["District"]
        zip_to_district[zip_code] = district

    # Step 2: Count company registrations per district
    district_counts = Counter()

    for row in company_data:
        date = row.get("CompanyRegistrationdate_date", "")
        address = row.get("Registered_Office_Address", "")

        # Only consider companies registered in the given year
        if not date.startswith(year):
            continue

        # Step 3: Find ZIP codes (handle formats like 400049 or 400 049)
        zip_codes = re.findall(r"\b\d{3}\s?\d{3}\b", address)

        # Step 4: Find matching district and count
        for z in zip_codes:
            z_clean = z.replace(" ", "")  # normalize ZIP (e.g. 400 049 → 400049)

            # Skip fake ZIPs
            if z_clean in {"000000", "999999"}:
                continue

            if z_clean in zip_to_district:
                district = zip_to_district[z_clean]
                district_counts[district] += 1
                break  # count only one ZIP per company

    return district_counts


# -----------------------------
# 3️⃣ PLOT FUNCTION
# -----------------------------
def plot(district_counts):
    """Plot bar chart of number of registrations by district"""

    # If too many districts, show top 10 for balance
    if len(district_counts) > 10:
        district_counts = dict(district_counts.most_common(10))

    plt.figure(figsize=(10, 6))
    plt.bar(district_counts.keys(), district_counts.values())
    plt.title("Company Registrations by District (2015)")
    plt.xlabel("District")
    plt.ylabel("Number of Registrations")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig("plots/company_registrations_2015_by_district.png")

    plt.show()


# -----------------------------
# 4️⃣ EXECUTE FUNCTION
# -----------------------------
def execute():
    """Run the entire process"""
    # Read data
    company_data = read("data/COMPANY_MASTER.csv")
    zipcode_data = read("data/zipcode_district.csv")

    # Calculate and plot
    district_counts = calculate(company_data, zipcode_data, year="2015")
    plot(district_counts)


# -----------------------------
# 5️⃣ MAIN CALL
# -----------------------------
if __name__ == "__main__":
    execute()
