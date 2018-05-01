from collections import OrderedDict

class SimpleCache:
    """Simple Least Recently Used (LRU) 
    replacement policy class
    """
    def __init__(self, max_size=1024):
        """
        Initialize a simple key/value cache based on
        max_size, with a default value of 1024 using
        an OrderedDict which preserves order of key/value
        insertion

        Parameters
        ----------
        max_size : int, optional
            The maximum size of the cache
        """
        self.max_size = max_size
        self.cache = OrderedDict()

    def fast_rate_lookup(self, key):
        """
        For a given key, return the value from the cache

        Parameters
        ----------
        key : string, required
            The street address    

        Returns
        -------
        value : float
            The value from cache or -1
        """

        try:
            value = self.cache.pop(key)
            # Ensure the key/value pair remains
            # in the OrderedDict and moves to 
            # the last entry
            self.cache[key] = value
            return value
        except KeyError:
            return -1


    def set(self, key, value):
        """
        Add a key/value pair to the cache

        When the capacity is exceeded the First-In, First-Out
        (FIFO) element (least used) expires (i.e. is removed)

        Parameters
        ----------
        key : string, required
            The street address
        value : float, required
            The sales tax rate

        Returns
        -------
        success : Return True if successful
        """

        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.max_size:
                # Remove the least used item
                self.cache.popitem(last=False)
        # Add the new key/value pair to the OrderedDict cache
        self.cache[key] = value


    def size(self):
        """
        Helper function to return the size of the cache
        """

        return len(self.cache)
