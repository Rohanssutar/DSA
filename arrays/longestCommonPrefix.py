def longestCommonPrefix(strs: list[str]) -> str:
    # Start with the first string
    prefix = strs[0]

    # Loop through the remaining array of str
    for i in range(1, len(strs)):
        # Initialize a variable j for comparing chars of each string
        j = 0

        # Using while loop makes sense bcz we don't knoq th exact length of a string
        # This loop will continue till the prefix are same or equal, if not it'll break out of it & check for new prefixes
        while j < min(len(prefix), len(strs[i])):
            if prefix[j] != strs[i][j]:
                break
            j += 1

        # New set of Prefix
        prefix = prefix[:j]

    # Return the longest set of prefix
    return prefix
