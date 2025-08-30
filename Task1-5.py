"""
The Resistance intercepted classified intelligence files about alien commanders. Each commander is represented as a dictionary:

{"name": "Xeron", "rank": 4, "missions": 20}

Your task is to help the rebel analysts make sense of the data:

Write a function sort_by_missions(commanders) → sorts the list by missions in descending order.

Write a function sort_by_rank(commanders) → sorts the list by rank in ascending order.
"""
def sort_by_missions(commanders):
    return sorted(commanders, key=lambda c: c["missions"], reverse=True)

def sort_by_rank(commanders):
    return sorted(commanders, key=lambda c: c["rank"])

