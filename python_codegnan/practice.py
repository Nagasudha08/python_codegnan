#travel expenses
def merge_expenses(expenses):
    totals = {}
    for category, amount in expenses:
        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount
    highest_category = max(totals, key=totals.get)
    return totals, highest_category
expenses = [("Travel", 500), ("Food", 200), ("Travel", 300)]
result, highest = merge_expenses(expenses)
print("Category-wise totals:", result)
print("Highest expense category:", highest)



#analyze_tickets

def analyze_tickets(tickets):
    total = {}
    opened = {}
    for ticket in tickets:
        category = ticket["category"]
        # Count total tickets
        total[category] = total.get(category, 0) + 1
        # Count open tickets
        if ticket["status"] == "Open":
            opened[category] = opened.get(category, 0) + 1
    print("Total tickets:", total)
    print("Open tickets:", opened)
tickets = [
    {"ticket_id": 1, "category": "Technical", "status": "Open"},
    {"ticket_id": 2, "category": "Billing", "status": "Closed"},
    {"ticket_id": 3, "category": "Technical", "status": "Open"},
    {"ticket_id": 4, "category": "Billing", "status": "Open"}
]
analyze_tickets(tickets)
