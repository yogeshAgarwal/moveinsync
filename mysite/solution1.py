class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        len_tree = len(tree)
        i = 0
        max_value = 0
        while(i<len_tree):
            # print("outer",i)
            value = 0
            aa = set()
            aa.add(tree[i])
            temp_index = i
            value += 1
            i += 1
            # print("outer,set",aa)
            while(i<len_tree):
                # print("inner",i)
                aa.add(tree[i])
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
