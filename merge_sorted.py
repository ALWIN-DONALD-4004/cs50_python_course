nums1 = [1,2,3,0,0,0]
nums2 = [3,2,5]
num = list()

nums1 += nums2

for i in nums1:
    if i != 0:
        num.append(i)
nums1 = sorted(num)

print(nums1)
        