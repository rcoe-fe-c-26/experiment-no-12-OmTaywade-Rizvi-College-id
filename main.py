# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:Om Satish Taywade
# Date:10/2/2026
num = int(input("Enter Length of Words: "))
with open ("story.txt", 'r') as f:
    content = f.read().split()
    wordList = [ i.lower() for i in content if(num == len(i))]
    wordSet = set(wordList)
    wordList2 = list(wordSet)
    print(f"Following Unique words of length 8 present: {wordList2}")
