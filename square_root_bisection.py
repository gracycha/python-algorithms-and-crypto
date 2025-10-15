def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1\n')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0\n')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.\n")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}\n')
    
    return root



def main():
    while True:
        print('1. Calculate the square root of a number')
        print('2. Exit')
        choice = input('Enter your choice (1 or 2): ').strip()
        if choice == '1':
            N = float(input('Enter a non-negative number to find its square root: '))
            square_root_bisection(N)
            #next_calculate = input('Do you want to calculate another square root? (y/n): ').strip().lower()

        elif choice == '2':
            print('Exiting the program.\n')
            break
        else:
            print('Invalid choice. Please enter 1 or 2.\n')


main()