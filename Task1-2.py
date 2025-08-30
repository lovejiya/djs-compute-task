"""
The Resistance must prioritize rations for children and the elderly. Unfortunately, the refugee registration team is overwhelmed, and the age records are a mess — some are written as strings, some have accidental letters, and others are fine.

Your job is to write a function clean_and_sort_ages(data) that:

Removes invalid entries (anything that isn’t purely digits).

Converts valid entries into integers.

Returns a clean, sorted list of ages in ascending order."""

def clean_and_sort_ages(data):
    ans = []
    for i in data:
        if str(i).isdigit():
            ans.append(i)
    
    ans.sort()
    return ans

def main():
    inp = str(input("Enter a list of entries:")).split()
    ans = clean_and_sort_ages(inp)
    print(ans)

main()