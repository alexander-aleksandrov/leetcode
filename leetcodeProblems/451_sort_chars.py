class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        for i in s: 
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
        res = ""
        for char, value in dic.items():
            res += char*value
        return res