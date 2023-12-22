class Solution:



    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        row_count = len(image)
        column_count = len(image[0])

        q = []
        q.append([sr, sc])
        visited = []

        while q :
            
            # print(q)

            sr = q[0][0]
            sc = q[0][1]

            # Check 4 directional and add to queue

            # print (sr, row_count, "\t", sc, column_count, "\t", q)

            if (sr - 1) >= 0 and (image[sr-1][sc] == image[sr][sc]):

                if [sr-1, sc] not in visited : q.append([sr-1, sc])

            if (sc - 1) >= 0 and (image[sr][sc-1] == image[sr][sc]):

                if [sr, sc-1] not in visited : q.append([sr, sc - 1])

            if (sr + 1) < row_count and (image[sr+1][sc] == image[sr][sc]):

                if [sr+1, sc] not in visited : q.append([sr+1, sc])
            
            if (sc + 1) < column_count and (image[sr][sc+1] == image[sr][sc]):

                if [sr, sc+1] not in visited : q.append([sr, sc + 1])

            # Flood fill current

            image[sr][sc] = color
            
            q.pop(0)

            visited.append([sr,sc])

        return image

