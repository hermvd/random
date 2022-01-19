

def flt(base, exp):
    return (base ** (exp-1)) % exp


# This script implements Fermat's Little Theorem to "check" if something is prime
def main():
    someBase = 100

    for i in range(1, someBase):
        print(f'FLT of {someBase, i} is: {flt(i, someBase)}')

        # this statement breaks out the loop if a counter-example is found
        if flt(i, someBase) != 1:
            break


    # In case you want to try this yourself
    # base = int(input())
    #
    # for i in range(1, base):
    #     print(f'FLT of {base, i} is: {flt(i, base)}')
    #
    #     # this statement breaks out the loop if a counter-example is found
    #     if flt(i, base) != 1:
    #         break

    return 0


 # essentially makes all the variables run more efficient and locally, also tells you whether the script is imported or not
if __name__ == '__main__':
    main()