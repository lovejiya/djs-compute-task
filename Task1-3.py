"""
 Supply crates are dropped at night by allied aircraft, but due to enemy fire, crates often scatter and the Resistance ends up with piles of mixed supplies. Each crate is labeled with a code:

"MED-###" for medical supplies

"FOOD-###" for food

"WPN-###" for weapons

Write a function count_supplies(supplies) that counts how many of each type the rebels have.
"""
def count_supplies(supplies):
    ans = {"FOOD":0,"MED":0,"WPN":0}
    for i in supplies:
        if i.startswith("FOOD"):
            ans["FOOD"]+=1
        if i.startswith("WPN"):
            ans["WPN"]+=1
        if i.startswith("MED"):
            ans["MED"]+=1
    return ans

def main():
    sup = input("Enter supplies:").split()
    ans = count_supplies(sup)
    print(ans)
main()