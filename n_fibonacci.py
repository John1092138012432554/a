"""
Filename: n_fibonacci.py
Author: Escobar, John
Created: 03/06/2026
Instructor: Holtslander
"""

def n_fibonacci():
    n1 = 0
    n2 = 1
    n3 = 1
    pal = int(input("Enter a non-negative whole number on the line below:\n"))
    for i in range(2,pal):
        n1 = n2 + n3
        n2 = n3 + n1
        print(f"{n1}", end=" ")
# You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("Print another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()