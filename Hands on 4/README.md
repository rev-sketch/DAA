### Problem 0 - Fibonacci Sequence

2. By stepping into the function when calling fib(5), I get the following sequence:
   <br />fib(5) -> fib(4) -> fib(3) -> fib(2) -> fib(1) -> fib(0)<br />-> fib(1) -> fib(2)<br /> -> fib(1) -> fib(0)<br />-> fib(3) -> fib(2) -> fib(1) -> fib(0)<br />-> fib(1)

Expressed in big-O notation, the time complexity is O(2^n), indicating that the time required by the algorithm grows exponentially with the input size n. This exponential growth leads to inefficiency for larger values of n due to the vast number of redundant calculations.

### Problem 1 - Merge K Arrays (Min Heap)
2. Time Complexity:
   The runtime would be calculated with the following summation formula:
   $$T(n,k) = c_7\*k\*n\*lg(k) + c_{10}\*k\*n\*lg(k) + Θ(k\*n)$$
   $$\Rightarrow T(n, k) = c\*k\*n\*lg(k) + Θ(k\*n)$$
   $$\Rightarrow T(n, k) = Θ(k\*n\*lg(k))$$

### Problem 2 - Remove Duplicates from array
2. Time Complexity:
   The runtime would be calculated with the following summation formula:
    <br />
    $$T(n) = \sum_{i=1}^{n+1} c_1 + \sum_{i=1}^{n} c_2$$
    $$\Rightarrow T(n) = c_1*(n+1) + c_2*n$$
    $$\Rightarrow T(n) = (c_1+c_2)*n + c_1$$
   $$\Rightarrow T(n) = Θ(n)$$
