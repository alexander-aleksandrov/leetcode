class Solution:
    def fullJustify(self, words , maxWidth):
        res = []
        cur = []
        num_of_letters = 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += " "
                res.append("".join(cur))
                cur = []
                num_of_letters = 0
            cur += [w]
            num_of_letters += len(w)
        res.append(" ".join(cur).ljust(maxWidth))
        return res
    
def main():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(Solution().fullJustify(words, maxWidth)) # Output: ["This    is    an", "example  of text", "justification.  "]

if __name__ == "__main__":
    main()