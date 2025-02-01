"""code to find factorial of a entered number"""

NUM=int(input("enter a number to find its factoral:"))

N=NUM
for N in range(N,1, -1):
    NUM=NUM * (N - 1)

print(f"Factoral is:{NUM}")
