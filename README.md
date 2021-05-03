# primes 
A function that prints out all the prime numbers up to some number n, uses iteration to check if each number is prime and a conditional to print out numbers
only if they are prime. Also utilises (or calls) helper functions inside of solution to ease it.    


0ptimization:    
The first optimization takes advantage of the fact that two is the only even prime. Thus we can check if a number is even and as long as its greater
than 2, we know that it is not prime.   
Our second optimization takes advantage of the fact that when checking factors, we only need to check odd factors up to the square root of a
number. Consider a number n decomposed into factors n = ab. There are two cases, either n is prime and without loss of generality, a = n, b = 1 or
n is not prime and a, b ≠ n, 1. In this case, if a > √n, then b < √n. So we only need to check all possible values of b and we get the values of a for
free! This means that even the simple method of checking factors will increase in complexity as a square root compared to the size of the number
instead of linearly.

The Sieve of Eratosthenes:   
This is an example of dynamic programming, where the general idea is to not redo computations we have already done.  
1. Generate a list of all numbers between 0 and N; mark the numbers 0 and 1 to be not prime    
2. Starting with p = 2 (the first prime) mark all numbers of the form np where n > 1 and np <= N to be not prime (they can't be prime since they are multiples of 2!)    
3. Find the smallest number greater than p which is not marked and set that equal to p, then go back to step 2. Stop if there is no unmarked number greater than p and less than N + 1
