def num_Adding():
    num_Add = int(input("Enter number to add: "))
    if num_Add in nums:
        print("Number is already added.")
        num_Adding()
    nums.append(num_Add)
    if num_Add in nums:
        print("Successfully added!")
    elif num_Add not in nums:
        print("Error 1")
    restart = input("Add another number? ")
    if restart in ("Yes","yes"):
        num_Adding()
    if restart in ("No", "no"):
        length = len(nums)
        print("You have added " + str(length) + " numbers")
        num_Guessing()
    
    else:
         print("Invalid entry. (Type yes or no) ")
         num_Adding()



num_Guessed = 0
def num_Guessing():
    num_Guess = int(input("Guess a number: "))
    global num_Guessed
    if num_Guess in nums:
        num_Guessed = num_Guessed+1
        guessed_Num_Index = nums.index(num_Guess)
        del nums[guessed_Num_Index]
        print("Correct, You have now guessed " + str(num_Guessed) + " numbers!")
        list_Length = len(nums)
    
    if num_Guess not in nums:
        print("Incorrect!")
        num_Guessing
    if list_Length == 0:
        print("Wow! Congrats, you have guessed all the numbers in the list.")
        exit()
    


def list_Count(x):
    for i in x:
        counter = 0
        counter = counter + 1
        return counter




nums = []

print("Number guessing game")
num_Adding()



    


    