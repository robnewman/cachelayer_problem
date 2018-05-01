import argparse
from lrucache import LRUCache

def sales_tax_lookup(address):
    """
    Placeholder for PSL-authored non-performant sales tax lookup
    Always return 8.25 placeholder value

    Parameters
    ----------
    address : str, required
        The address to lookup

    Returns
    -------
    sales_tax_rate : float
        A placeholder sales tax rate
    """

    return 8.25


def main(verbose=False):
    """
    Main program code. Assume running on a single server
    with cache stored in memory
    """

    # Initialize a new LRU cache with size of max_size
    address_cache = LRUCache.SimpleCache(max_size=50000)

    # Accept first simple user input
    input_address_str_1 = input("1. First address to look up? ")
    # Check the cache
    sales_tax_1 = address_cache.fast_rate_lookup(input_address_str_1)
    if sales_tax_1 == -1:
        # Call the PSL function
        if verbose:
            print("Missing from cache -- calling PSL function")
        sales_tax_1 = sales_tax_lookup(input_address_str_1)
        # Add new sales_tax value to the cache
        address_cache.set(input_address_str_1, sales_tax_1)

    if verbose:
        print("Sales tax rate for address (%s): %0.2f" % (input_address_str_1, sales_tax_1))
        print("Current cache size: %d" % address_cache.size())
    
    # Accept second simple user input
    input_address_str_2 = input("2. Second address to look up? ")
    # Check the cache
    sales_tax_2 = address_cache.fast_rate_lookup(input_address_str_2)
    if sales_tax_2 == -1:
        # Call the PSL function
        if verbose:
            print("Missing from cache -- calling PSL function")
        sales_tax_2 = sales_tax_lookup(input_address_str_2)
        # Add new sales_tax value to the cache
        address_cache.set(input_address_str_2, sales_tax_2)

    if verbose:
        print("Sales tax rate for address (%s): %0.2f" % (input_address_str_2, sales_tax_2))
        print("Current cache size: %d" % address_cache.size())
 

if __name__ == "__main__":

    ## Initialize argument parser
    parser_desc_str = ["Take an input address (key)",
                       "and return the cached sales tax (value),"
                       "if present. If missing, make call to sales_tax_lookup function."]
    parser = argparse.ArgumentParser(
        description = " ".join(parser_desc_str),
        formatter_class = argparse.RawDescriptionHelpFormatter, 
    )   
    # Verbose output
    parser.add_argument('-v', '--verbose',
        help = 'Turn on verbose logging.',
        action="store_true",
        required = False)
    # Parse arguments
    args = parser.parse_args()
    verbose = args.verbose

    main(verbose)
