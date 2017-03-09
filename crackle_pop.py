#Write a program that prints out the numbers 1 to 100 (inclusive).
#If the number is divisible by 3, print Crackle instead of the number.
#If it's divisible by 5, print Pop.
#If it's divisible by both 3 and 5, print CracklePop. You can use any language.

#custom range
start = 1
end = 101
my_range = range(start,end)
divisor_three = 3
divisor_five = 5
#function
def cracklepop(number, divisor):
    return number % divisor == 0 # what is my residual

#loop
for i in my_range:
    result = ""
    if cracklepop(i, divisor_three):
        result += "Crackle"
    if cracklepop(i, divisor_five):
        result += "Pop"
    print(i if result == "" else result)
    

#https://repl.it/GICd
