#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
a) O(n)
    line 1 is O(1) because it's a constant
    line 2 is O(n^3) because it is checking until n^3 is reached
    line 3 is O(n^2) because it is increasing "a" by n-squared added to itself. But since we don't count the constants, we don't need to count "a"
    Caveat: Since line 3 is forcing "a" (in line 1) to aproach the limit set by line 2 twice as fast, we can take "n^2" off of "n^3" in order to make it "n^1" (which is just "n")

b) O(n log n)
    For this one I actually think it's a bit easier to not break it down line-by-line. The main parts that I focused on were lines 2, 4, and 5. Line 2 is an O(n) operation because it increases depending on how large "n" is, and initially, line 4 does nearly the same. But in looking at line 5, it actually becomes evident that j is going to approach n faster (than, say, if we added (like in the previous example)). But... as "n" increases, the number of operations it takes for j to reach "n" actually increases slightly. if n = 10, then the outer loop runs 10 times BUT the inner loop runs 40 times (4 times per outer loop). if n = 100, then the outer loop runs 100 times BUT the inner loop runs 700 times. This only increases the higher and higher you increase "n". So this would have to be O(n log n)

c) O(n)
    The way this one works is by taking the number of bunnies and adding "2" for each time the recursion is run and decreasing the amount of bunnies at the same time. So if there are 5 bunnies, then the loop would run 5 times with 1 bunny giving the value of 2, 2 bunnies giving the value of 4, 3 bunnies giving the value of 6, 4 bunnies giving the value of 8, and 5 values giving the value of 10 ears total. But since the number of operations is directly proportional to the input (bunnies) it would be a linear runtime, so O(n)

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

