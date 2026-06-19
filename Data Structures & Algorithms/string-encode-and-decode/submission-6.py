class Solution:

    def encode(self, strs: List[str]) -> str:
        
        s = ""
        add = []

        for i, string in enumerate(strs):
            add.append("#" + str(len(string)) + "#" + string)
            s = s + add[i]

        return s 

    def decode(self, s: str) -> List[str]:

        arr = []
        i = 0
        j = 0

        while i != len(s):

            if s[i] == "#" and i != len(s) - 1:
                j = i+1
                k = 0
                while j != "#" and s[j].isdigit():
                    k = 10*k + int(s[j])
                    j += 1
                arr.append(s[j+1:j+1+k])
                i = j + k + 1
                continue
            
            i += 1
            

        return arr


