#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only.


'''def lengthOfLastWord(s: str) -> int:
    words = s.strip().split()
    return len(words[-1]);
s = "Hello World"    '''

def lengthOfLastWord(s: str) -> int:
    length = 0
    i = len(s) - 1

    # skip trailing spaces
    while i >= 0 and s[i] == ' ':
        i -= 1

    # count last word
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    return length
s = "   fly me   to   the moon  "
print(lengthOfLastWord(s))