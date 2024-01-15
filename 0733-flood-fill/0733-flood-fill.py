class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue = deque()

        queue.append((sr,sc))

        visited = set()

        m = len(image)

        n = len(image[0])

        while queue :

            row, col = queue.popleft()

            visited.add((row, col))


            # row + 1, col
            # row - 1, col

            # row, col + 1
            # row, col - 1

            if row + 1 < m and (row+1, col) not in visited:
            
                if image[row+1][col] == image[row][col] :

                    queue.append((row+1, col))

            if row - 1 >= 0 and (row-1, col) not in visited:
            
                if image[row-1][col] == image[row][col] :

                    queue.append((row-1, col))
            
            if col + 1 < n and (row, col+1) not in visited:
            
                if image[row][col + 1] == image[row][col] :

                    queue.append((row, col + 1))
            
            if col - 1 >= 0 and (row, col - 1) not in visited:
            
                if image[row][col - 1] == image[row][col] :

                    queue.append((row, col - 1))

            image[row][col] = color

        
        return image

        
        

