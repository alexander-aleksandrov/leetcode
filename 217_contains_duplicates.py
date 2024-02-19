def containsDuplicate(nums):
    return len(nums) != len(set(nums))

def main():
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

if __name__ == "__main__":
    main()