def find_sublist_with_max_matching_elements(l, l2):
    max_count = 0
    max_sublist = []

    # Iterate over each sublist in l
    for sublist in l:
        count = 0  # Reset count for each sublist

        # Count the number of matching elements between sublist and l2
        for element in sublist:
            if element in l2:
                count += 1

        # Debug: Print the count for the current sublist
        print(f"Sublist: {sublist}, Count: {count}")

        # If we find more matches, update max_count and reset max_sublist
        if count > max_count:
            max_count = count
            max_sublist = [sublist]
        elif count == max_count:
            # If the count is the same as the max, add this sublist to max_sublist
            max_sublist.append(sublist)

    return (max_sublist, max_count)

# Input lists
l = [[1, 2, 3], [4, 5, 6], [1, 3, 4], [4, 5, 1]]
l2 = [2, 5, 1]

# Print the result
print(find_sublist_with_max_matching_elements(l, l2))  # Expected output: [4, 5, 1]
