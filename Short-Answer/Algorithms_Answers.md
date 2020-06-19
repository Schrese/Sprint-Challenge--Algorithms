#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n^3) - Polynomial
    Correction:
    - it's doing an operation n ^ 3 times. so "a" needs to change (possibly) that many times. if "n" were 2, then "a" would need to change 8 times, and if "n" were 10, then "a" would change 1,000 times  
<!-- O(1)
    - the first line is O(1) because it's just a definition
    - the second line is a while loop, but it's only checking the values of a and n, then doing a simple operation, so I think that would be O(1)
    - the third line is doing the same thing, it's just doing an operation, so it would also be O(1)
    - Basically. No matter how large/small "n" is, the number of operations doesn't increase -->
b) O(n)
    - it's doing the operation only runs "n" times. So if "n" is 2, then this will run 2 times (the "j" almost got me thinking that this is actually O(log n), but the while loop has no bearing on how many times "n" is run). And from there it's just operations

c) O(1)
    - This is not trying to loop through any data, it's just doing mathematical operations/comparisons. No matter how many bunnies are input, the number of operations does not increase 

## Exercise II

- My initial thoughts for this exercise were that this would be the perfect time to use a binary search algorithm. This would start at the midpoint and determine whether or not the egg broke and whether it breaks or not, half of the stairs are cut out of being possibilities. Continuing to do this could continue to "rule out" an additional half of the remaining stairs each time. Depending on the amount of stairs.
- Runtime: O(log n)

