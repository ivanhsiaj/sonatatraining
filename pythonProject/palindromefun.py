def ispalindrome(s):
    return s==s[::-1]
s='13231'
ans=ispalindrome(s)
if ans:
    print("YES")
else:
    print("NO")