


# Travel Salesman Problem (TSP)

Explanation: Given a ****2d matrix cost[][]**** of ****size n**** where ****cost[i][j]**** denotes the cost of moving from ****city i to city j.**** The task is to complete a ****tour**** from ****city 0 (0-based index)**** to all other cities such that we visit each city ****exactly once**** and then at the end come back to ****city 0**** at minimum cost. 
Find the minimum possible cost to visit every city exactly once and return to the starting city.


## 📘 **Concepts Used**

### 1. **Bitmasking**

- Each city is represented by a bit in a binary number.
    
- If the bit is `1`, that city is visited.
    
- Example (for `n = 4` cities):
    
    - `mask = 0001` → only city 0 visited
        
    - `mask = 1011` → cities 0, 1, 3 visited
        
    - `mask = 1111` → all 4 cities visited ✅
        

### 2. **Recursion**

- `totalCost(mask, pos)` gives **minimum cost** to complete the tour starting from the current `pos`, given the visited cities (`mask`).
    

### 3. **Base Case**

If all cities are visited (`mask == (1 << n) - 1`),  
→ Return cost to go back to the starting city (0).


```
Input: int[][] cost = {
  { 0, 10, 15, 20 },
  { 10, 0, 35, 25 },
  { 15, 35, 0, 30 },
  { 20, 25, 30, 0 }
};  
```

`Ouput: 80`

```
// Java program to find the shortest possible route
// that visits every city exactly once and returns to
// the starting point using memoization and bitmasking
 
import java.util.*;

  class GfG {
 
      static int totalCost(int mask, int pos, int n,
                                int[][] cost) {
        
        // Base case: if all cities are visited, return the
        // cost to return to the starting city (0)
        if (mask == (1 << n) - 1) {
            return cost[pos][0];
        }

        int ans = Integer.MAX_VALUE;

        // Try visiting every city that has not been visited
        // yet
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) == 0) {
              
                // If city i is not visited, visit it and
                // update the mask
                ans = Math.min(ans, cost[pos][i]+ totalCost(mask | (1 << i), i, 
                                                            n, cost));
            }
        }

        return ans;
    }
 
      static int tsp(int[][] cost) {
        int n = cost.length;
        
      // Start from city 0, and only city 0 is
      // visited initially (mask = 1)
        return totalCost(1, 0, n, cost);  
    }

    public static void main(String[] args) {
        
        int[][] cost = { { 0, 10, 15, 20 },
                         { 10, 0, 35, 25 },
                         { 15, 35, 0, 30 },
                         { 20, 25, 30, 0 } };
      
        int res = tsp(cost);
 
        System.out.println(res);
    }
}
```



------------------------------------------------------------------


# Sieve of Eratosthenes

# Given a positive integer **n**, calculate and return all prime numbers less than or equal to **n** using the **Sieve of Eratosthenes** algorithm.  


```Input: n = 10
Output: [2, 3, 5, 7]
Explanation: Prime numbers less than equal to 10 are 2, 3, 5 and 7.
```


```
class Solution {
    public int[] sieve(int n) {
        // code here
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        
        List<Integer> prime = new ArrayList<>();
        
        isPrime[0] = false;
        isPrime[1] = false;
        
        for(int i = 2; i * i <= n; i++){
            if(isPrime[i] == true){
                for(int j = i * i; j <= n; j += i){
                    isPrime[j] = false;
                }
            }
        }
        for(int i = 2; i <= n; i++){
            if(isPrime[i] == true){
                prime.add(i);
            }
        }
        
        int[] result = new int[prime.size()];
        
        for(int i = 0; i < prime.size(); i++){
            result[i] = prime.get(i);
        }
        
        return result;
    }
    }
```

