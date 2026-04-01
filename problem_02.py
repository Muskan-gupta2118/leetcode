class solution(object):
    def isPalindrome(self ,x):
        #Negative numbers are not a palindrome
        if x < 0:
            return False
        return str(x)==str(x)[::-1];
obj=solution();
x=int(input("Enter number : "))
print(obj.isPalindrome(x))