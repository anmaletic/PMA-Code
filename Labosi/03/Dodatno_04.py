# 4. 
# Napisati Python kod koji će pomoću for ili while petlje iscrtati sljedeći lik:

#   +++++
#   +   +
#   +   +
#   +++++


def Box(p_stupac, p_red):
    for i in range(1, p_red+1):
        for j in range(1, p_stupac+1):
            if(i == 1 or i == p_red):
                print("+", end="")
            else:
                if(j == 1 or j == p_stupac):
                    print("+", end="")
                else:
                    print(" ", end="")
        print()


def main():
    Box(5, 4)


main()