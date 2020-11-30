def calc_num_steps(n):
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
    num_steps = int(input("How many steps are we performing the calculation for? Enter here: "))
    result = calc_num_steps(num_steps)
    print("There are " + str(result) + " distinct ways to climb to the top")
    
    
if __name__ == "__main__":
    main()