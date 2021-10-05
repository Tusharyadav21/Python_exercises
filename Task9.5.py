# Check a character is Vowel or Consonant

n = input("Enter a Character : ")
vowels = ('A', 'E', 'I', 'O', 'U')
n = n.upper()

if n in vowels:
    print(n," is a Vowel.")
else:
    print(n," is a consonant.")
