class FirstUnique:

    def __init__(self, nums: List[int]):
        if len(nums) == 0:
            return -1
        
        #self.deque = collection.deque()
        self.dict = {'one':[nums[0]] , nums[0]:1}
        
        for num in nums[1:]:
            self.add(num)
        

    def showFirstUnique(self):
        unique_val = self.dict['one']
        
        if len(unique_val) >= 1:
            return unique_val[0]
        else:
            return -1
        
        

    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value] += 1
            unique_val = self.dict['one']
            
            if value in unique_val:
                unique_val.remove(value)
                self.dict['one'] = unique_val
            
        else:
            self.dict['one'] += [value]
            self.dict[value] = 1
            

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)