def common_prefix(strs):
    prefix = strs[0]  # Initialize prefix as first string in array of strings

    for str in strs[1:]:  # Starting from second Array, ...

        while str[:len(prefix)] != prefix and prefix:  # Check whether the length Starting from 0 to length of prefix of second Array is equal to prefix while there is prefix only
            prefix = prefix[:-1]  # If not Equal, update the prefix and ... this will continue untill the prefix will come together or if prefix will end.
            if not prefix:  # if prefix becomes empty return  empty string ""
                return ""
    print(prefix)

strs = ["flower","flow","flight"]
common_prefix(strs)