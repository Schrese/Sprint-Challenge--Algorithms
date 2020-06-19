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
- 
```
    # store the highest stair
    # store the lowest stair

    # we need to determine where/when to stop the loop
    # As long as our lowest stair does not exceed the highest stair, we can keep making comparrisons and setting our values
        # create/store a midpoint that is the result of the lowest stair and highest stair divided by 2 (rounded down to the nearest whole number, we can't deal with decimals here) 
        # if the egg doesn't break when it is dropped off of the midpoint, then set the lowest stair to the midpoint and run again
        # if the egg breaks when it is dropped off of the midpoint, then set the highest stair to the midpoint
        # once the midpoint has been reached (where the egg is not broken), we just return that midpoint
```

- Runtime: O(log n)

