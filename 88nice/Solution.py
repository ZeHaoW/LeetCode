class Solution(object):
    def merge(self, nums1, m, nums2, n):
    	del nums1[m:]
    	del nums2[n:]
    	print nums1, nums2
    	if m == 0:
    		nums1.extend(nums2)
    		print nums1
    		return
        tmp = 0
        for i in nums2:
        	for j in range(tmp, len(nums1)+1):
        		if j == len(nums1):
        			nums1.insert(j, i)
        			break
        		if i > nums1[j]:continue
        		else:
        			tmp = j+1
        			nums1.insert(j, i)
        			break
        	continue
        return


# genius solution每次都解决最大的一个，从后往前插入
    def merge(self, nums1, m, nums2, n):
    	while m > 0 and n > 0:
    		if nums1[m-1] >= nums2[n-1]:
    			nums1[m+n-1] = nums1[m-1]
    			m-=1
    		else:
    			nums1[m+n-1] = nums2[n-1]
    			n-=1
    	if n > 0:
    		nums1[:n] = nums2[:n]
