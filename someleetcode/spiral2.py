class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
         res = [[0 for _ in range(n)] for _ in range(n)]
    
        i, j, di, dj = 0, 0, 0, 1

        for k in range(n*n):

            res[i][j]=k+1

            if res[(i+di)%n][(j+dj)%n]:

                di, dj = dj, -di

            i+=di
            j+=dj

        return res
        
        
        ^ Very smart way of handling directions. Recognized:
        x 1 0 -1 0
        y 0 1 0 -1
        check array to see if you hit that index already. If you have, x = -y, y = x
        """
        arr = []
        for i in range(n):
            temp = []
            for j in range(n):
                 temp.append(0)
            arr.append(temp)
        act_x = [1,0,-1,0]
        act_y = [0,1,0,-1]
        action = 0
        cur_x = 0
        cur_y = 0
        used = [[False for i in range(n)] for _ in range(n)]
        for i in range(n**2):
            #print("{} {}".format(cur_x, cur_y))
            arr[cur_y][cur_x] = i+1
            #print(i+1)
            #print(arr)
            used[cur_y][cur_x] = True
            tx = cur_x+act_x[action]
            ty = cur_y+act_y[action]
            if (((0 <= tx < n) and (0 <= ty < n)) and not used[ty][tx]):
                cur_x, cur_y = tx,ty
            else:
                action = (action+1)%4
                cur_x+=act_x[action]
                cur_y+=act_y[action]
        return arr
            
            
            
