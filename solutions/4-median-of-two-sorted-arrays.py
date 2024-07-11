from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # let "a" be the smaller array 
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = nums2, nums1
        total = len(a) + len(b)
        half = total // 2

        l = 0
        r = len(a) - 1

        while True:
            i = l + (r - l) // 2 
            j = half - i - 2

            al = a[i] if i >= 0 else float("-infinity")
            ar = a[i + 1] if (i + 1) < len(a) else float("infinity")
            bl = b[j] if j >= 0 else float("-infinity")
            br = b[j + 1] if (j + 1) < len(b) else float("infinity")

            # if correctly partitioned
            if al <= br and bl <= ar:
                # solve odd case 
                if total % 2:
                    return min(ar, br)
                # solve even case 
                return (max(al, bl) + min(ar, br)) / 2 
            elif al > br:
                r = i - 1 
            else:
                l = i + 1 

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1,2], [3]))
    print(sol.findMedianSortedArrays([1,3], [2,4]))
