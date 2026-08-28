class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        primo, secondo = None, 0 
        operator = {"+","-","/","*"}
        stack = []
        for toke in tokens:
            if toke in operator:
                if toke == "+":
                    #primo = primo + secondo
                    stack.append(stack.pop() + stack.pop())
                elif toke == "-":
                    #primo = primo - secondo
                    tmp = stack.pop()
                    stack.append(stack.pop() - tmp)
                elif toke == "*":
                    #primo = primo * secondo
                    stack.append(stack.pop() * stack.pop())
                else:
                    #primo = primo // secondo
                    tmp = stack.pop()
                    
                    stack.append(int(stack.pop() / tmp))
            else:
                stack.append(int(toke))
            
            #print(toke,stack)

        return stack[0]

            
            
