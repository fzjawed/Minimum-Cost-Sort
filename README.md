# Minimum-Cost-Sort

03 May 2021 05:35 PM

This one was actually really simple but I think coming up with the way to write the solution was a bit weird. I didn't think I'd be making two copies of the array because I haven't done that in many questions so I was honestly a bit shook that this method worked. 

***Question: Given a list of integers nums, return the minimum cost of sorting the list in ascending or descending order. The cost is defined as the sum of absolute differences between any element's old and new value.***

So basically what we're doing in the solution is make two variables one with the array sorted in ascending order and one with the array sorted in descending. The other two variable s``sum1 sum2`` will be used to track the ``cost``.

When you're subtracting each element from the sorted arrays with the actual array you're sort of seeing how many switches have been made while tracking the cost at the same time. 

