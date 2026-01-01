

# Longest Palindromic SubString 

Explanation: Given a string ****s****, find the longest substring which is a palindrome. If there are multiple answers, then find the first appearing substring.


`Input : s = "forgeeksskeegfor"`
`Output: "geeksskeeg"`

1. Create a function to check whether the given substring is palindrome or not. (args: String s, int low, int high)
2. Main function : Get the length of the given string. create two variables : maxLen = 1 and start = 0;
3. Create two loops where i = 0 and j = i
4. Check whether the substring is a palindrome or not and also the length of the substring is greater than the maxLen. (Sliding window).
	`for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {

                // check if the current substring is 
                // a palindrome
                if (checkPal(s, i, j) && (j - i + 1) > maxLen) {
                    start = i;
                    maxLen = j - i + 1;
                }
            }
        }`
5. return or print the substring with start index and start + maxLen


-----------------------------------------------------------------

# A positive integer has been given as an input. Convert decimal value to binary representation. Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits


`Input :10  -> Integer
`Output : 5    -> result- Integer

`Explanation: Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents “5”. Hence output will print “5”.`


```
import java.util.*;
class Main
{
  public static void main(String[] args)
  {
         Scanner sc=new Scanner(System.in);
         int no=sc.nextInt();
          String bin="";
         
          while(no!=0)
           {
                  bin=(no&1)+bin;
                  no=no>>1;
           }
            bin=bin.replaceAll("1","2");
            bin=bin.replaceAll("0","1");
            bin=bin.replaceAll("2","0");
            int res=Integer.parseInt(bin,2);
           System.out.println(res);
   }
```


 1. Reads Input: It takes an integer input from the user.
 2. Converts to Binary String: It converts the input integer into its binary string representation. It does this by repeatedly checking the least significant bit (no & 1) and right-shifting the number (no >> 1).
 3. Inverts Bits: It then "flips" the bits in the binary string:
       * All '1's are temporarily changed to '2's.
       * All '0's are changed to '1's.
       * All '2's (which were original '1's) are changed to '0's.
      This effectively changes every '0' to a '1' and every '1' to a '0' in the binary string.
   4. Converts Back to Integer: The modified binary string (with inverted bits) is then converted back into an integer.
   5. Prints Result: Finally, it prints this new integer to the console.


------------------------------------------------------------------


# Count the number of Sunday jack will get within n number of days.

`Input: mon - input STring denoting the start day of the month`
`Output: 13 -> input integer denoting the number days from the start of the month`


```
Scanner sc=new Scanner(System.in);
 String str = sc.next();
 int n =sc.nextInt();
 String arr[]={"mon","tue","wed","thu","fri","sat","sun"};
 
 int i = 0;
 for(i = 0; i < arr.length; i++){
	 if(arr[i].equals(str)){
		 break;
	 }
 }
 
 int res = 1;
 int rem = 6 - i;
 n = n - rem;
 if(n > 0){
	 res += n / 7;
 }
 System.out.println(res);
```


------------------------------------------------------------------


# find the max number of 'a' in the string 

`input: bbbaaababa -> Value of str`,  3    -> Value of L
`output: 3   -> Maximum number of a’s`

**Explanation:**

From the input given above.

Dividing the string into sets of 3 characters each 

Set 1: {b,b,b}

Set 2: {a,a,a}

Set 3: {b,a,b}

Set 4: {a} -> leftover characters also as taken as another set

Among all the sets, Set 2 has more number of a’s. The number of a’s in set 2 is 3.

Hence, the output is 3.


```
int n=sc.nextInt();
int max=0,count=0;
for(int i=0;i< str.length();i++)
{
	   if(i%n==0)
	   {
		  max=Math.max(count,max); 
		  count=0;
	   }
	   if(str.charAt(i)=='a')
			 count++;
}
max=Math.max(count,max);
System.out.println(max);
```

------------------------------------------------------------------


## An international round table conference will be held in india. Presidents from all over the world representing their respective countries will be attending the conference. The task is to find the possible number of ways(P) to make the N members sit around the circular table such that.

## The president and prime minister of India will always sit next to each other.


`Input: 4`
`Output: 12 -> possible ways of seating the members`

**Explanation:**

2  members should always be next to each other. 

So, 2 members can be in 2! ways

Rest of the members can be arranged in (4-1)!  ways.(1 is subtracted because the previously selected two members will be considered as single members now).

So total possible ways 4 members can be seated around the circular table 2*6= 12.

Hence, output is 12.


```
 public static BigInteger fact(int number)
      {
           BigInteger res= BigInteger.ONE;
           for (int i = number; i > 0; i--)
                 res = res.multiply(BigInteger.valueOf(i));
           return res;
      }
      public static void main(String[] args)
     {
           BigInteger res=fact(n-1);
           System.out.println(res.multiply(BigInteger.valueOf(2)));    
     }
```


------------------------------------------------------------------

# Nearest multiple of 10


# Explanation: A string **s** is given to represent a positive number. The task is to round str to the nearest multiple of 10.  If you have two multiples equally apart from s, choose the smallest element among them.


`Input: s = "29"
`Output: 30`
`Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29.`


1. Get the last Character (charAt(n - 1) - '0')
2. if its less than 5, change the last digit to 0. (setCharAt(n - 1, '0'))
3. else if, last char is greater than 5. set the last character to 0 and put i = n - 2
4. while(i >=0 && num.charAt(i) == '9) set the i value to 0. setCharAt(i, '0') and i--;
5. if the last character is greater than 0, set the value of the i'th character + 1. (num.setCharAt(i, (char) (num.charAt(i)+1));)
6. else insert 1 at the front. 
7. if its equal to 5, then put at the last.
8. lastly convert it back to string.

------------------------------------------------------------------

# Merge two strings

# Given two strings **S1** and **S2** as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of S2 and so on till the strings end.  
**NOTE:** Add the whole string if other string is empty.


`Input:S1 = "Hello" S2 = "Bye"
`Output: HBeylelo`

1. You need to get the shortest length of string in 'N' variable
2. store the longest string in len variable

```
 StringBuilder s = new StringBuilder();
        
        int index = 0;
        int n = 0;
        String len = "";
        if(S1.length() <  S2.length()){
            n =  S1.length();
            len = S2;
            
        }
        else{
            n =  S2.length();
            len = S1;

        }
        
        for(int i = 0; i < n; i++){
            s.append(S1.charAt(i));
            s.append(S2.charAt(i));
            index++;
        }
        s.append(len.substring(index, len.length()));
        
        return s.toString();
```


------------------------------------------------------------------


# Unusual String Sort

# Given a string composed of both lowercase and uppercase letters. Sort it in such a manner such that the uppercase and lowercase letter comes in an alternate manner but in sorted way.

`Input: S = bAwutndekWEdkd 
`Output: AbEdWddekkntuw`


1. create two string variable such as cap and low
2. put a for loop and check of if the character is uppercase or not. (Character.isUpperCase())
3. if true, add the character to the cap variable
4. if false, add the character to the low variable.
5. create a char array and add the string to it and sort it. 
6. do the same for low string too.
7. then convert it back to the string. (low = new String(lows)) and (cap = new String(caps))
8. create a string builder and two variables such i and j
9. in a while loop, put i < length and j < length
10. append the cap and low string characters.
11. lastly append the leftover characters too by using substring. if(i < low.length()) str.append(cap.charAt(i++)).



------------------------------------------------------------------


# Change Bits

# Given a number N , change the 0 to 1 

1. use Integer.toBinaryString() which gives you the binary value of number in string. get that string length;
2. leftshift the bits with 1;
3. (1 << length of string) - 1


------------------------------------------------------------------


# Odd Same

# Given a array of length N, remove all element at odd position

1. the odd element in an array of length N is always the power of 2 which is less than N.
2. take ans = 1L
3. while(ans * 2 <=N){
		ans  * =2;
		}
	return ans;


--------------------------


