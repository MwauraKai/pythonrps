def is_palindrome(string):
   
    # Remove spaces and convert to lowercase for consistent comparison
    cleaned_string = string.replace(" ", "").lower()
    
    # Compare the string with its reverse
    if cleaned_string == cleaned_string[::-1]:
        return True
    return False

word = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")

#Anagrams
def are_anagrams(string1, string2):
   
    # Remove spaces, convert to lowercase, and sort characters
    cleaned_string1 = sorted(string1.replace(" ", "").lower())
    cleaned_string2 = sorted(string2.replace(" ", "").lower())
    
    # Compare the sorted versions of both strings
    return cleaned_string1 == cleaned_string2


word1 = input("Enter the first string: ")
word2 = input("Enter the second string: ")
if are_anagrams(word1, word2):
    print(f"'{word1}' and '{word2}' are anagrams.")
else:
    print(f"'{word1}' and '{word2}' are not anagrams.")
