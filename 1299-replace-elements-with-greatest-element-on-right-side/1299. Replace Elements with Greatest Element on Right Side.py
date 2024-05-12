class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1] #reverse the array
        res = [] # create a new array to store variables
        max = -1 # initialize the max variable

        for i in arr: 
            res.append(max) #append the max variable to new array
            if i > max: #if i is greater than the max variable, set to max to i
                max = i
        return res[::-1] # return reversed new array