class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
   
        s = list(s)
        actual_shift = 0
        for shift_item in shift:
            if shift_item[0] == 0:
                actual_shift += shift_item[1]
            else:
                actual_shift -= shift_item[1]
        
        print(actual_shift)
        if actual_shift == 0:
            return ''.join(s)
        elif actual_shift > 0:
            for i in range( actual_shift ):
                pop_item = s.pop(0)
                s.append(pop_item)
        else:
            for i in range(abs(actual_shift)):
                pop_item = s.pop(-1)
                print(pop_item)
                s.insert( 0 , pop_item )       

        return ''.join(s)