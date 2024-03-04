def repeatedCharacter(s: str) -> str:
        d = {}
        for c in s:
            if c in d and d[c] == 1:
                return c
            else:
                d[c] = 1       
        else:
            return -1
             
def main():
    s = "abacabadabacaba"
    print(repeatedCharacter(s))

if __name__ == "__main__":
    main()             