# Prints Fibonacci sequence up to nth term

# Stores number of terms to display
nterms = int(input("How many terms?"))

# First two terms 
n1 , n2 = 0 , 1
count = 0

# Check if number of terms is valid 
if nterms <= 0:
    print("Please enter a positive integer")
    
# If there is only 1 term, print n1
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
        
# Generate Fibonacci sequence 
else:
    print("Fibonacci sequence:")
while count < nterms:
                print(n1)
                nth = n1 + n2
            # Update values
                n1 = n2
                n2 = nth
                count += 1