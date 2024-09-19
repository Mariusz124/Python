import sys
sys.set_int_max_str_digits(0)
n=int(input('Ile liczb ciagu mam wyznaczyc? :'))

fib = [1,1]

for i in range(2,n):
        fib.append(fib[-1] + fib[-2])
for i in fib:
        print(i)