def calc_num_steps(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    steps = [0] * n
    steps[0] = 1
    steps[1] = 2
    for i in range(2, n):
        steps[i] = steps[i-1] + steps[i-2]
    return steps[n-1]
        
def main():
    print("What is the total number of steps (A) we are climbing? Constraint: Do not enter a number less than 0.")
    num_steps = -1
    invalid = False
    while num_steps < 0:
        if invalid:
            print("You entered a number less than 0. Try again - your input needs to be greater than 0.)")
        num_steps = int(input("Enter here: "))
        invalid = True
    result = calc_num_steps(num_steps)
    print("There are " + str(result) + " distinct ways to climb to the top")
    
    
if __name__ == "__main__":
    main()