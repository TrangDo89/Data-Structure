from stack import Stack

def isPalindrome(sentence):          
    """Returns True if sentence is a palindrome
    or False otherwise."""
    stk = Stack() # Creates a stack called stk.

    # *** Write your code here ***
# create new string to get the sentence only alphabet
# use loop to get push the letter in stack
    new_sentence = ""
    for c in sentence:
        if (c.isalpha()) == True:
            stk.push(c.upper())
            new_sentence += c.upper()

#use loop to pop the letter
    count = 0
    for c in new_sentence:
        if c == stk.pop():
            count +=1

    if(count != len(new_sentence)):
        return False

    return True
# *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")

main()
