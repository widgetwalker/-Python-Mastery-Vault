import csv
from collections import defaultdict
from datetime import datetime, timedelta

def read_transactions(csv_file):
    transactions = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert types
            row['Amount'] = float(row['Amount'])
            row['Class'] = int(row['Class'])
            transactions.append(row)
    return transactions

def detect_fraud(transactions):
    frauds = []
    for tx in transactions:
        if tx['Class'] == 1:
            frauds.append(tx)
        elif tx['Amount'] > 5000:
            frauds.append(tx)
    return frauds

if __name__ == "__main__":
    csv_file = input("Enter the path to the transactions CSV file: ")
    transactions = read_transactions(csv_file)
    frauds = detect_fraud(transactions)

    if not frauds:
        print("No fraud detected.")
    else:
        print("Potential fraud detected:")
        for tx in frauds:
            print(f"Time: {tx['Time']}, Amount: {tx['Amount']}, Class: {tx['Class']}")
