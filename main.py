# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder:Om Satish Taywade
# Date:10/2/2026

print("--- Extracting Words from Text File ---\n")
file = "story.txt"
num = int(input("Enter Length of Words: "))
with open (file, 'r') as f:
    content = f.read().split()
    wordList = [ i for i in content if(num == len(i))]
    print(f"Following Unique words of length 8 present: {wordList}")
