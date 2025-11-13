"""
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

class Solution:
    def fizz_buzz(self, n: int) -> List[str]:
        """
        Basic approach: check divisibility by 15, then 3, then 5 separately.
        Advantage: straightforward and readable; leverages short-circuit evaluation
        to avoid redundant checks (if divisible by 15, we skip the elif branches).
        """
        result = []
        for i in range(1, n+1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
    
    def fizz_buzz_better(self, n: int) -> List[str]:
        """
        String concatenation approach: build the result string by appending "Fizz"
        and "Buzz" independently, avoiding the need to check all 4 cases explicitly.
        Advantage: more scalable—if you add a new divisor (e.g., "Wazz" for 7),
        you just add another if block; no need to create new elif branches or
        handle cross-product combinations (e.g., 15, 21, 35, 105, etc.).
        """
        result = []
        for i in range(1, n+1):
            ith_result = ""
            flag = False
            if i % 3 == 0:
                ith_result += "Fizz"
                flag = True
            if i % 5 == 0:
                ith_result += "Buzz"
                flag = True
            if flag:
                result.append(ith_result)
            else:
                result.append(str(i))
        return result
    
    def fizz_buzz_best(self, n: int) -> List[str]:
        """
        Counter-based approach: maintain separate counters for multiples of 3 and 5.
        Instead of using the modulo operator (%), we increment counters and reset
        them when they hit 3 or 5, respectively.
        Advantage: avoids modulo operations (which can be costly in tight loops).
        Trades modulo for simple addition/comparison, which is faster in some
        performance-critical scenarios. Also demonstrates an alternative algorithmic
        pattern for tracking cycles.
        """
        result = []
        three_counter = 1
        five_counter = 1
        for i in range(1, n+1):
            ith_result = ""
            flag = False
            if three_counter == 3:
                ith_result += "Fizz"
                three_counter = 0
                flag = True
            if five_counter == 5:
                ith_result += "Buzz"
                five_counter = 0
                flag = True
            if flag:
                result.append(ith_result)
            else:
                result.append(str(i))
            three_counter += 1
            five_counter += 1
        return result