class Solution:
    def totalFruit(self, input) -> int:
        len_input = len(input)
        i = 0
        max_value = 0
        while(i<len_input):
            # print("outer",i)
            value = 0
            aa = set()
            aa.add(input[i])
            temp_index = i
            value += 1
            i += 1
            # print("outer,set",aa)
            while(i<len_input):
                # print("inner",i)
                aa.add(input[i])
                if len(aa) == 1:
                    temp_index = i
                # print("inner set",aa)
                if len(aa) <= 2:
                    value +=1
                    i +=1
                else:
                    i = temp_index + 1
                    break
            if max_value < value:
                max_value = value
        return max_value
