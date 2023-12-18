def countOrders(n):
    """
    :type n: int
    :rtype: int
    """
    slots = 2 * n
    ans = 1
    while slots > 1:
        valid_slots = (slots * (slots - 1))//2
        ans *= valid_slots
        slots -= 2
    return ans % (10**9 + 7)




def countOrders(n):
    """
    :type n: int
    :rtype: int
    """
    # Initialize the total number of available slots (twice the number of pairs)
    slots = 2 * n

    # Initialize the variable to store the final count of valid permutations
    ans = 1

    # Continue as long as there are more than 1 slot available
    while slots > 1:
        # Calculate the number of valid slots for the current configuration
        valid_slots = (slots * (slots - 1)) // 2

        # Multiply the current count of valid permutations by the number of valid slots
        ans *= valid_slots

        # Reduce the number of available slots by 2 for the next iteration
        slots -= 2

    # Return the final count of valid permutations modulo (10^9 + 7) to prevent overflow
    return ans % (10**9 + 7)
