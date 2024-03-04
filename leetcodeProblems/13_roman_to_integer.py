def main():
    print(roman_to_integer('XIV'))
    print(roman_to_integer('XX'))
    print(roman_to_integer('IV'))
    print(roman_to_integer('IX'))
    print(roman_to_integer('LVIII'))


def roman_to_integer(s: str) -> int:
    #make a dict for symbols 
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #initialize the result
    result = 0
    for i in range(len(s)):
        if i == len(s) - 1:
            result += symbols[s[i]]
            break
        if symbols[s[i]] < symbols[s[i+1]]:
            result -= symbols[s[i]]
        else:
            result += symbols[s[i]]
    return result
        

if __name__ == "__main__":
    main()      
