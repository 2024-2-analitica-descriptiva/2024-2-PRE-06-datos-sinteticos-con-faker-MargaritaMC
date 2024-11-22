"""Generate fake data with Faker."""

import csv
import os

from faker import Faker
from tqdm import tqdm  # type: ignore

fake = Faker()

def generate_fake_drivers(n):
    """Generate n fake records.

    Each record has the following fields:
    - driverId: sequential int (unique) beigning in 10
    - name: fake name
    - ssn: fake ssn
    - location: fake address
    - certified: 'Y' or 'N'
    - wage-plan: 'miles' or 'hours'

    """
    drivers = []
    for i in tqdm(range(n), desc="drivers"):
        record = {
            "driverId": i + 10,
            "name": fake.name(),
            "ssn": fake.ssn(),
            "location": fake.address(),
            "certified": fake.random_element(elements=("Y", "N")),
            "wage-plan": fake.random_element(elements=("miles", "hours")),
        }
        drivers.append(record)

    return drivers


def save_fake_data(fake_data, filename):
    """Save fake data to a CSV file."""

    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fake_data[0].keys())
        writer.writeheader()
        for record in fake_data:
            writer.writerow(record)



if __name__ == "__main__":
    # Generate fake data
    fake_drivers = generate_fake_drivers(100)

     # Save fake data to CSV files
    if not os.path.exists("files"):
        os.makedirs("files")
    save_fake_data(fake_drivers, "files/drivers.csv")
