def canJump(nums):
    if len(nums) <= 1:
        return True
    main, hold = len(nums) - 2, len(nums)-1
    while main >= 0:
        if (hold - main) <= nums[main]:
            hold = main
        main -= 1
    if hold == 0:
        return True
    return False