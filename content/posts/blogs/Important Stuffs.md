
# convert binary to Integer

## Explanation: Multiply the digit from last to the 2^i++ and append the value to a variable.

1. create 2 variable base  = 1 and dec = 0.
```
while(N > 0){

	int temp = N % 10;
	N = N / 10;
	dec += temp * base;
	base = base * 2;
}
```

# Integer to Binary

```
 String binary = "";
        if (n == 0) {
            binary = "0";
        } else {
            while (n > 0) {
                int rem = n % 2;
                binary = rem + binary;  // prepend remainder
                n = n / 2;
            }
        }
```


# find gcd

1. LCM = a * b / GCD(a, b)
2. if b is 0 then gcd is a

```
static int findGCD(int a, int b) {
        if (b == 0)
            return a;          // Base case
        return findGCD(b, a % b);  // Recursive step
    }
    
```


------------------------------------------------------------------
# Find Prime

# the number should be divided by 1 and itself

```
static boolean isPrime(int n) {
        if (n <= 1) return false;      // 0 and 1 are not prime
        if (n == 2) return true;       // 2 is prime
        if (n % 2 == 0) return false;  // even numbers > 2 are not prime

        // Check divisibility up to √n
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
    
```

---------------

# Leap Year

1. The leap year should be divisible by 4 and 400
2. should not be divisible by 100
3. `n % 100 != 0 && n % 4 == 0 || n % 400 == 0`


------------------------------------------------------------------

# Geometric progression series

` a x r ^ (n - 1)` - > n varies from 0 to n


------------

# Automorphic number

76^2  = 5776
last digit should be same

-------------

# Check power of 2

`boolean isPow2 = (n > 0) && ((n & (n - 1)) == 0);

---------

# Swap without temp

```
a = a ^ b;
b = a ^ b;
a = a ^ b;

```

----


#  Reverse a number

```
int rev = 0; while (n > 0) {
	rev = rev * 10 + n % 10; 
	n /= 10; 
	}
	
```


------

# Check Palindrome (Number)

```
int temp = n, rev = 0; while (n > 0) {
     rev = rev * 10 + n % 10;
     n /= 10; 
} 
if (rev == temp) System.out.println("Palindrome");
```

-----

# Fibonacci

```
int a = 0, b = 1;
for (int i = 0; i < n; i++) {
    System.out.print(a + " ");
    int c = a + b;
    a = b;
    b = c;
}
```

------

# Armstrong number

```
int sum = 0, temp = n;
int digits = String.valueOf(n).length();
while (n > 0) {
    int rem = n % 10;
    sum += Math.pow(rem, digits);
    n /= 10;
}
if (sum == temp) System.out.println("Armstrong");
```

-----

# Sum of n natural numbers


`int sum = n * (n + 1) / 2;

-----
