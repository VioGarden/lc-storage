# Define a class named "Solution" to encapsulate the median finding logic.
class Solution(object):

    # Recursive function to find the kth element in two sorted arrays.
    # The function takes input arrays, start and end indices for each array, and k.
    def find_kth_element(self, nums1, start1, end1, nums2, start2, end2, k):

        # Check if there are no more elements in nums1.
        if end1 - start1 < 0:
            # Return the kth element in nums2.
            return nums2[start2 + k]
        
        # Check if there are no more elements in nums2.
        if end2 - start2 < 0:
            # Return the kth element in nums1.
            return nums1[start1 + k]
        
        # Base case: If k is less than 1, return the minimum of two elements.
        if k < 1:
            return min(nums1[start1 + k], nums2[start2 + k])
        
        # Calculate the middle indices for both arrays.
        middle1, middle2 = (start1 + end1) // 2, (start2 + end2) // 2
        median1, median2 = nums1[middle1], nums2[middle2]

        # Calculate the number of elements in the lower halves of both arrays.
        lower_half_count = (middle1 - start1) + (middle2 - start2)

        # If the sum of lower_half_count and 2 (for median1 and median2) is less than k,
        # it means the kth element is in the upper halves.
        if lower_half_count < k:
            # Determine which median to discard based on their values.
            if median1 > median2:
                # Recursively search the upper half of nums2.
                return self.find_kth_element(nums1, start1, end1, nums2, middle2 + 1, end2, k - (middle2 - start2) - 1)
            else:
                # Recursively search the upper half of nums1.
                return self.find_kth_element(nums1, middle1 + 1, end1, nums2, start2, end2, k - (middle1 - start1) - 1)
        
        # If the sum of lower_half_count and 2 is greater than or equal to k,
        # it means the kth element is in the lower halves.
        else:
            if median1 > median2:
                # Recursively search the lower half of nums2.
                return self.find_kth_element(nums1, start1, middle1 - 1, nums2, start2, end2, k)
            else:
                # Recursively search the lower half of nums1.
                return self.find_kth_element(nums1, start1, end1, nums2, start2, middle2 - 1, k)

    # Function to find the median of two sorted arrays.
    def findMedianSortedArrays(self, nums1, nums2):
        # Calculate the total length of both arrays.
        total_length = len(nums1) + len(nums2)

        # Check if the total length is odd.
        if total_length % 2 == 1:
            # Return the middle element using the find_kth_element function.
            return self.find_kth_element(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, total_length // 2)
        
        # If the total length is even, calculate two medians and return their average.
        else:
            median1 = self.find_kth_element(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, total_length // 2)
            median2 = self.find_kth_element(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, total_length // 2 - 1)
            return (median1 + median2) / 2.0
