class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		#self.dict_xy = dict((i+1,a) for i,a in enumerate(height))
		# self.dict_sorted = sorted(self.dict_xy.iteritems(), key = lambda x:x[1], reverse = False)
		# maxArea = 0

		# for i in range(len(self.dict_sorted)):
		# 	index1 = self.dict_sorted[i][0]
		# 	for j in range(i+1, len(self.dict_sorted)):
		# 		index2 = self.dict_sorted[j][0]
		# 		currentArea = self.computeArea(index1, index2)
        #
		# 		if currentArea > maxArea:
		# 			maxArea = currentArea
		# 		print index1, index2, maxArea

		# for i in range(len(self.dict_sorted)):
		# 	index1 = self.dict_sorted[i][0]
		# 	#print index1
		# 	index2 = self.findfarindex(index1,i)
        #
		# 	currentArea = self.computeArea(index1, index2)
		# 	if currentArea > maxArea:
		# 		maxArea = currentArea
		# return maxArea
		maxArea = 0
		l = 0
		r = len(height)-1
		while(l < r):
			currentArea = (r-l) * min(height[r],height[l])
			if currentArea > maxArea:
				maxArea = currentArea
			if height[l] < height[r]:
				# as height[l] < height[r]
				# min(height[l] , height[r-1]) * (r-l-1) must < currentArea , so l += 1
				l += 1
			else:
				r -= 1
		return maxArea
	# def computeArea(self, index1, index2):
	# 	return abs(index1 - index2) * min(self.dict_xy[index1],self.dict_xy[index2])

	# def findfarindex(self, index,ii):
	# 	#print self.dict_sorted
	# 	#print 'index',index
	# 	dict_2sort = dict(i for i in self.dict_sorted[ii:])
	# 	#print dict_2sort
	# 	res =  sorted(dict_2sort.iteritems(), key = lambda x:abs(x[0]-index), reverse= True)[0][0]
	# 	#print res
	# 	return res
if __name__ == '__main__':
	height = [1,2,3,4,5,25,24,3,4]
	sol = Solution()
	res = sol.maxArea(height) 
	print res
