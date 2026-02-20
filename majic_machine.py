## majic_machine with test
def majic_machine(n): #The function I've defined:
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2 
        else:
            n = n * 3 + 1
        print(n)
    return(n)

#function tests
assert majic_machine(50)==1, "Test 1 failed"
assert majic_machine(2)==1, "Test 2 failed"
assert majic_machine(3)==1, "Test 3 failed"
print("All tests passed!")

n = int(input("Enter a random number: "))
if 2 <= n <= 1000:
    majic_machine(n)
else:
    print(f"{n} is not valid!!")

## What if I don't want the steps to be printed in the test output???