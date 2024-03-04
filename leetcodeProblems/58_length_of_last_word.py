class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
        
def main():
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))

if __name__ == "__main__":  
    main()