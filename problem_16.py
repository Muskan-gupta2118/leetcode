def merge(nums1, m, nums2, n):
    i = m - 1  # last element in nums1 (valid part)
    j = n - 1  # last element in nums2
    k = m + n - 1  # last position of nums1

    # Merge from the end
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If elements left in nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# Example input
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print("Before Merge:", nums1)

merge(nums1, m, nums2, n)

print("After Merge:", nums1)