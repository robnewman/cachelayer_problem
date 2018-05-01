# cachelayer_problem
Write a performant caching layer

## OVERVIEW

This problem may be solved using any programming language.  It is a
made-up problem to test your technical skills, and should take approximately
an hour to complete. 
 
## BACKGROUND

Determining the sales tax rate at a given address is an expensive operation.
Our team has written a function called `sales_tax_lookup`, that takes a street
address as a parameter and returns the sales tax rate, but it is slow to return
a result. 
 
## PROBLEM

While there are billions of addresses, we've identified that 95%
of lookups come from a relatively small number of addresses (less than 100K
addresses).  Unfortunately, you won't know what these addresses are in advance.
You have been tasked with writing a caching layer, with a constraint that
the cache can only be large enough to store approximately 50K addresses.
Your goal is to produce a function `fast_rate_lookup` that returns the same
results as `sales_tax_lookup`, but with better performance. 
 
## NOTES

Optimize for the fewest number of calls to `sales_tax_lookup` while still
maintaining full functionality.
It is okay for the cache to start empty, and to fill over time.There is no need
to prewarm the cache when the server reboots.
Assume this will run on a single server, and that the cache can be stored
in program memory (i.e., a persistent variable is okay for the exercise).

## ABOUT THE SOLUTION

* The solution uses a Least Recently Used (LRU) replacement policy.
* The cache makes use of an OrderedDict to preserve key/value order
* The solution checks the LRU cache object `SimpleCache` using `fast_rate_lookup` method call
* If the address is missing from the cache, `-1` is returned and the `sales_tax_lookup` function is called
* If the address is in the cache, it is returned
* If adding the address exceeds the cache `max_size`, the least used key/value pair in the cache expires and is replaced with the new address

