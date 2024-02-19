from itertools import permutations


def generate_parenthesese(n):
    nums_combinations = []
    # generate all combinations of numbers that can be a sum of n 
    def backtrack(remaining, combination, start):
        if remaining == 0:
            nums_combinations.append(combination.copy())
            return
        elif remaining < 0:
            return

        for i in range(start, n + 1):
            combination.append(i)
            backtrack(remaining - i, combination, i)  # Allow same number to be used
            combination.pop()  # Backtrack

    backtrack(n, [], 1)

    def generate_permutations_for_combinations(combinations):
        all_permutations = []

        for combination in combinations:
            perms = set(permutations(combination))
            all_permutations.extend(perms)

        return [list(perm) for perm in all_permutations] 

    nums_combinations = generate_permutations_for_combinations(nums_combinations)
    #generate parentheses according to numbers
    parentheses = []
    for combination in nums_combinations:
        comb = []
        for number in combination:
            comb.append("(" * number + ")" * number)
        parentheses.append("".join(comb))
    return parentheses

def main():
    generate_parenthesese(3) 
    print(generate_parenthesese(3)) ["((()))","(()())","(())()","()(())","()()()"]

if __name__ == "__main__":
    main()