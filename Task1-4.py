"""
The rebel scientists have been analyzing captured alien samples. They have discovered rules that can identify whether a DNA sequence is alien or human:

Alien DNA always ends with "XZ"

OR contains the substring "QW"

OR has a total length greater than 12 characters

Write a function detect_aliens(dna_list) that separates sequences into two lists: Aliens and Humans.
"""
def detect_aliens(dna_list):
    aliens = []
    human = []
    for i in dna_list:
        if i.endswith("XZ") or "QW" in i or len(i)>12:
            aliens.append(i)
        else:
            human.append(i)
    return aliens,human

def main():
    sq = input("Enter dna sequences:").split()
    alien,human = detect_aliens(sq)
    print(alien)
    print(human)
main()