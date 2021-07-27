def generateParenthesis(n: int) -> List[str]:
        if n == 1:
            return ["()"]
        res_list = []
        def check_valid(par_str):
            stack = []
            t_n = 0
            for i in par_str:
                if i == "(":
                    stack.append(i)
                else:
                    if stack:
                        if stack.pop() == "(":
                            t_n+=1
                        else:
                            break
                    else:
                        break
            return t_n
        def generate_p(stri):
            #print(stri)
            stri_2 = "".join(stri)
            #print(stri_2)
            if len(stri) <= 2*n:
                
                if check_valid(stri_2) == n:
                    print(stri_2)
                    res_list.append(stri_2)
                else:
                    #initially i did a for loop but the choices are binary. Add ( or ).
                    #also if I kept the forloop the list would have repeats
                    stri.append("(")
                    generate_p(stri)
                    stri.pop()
                    stri.append(")")
                    generate_p(stri)
                    stri.pop()

        generate_p([])
        print(res_list)
        return res_list
        
                    
                    
            
            
            