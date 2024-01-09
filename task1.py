class Solution(object):
    def romanToInt(self, s):
        s=input("Enter the roman number: ")
        dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        output=0
        for i in s :
            output+=dictionary[i]
        return output
print(Solution().romanToInt(s))