class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
    
def main():
    s = "the sky is blue"
    print(Solution().reverseWords(s)) # Output: "blue is sky the"   

if __name__ == "__main__":
    main()