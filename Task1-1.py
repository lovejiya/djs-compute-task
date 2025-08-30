"""The alien invaders have begun intercepting resistance transmissions. To counter this, the rebels have adopted a simple text-based encryption method:

Every alternate word in a sentence is reversed.

The first word stays as it is, the second is reversed, the third stays as it is, the fourth is reversed, and so on.

eg: Input: "We strike at dawn tomorrow" Output: "We ekirts at nwad tomorrow"

Write a function encrypt_message(message) that takes in a sentence and returns the encrypted version."""

def encrypt_message(message):
    count = 1
    ans = ""
    for i in message.split():
        if count%2==0:
            i = i[::-1]
        ans+= " "+i
        count+=1
    return ans

def main():
    msg = input("Enter a message:")
    ans = encrypt_message(msg)
    print(ans)

main()
