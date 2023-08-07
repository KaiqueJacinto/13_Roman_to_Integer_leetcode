class Solution:
    def romanToInt(self, s: str) -> int:
        letras = ['I','V','X','L','C','D','M']
        num = [1,5,10,50,100,500,1000]
        valor = 0
        j = 0
        for i in range(len(s)):
            if i+j+1 < len(s):
                if num[letras.index(s[i+j])] < num[letras.index(s[i+j+1])]:
                    valor += num[letras.index(s[i+j+1])]-num[letras.index(s[i+j])]
                    j +=1
                else:
                    valor += num[letras.index(s[i+j])]
            elif i+j < len(s):
                valor += num[letras.index(s[i+j])]
        return valor
