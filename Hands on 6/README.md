The average runtime complexity of the non-random pivot version of quicksort can be derived mathematically as follows:

Let T(n) be the average time complexity of quicksort for an input of size n. In the non-random pivot version, the pivot is chosen as the last element of the array.

In the best case scenario, the pivot always divides the array into two equal parts. Thus, 

T(n)=2T(n/2)+O(n).

In the worst case scenario, the pivot always selects the largest or smallest element, resulting in unbalanced partitions. Thus, 

T(n)=T(n−1)+O(n).

In the average case scenario, we assume that the pivot divides the array into two parts of roughly equal size. Thus, 

T(n)=2T(n/2)+O(n).

By solving these recurrence relations, we find that the average time complexity of the non-random pivot version of quicksort is O(n^2) in the worst case and O(nlogn) in the best and average cases.
