# Challenge Summary
<!-- Description of the challenge -->
https://github.com/HaneenHaashlamoun/data-structures-and-algorithms/pull/34

### Implementation
- [x] Provide a visual step through for each of the sample arrays based on the provided pseudo code
- [x] Convert the pseudo-code into working code in your language
- [x] Present a complete set of working tests

## Whiteboard Process
<!-- Embedded whiteboard image -->
![quick_sort](quick_sort.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Time: O(n log n)
- Space: O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->
used recursion to sort the a shift point and rearrange the elements lesser than the shift to it's left side
and elements larger than the shift to it's right side. Continue doing this until array is
sorted. In this case, shift point is always selected as a last one.
