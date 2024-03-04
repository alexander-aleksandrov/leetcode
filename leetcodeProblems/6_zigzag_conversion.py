class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ""
        if numRows == 1 or numRows >= len(s):
            return s
        row = 0
        while True:
            for i in range(row, len(s), numRows*2-2):
                res += s[i]
                current_index = i + (numRows-1-row)*2
                if row != 0 and row != numRows-1 and current_index < len(s):
                    res += s[current_index]
            row += 1
            if row == numRows:
                break
        return res
    
def main():
    s = "PAYPALISHIRING"
    numRows = 4
    print(Solution().convert(s, numRows)) # Output: "PAHNAPLSIIGYIR"

if __name__ == "__main__":
    main()
        