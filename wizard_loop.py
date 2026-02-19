#جادوی حلقه قابل تست
def number_booster(n,x):  #The function I've defined:
    for i in range(n):
        if x % 2 != 0:
            x = x * 2 - 1
        else:
            x = x // 2
    return(x)
#function tests
assert number_booster(5,10)==65, "Test 1 failed"
assert number_booster(6,10)==129, "Test 2 failed"
assert number_booster(3,10)==17, "Test 3 failed"
assert number_booster(4,8)==1, "Test 4 failed"
print("All tests passed!")

x = int(input(f"Enter a number between 1 to 1000 you want to boost: "))
n = int(input(f"Enter the number of times between 1 to 20 you want {x} to be boosted :"))
if 1 <=n <= 20 and 1 <= x <= 1000:
    print(f" The boosted number is : {number_booster(n,x)}")