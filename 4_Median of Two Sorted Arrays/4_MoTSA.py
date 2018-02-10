class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1);
        n = len(nums2);
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m
        imin = 0;
        imax = m;

        while imin <= imax:
            i = (imin + imax) / 2;
            j = (m + n + 1) / 2 - i;
            if i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1;                                #二分寻值，用i=i-1也能ac但是慢。
            elif i < m and nums1[i] < nums2[j - 1]:
                imin = i + 1;
            else:
                if (i == 0):                                #分别讨论左值和右值。
                    maxleft = nums2[j - 1];
                elif (j == 0):                              #在nums1=[1] nums2=[1]的情况下需要考虑
                                                            #我一开始认为n>m不用j==0的情况，但是考虑到n与m相等或者相近的情况需要考虑。
                    maxleft = nums1[i - 1];
                else:
                    maxleft = max(nums1[i - 1], nums2[j - 1])
                if (m + n) % 2 == 1:                        #若m+n奇数中位数直接就是中间值，即maxleft;
                    return maxleft;
                if i == m:
                    minright = nums2[j];
                elif j == n:                                   #在nums1=[1] nums2=[1]的情况下需要考虑同左值
                    minright = nums1[i];
                else:
                    minright = min(nums1[i], nums2[j])
                return (maxleft + minright) / 2.0;

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        total = len1 + len2
        if (len1+len2) % 2 == 0:
            return (self.findKsort(nums1, len1, nums2, len2, total/2) + self.findKsort(nums1, len1, nums2, len2, total/2+1))*0.5
        else:
            return float(self.findKsort(nums1, len1, nums2, len2, total/2+1))
        
    def findKsort(self, li1, len1, li2, len2, k):
        if len1 > len2:
            return self.findKsort(li2, len2, li1, len1, k)
        if len1 == 0:
            return li2[k -1]
        if k == 1:
            return min(li1[0],li2[0])
        
        mid = k/2
        m1 = min(mid, len1)
        m2 = k - m1
        if li1[m1-1] < li2[m2-1]:
            return self.findKsort(li1[m1:], len1 - m1, li2, len2, k - m1)
        elif li1[m1-1] > li2[m2-1]:
            return self.findKsort(li1, len1, li2[m2:], len2 - m2, k - m2)
        else:
            return li1[m1-1]


class Solution:  
    def findKth(self,a,b,k):  
        len1=len(a)  
        len2=len(b)  
        if len1==0:return b[k-1]  
        if len2==0:return a[k-1]  
        if k==1:return min(a[0],b[0])  
        mid1=min(k/2,len1)  
        mid2=min(k/2,len2)  
        if a[mid1-1] < b[mid2-1]:  
            c=a[mid1:len1]  
            return self.findKth(c,b,k-mid1)  
        else:  
            c=b[mid2:len2]  
            return self.findKth(a,c,k-mid2)  
    # @param {integer[]} nums1  
    # @param {integer[]} nums2  
    # @return {float}  
    def findMedianSortedArrays(self, nums1, nums2):  
        len1=len(nums1)  
        len2=len(nums2)  
        if (len1+len2)%2 == 1:  
            return self.findKth(nums1,nums2,(len1+len2+1)/2)  
        else:  
            return (self.findKth(nums1,nums2,(len1+len2+1)/2)+self.findKth(nums1,nums2,(len1+len2+1)/2+1))/2.0  
    def min(self,a,b):  
        return a if a<b else b