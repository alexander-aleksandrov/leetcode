from ast import List


class Solution:
    def longestCommonPrefix(self, strs): 
        prefix = ""
        if not strs:
            return prefix
        elif len(strs) == 1:
            return strs[0]
        char = 0
        while True:
            new_prefix = ""
            for i in range(len(strs)):
                if char >= len(strs[i]):
                    return prefix
                if not new_prefix:
                    new_prefix = strs[i][char]
                if char >= len(strs[i]) or strs[i][char] != new_prefix:
                    return prefix
            else:
                prefix += new_prefix
            char += 1
        

                

def main():
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs)) # Output: "fl"

if __name__ == "__main__":
    main()
            
