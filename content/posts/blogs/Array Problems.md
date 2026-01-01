	

# Element with Left side smaller than Right side greater

`Input : [4, 2, 5, 7]`
`output : 5`

1. Create two array, leftMax and rightMin
2. Assing rightMin[n - 1]  to max value (Integer.MAX_VALUE
3. In a for loop from i = 1, assign the leftMax[i] = Math.max(leftMax[i - 1], arr[i - 1])
4. In a for loop from i = n - 2, assign the RightMin[i] = Math.min(rightMin[i + 1], arr[i + 1]) 
5. then return the element that is arr[i] > leftMax[i] && arr[i] < rightMin[i]

------------------------------------------------------------------
# Sorting Elements of an Array by Frequency

### Explanation: Given an array **A[]** of integers, **sort** the array according to **frequency** of elements. That is elements that have higher frequency come first. If frequencies of two elements are same, then smaller number comes first.

  Input: arr = [2, 5, 2, 8, 5, 6, 8, 8]
  Output: 8 8 8 2 2 5 5 6

   1. Create a Frequency Map:
       * Create a HashMap to store each number from the array as a key and its frequency (count) as the value.
       * Iterate through the input array arr. For each number, update its count in the HashMap.
       * Example Map: {2=2, 5=2, 6=1, 8=3}

   2. Implement Custom Sorting:
       * Use Collections.sort() on the original array arr.
       * Provide a custom comparator to define the sorting rules.

   3. Primary Sort Rule (by Frequency):
       * Inside the comparator, for two numbers a and b, get their frequencies from the HashMap.
       * If the frequencies are different, sort in descending order of frequency. The comparison will be frequency of b - frequency of a.
		```
			Collections.sort(arr, (a, b)-> {
    		    int freqA = map.get(a);
    		    int freqB = map.get(b);
    		    
    		    if(freqA != freqB){
    		        return freqB - freqA;
    		    }
    		    else{
    		        return a- b;
    		    }
    		});
		```

   4. Secondary Sort Rule (by Value):
       * If the frequencies are the same, sort the numbers in ascending order of their value. The comparison will be a - b.

   5. Print the Sorted Array:
       * Iterate through the now-sorted array and print each element.


------------------------------------------------------------------
# Counting Elements in two arrays

`Input: A: [4, 8, 7, 5, 1] B: [4, 48, 3, 0, 1, 1, 15`
`Output: [5, 6, 6, 6, 3]`

Explanation: A[0] = 4, which is 5 elements lesser than 4 in the B array. return those count for each element in A.

1. Create a list and sort the B list
2. Create a function that does Binary Search with the B array and one element from A.
		```
		if(arr[mid] <= key){
			low = mid + 1;	
		}
		else{
			high = mid;
		}
		return low;
		
		```
1. It counts the elements which are lesser than the key.
2. Add the count to the list.

------------------------------------------------------------------










# Two Repeated Elements

`INput: [1, 2, 1, 3, 4, 3]`
`Output: [1, 3]`

## Explanation: Need to return the two elements which are repeated.

1. Create a set and a variable 'Index'
2. Loop the elements of the arr and check that element is present in the set.
3. if not present, add the element in the set.
4. If present, add the element to the list and increment the index.
5. When the index is 2, break.


------------------------------------------------------------------
# Elements in Range


`INput: A = 2, B = 5, arr = [1, 4, 6, 2, 7, 8, 3]`
`Output: True or False`

## Explanation: Return true if the range from A to B are present in the array

1. Sort the Array. (Arrays.sort(arr))
2. Create a Set and add the elements
3. in loop check from A to B for elements

------------------------------------------------------------------
# Remove Minimal Elements

`Input: arr = [4, 5, 100, 9, 10, 11, 12, 15, 200]`

## Explanation: 2 * min >= max  --> Remove the elements so that it is satisfied

1. sort the array
2. STart = 0, maxLen = 0
3. create a for loop (int end = 0)
4. ```
   while(start < end) && 2 * arr[start] < arr[end]{
	   start++;
	}
	maxLen = Math.max(maxLen, end - start+ 1);
		}
	}
   ```
   5. return the n -  maxLen so that it gives count of elements to remove.

------------------------------------------------------------------

# Adding Array Elements

`Input: N = 6, K = 6, arr = [1, 10, 12, 9, 2, 3]`

## Explanation: Add first 2 elements and erase them , the added elements should be >= K. count the number of operations required.

```
class Solution {
    int minOperations(int[] arr, int n, int k) {
        // code here
       
       PriorityQueue<Integer> pq = new PriorityQueue<>();
       int count = 0;
       for(int i: arr){
           pq.add(i);
       }
       
       while(!pq.isEmpty()){
          

           if(pq.peek() >= k)
           {
               return count;
           }
             int first = 0, sec = 0;
           
           if(pq.size() == 1){
               if(pq.peek() < k) return -1;
               else{
               return count;
                   
               }
           }
           
           
           
           first = pq.peek();
           pq.poll();
           sec = pq.peek();
           pq.poll();
           
           pq.add(first + sec);
           count++;
       }
       return count;
    }
}
```

------------------------------------------------------------------


# Array Subset

`input: A[] = [11, 7, 1, 13, 21, 3, 7, 3] , B[] = [11, 3, 7, 1, 1]

## Explanation: Return true if the B array is subset of A.

1. create a Hashmap for B array and get the count
2. traverse the A array and remove the value of key, if it is present in the map. 
	`map1.put(i, map1.get(i) - 1))`
3. Traverse the map.values() and check if the values is > 0. 
4. If true then return false or else true.


------------------------------------------------------------------
# Rearrange the array in a way that max element comes first and min element comes second

`Input: [1, 2, 3, 4, 5]`
`Output: [5, 1, 4, 2, 3]`

1. Traverse a Array
2. Create a two pointer
3. if flag is True, Insert the last element to the new array.
4. Then put `flag = !flag.
5. Add the first element to the array.


------------------------------------------------------------------

# Swap a element in list

-> list.set(value, arr.get(i));

------------------------------------------------------------------

# Sum of middle elements of two sorted Arrays

## Explanation: Given two sorted arrays, ****arr1[]**** and ****arr2[]****, each of size ****N****, the task is to merge the arrays and find the sum of the two middle elements of the merged array.


`Input:N = 5, arr1[] = {1,2,4,6,10}, arr2[] = {4,5,6,9,12}`
`Output: 11`


1. Create a merged array of size 2*n
2. Traverse both arrays and merge them into the  merged array]
3. ` while (i < n && j < n) {
            if (arr1[i] <= arr2[j]) {
                merged[k++] = arr1[i++];
            }
            else {
                merged[k++] = arr2[j++];
            }
        }`
4. Then copy the remaining elements in arr1 to the merged array
5. ` while (i < n) {
            merged[k++] = arr1[i++];
        }`
6. and also copy the elements in arr2 to merged array.
7. `   while (j < n) {
            merged[k++] = arr2[j++];
        }
8. Return the sum of the middle two elements.


------------------------------------------------------------------

# Remove character

# Explanation: Given two strings str1 and str2, remove those characters from the first string(str1) which are present in the second string(str2). Both the strings are different and contain only lowercase characters.


`Input: str1 = "computer", str2= "cat"
`Output: "ompuer"`


1. Create a set and append the str1 into it. 
2. then traverse the str2 and check if the str2 is present in the str1, if not present, add it to the stringBuilder.


------------------------------------------------------------------


# Convert a String to Camel Case


## Explanation: Convert the given String to Camel Case.
`input`: S = 'i love programming'
`output: 'I Love Programming'`

1. create a StringBuilder and append the first character which is converted to uppercase (Character.toUpperCase());
2. then traverse through the string by using split().
3. get the character in a variable and check for the previous values (i - 1) is space or not.
4. if True; append the value which should be converted to upper.
5. else; append the character to the stringbuilder


`
----------------------------------------------------------------------------------------------


# Count the Substring

# Explanation: Return the number of subString possible in String.

`INput: '10101'`
`Output: 3` 


1. get the count of '1'
2. use formula n * (n - 1) / 2


------------------------------------------------------------------

# Reverse the String without reversing the individuals words.


`input: I.LOVE.YOU`
`output: YOU.LOVE.I`

1. split the words and store it in array. `split("\\.")`
2. traverse the array in reverse
3. if the stringbuilder length is > 0 then append the dot (.)
4. Because first character should not be dot
5. else append the value to the stringbuilder


------------------------------------------------------------------



#  Check if two Strings are Anagrams of each other

## Explanation: Given two non-empty strings ****s1**** and ****s2**** of lowercase letters, determine if they are anagrams — i.e., if they contain the same characters with the same frequencies.


`Input: s1 = “geeks”  s2 = “kseeg”  
`Output: true  
`Explanation: Both the string have same characters with same frequency. So, they are anagrams.


1. if both the length of the string are not matching, then return false;
2. store the two string in two separate array
3. sort the arrays
4. check if both the array are equal. Arrays.equals(arr1, arr2);

------------------------------------------------------------------


# Valid Substring

# Explanation:  Given a string **`s`** consisting only of opening and closing parentheses **`'('`** and `')'`, find the length of the **longest valid** (well-formed) parentheses **substring**.


`Input`:  s = "(()("
`Output: 2


1. create a stack
2. push(-1) to the stack
3. get the character and check if its '(' then push the i value to the stack.
4. if false, pop the stack and check if its empty. stack.isEmpty()
5. if true, push(i) and if false, check for maxLength  = math.max(maxLength, i - stack.peek())


------------------------------------------------------------------


# Stock Buy and Sell – Max one Transaction Allowed



class Solution {
    public int maximumProfit(int prices[]) {
        // Code here
        int min = Integer.MAX_VALUE;
       int maxProfit = 0;
       for(int price : prices){
           min = Math.min(min,price);
           maxProfit = Math.max(maxProfit,price-min);
       }
       return maxProfit;
        
    }



---- 

# Maximum Subarray Sum - Kadane's Algorithm

	    static int maxSubarraySum(int[] arr) {
        
        // Stores the result (maximum sum found so far)
        int res = arr[0];
        
        // Maximum sum of subarray ending at current position
        int maxEnding = arr[0];

        for (int i = 1; i < arr.length; i++) {
            
            // Either extend the previous subarray or start 
            // new from current element
            maxEnding = Math.max(maxEnding + arr[i], arr[i]);
          
            // Update result if the new subarray sum is larger
            res = Math.max(res, maxEnding);
        }
        return res;
    }


# Nth Fibonacci Number


class GfG {
  
    static int nthFibonacci(int n){

        if (n <= 1) {
            return n;
        }


        return nthFibonacci(n - 1) + nthFibonacci(n - 2);
    }

    public static void main(String[] args){
        int n = 5;
        int result = nthFibonacci(n);
        System.out.println(result);
    }
}



# Fibonacci Series

class Solution {  
    // Function to return list containing first n fibonacci numbers.  
    public static int[] fibonacciNumbers(int n) {  
        // Your code here  
        int fqi[] = new int[n];  
        int num1 = 0, num2 =1;  
        int sum = 0;  
          
        for(int i =0 ;i< n;i++){  
            fqi[i] = num1;  
            sum = num1 +num2;  
            num1 = num2;  
            num2 = sum;  
              
        }  
        return fqi;  
    }  
}


