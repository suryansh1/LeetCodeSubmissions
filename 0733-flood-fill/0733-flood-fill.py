class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        queue = deque()

        queue.append((sr,sc))

        visited = set()

        m = len(image)

        n = len(image[0])

        while queue :

            cur = queue.popleft()

            visited.add((cur[0], cur[1]))


            # cur[0] + 1, cur[1]
            # cur[0] - 1, cur[1]

            # cur[0], cur[1] + 1
            # cur[0], cur[1] - 1

            if cur[0] + 1 < m and (cur[0]+1, cur[1]) not in visited:
            
                if image[cur[0]+1][cur[1]] == image[cur[0]][cur[1]] :

                    queue.append((cur[0]+1, cur[1]))

            if cur[0] - 1 >= 0 and (cur[0]-1, cur[1]) not in visited:
            
                if image[cur[0]-1][cur[1]] == image[cur[0]][cur[1]] :

                    queue.append((cur[0]-1, cur[1]))
            
            if cur[1] + 1 < n and (cur[0], cur[1]+1) not in visited:
            
                if image[cur[0]][cur[1] + 1] == image[cur[0]][cur[1]] :

                    queue.append((cur[0], cur[1] + 1))
            
            if cur[1] - 1 >= 0 and (cur[0], cur[1] - 1) not in visited:
            
                if image[cur[0]][cur[1] - 1] == image[cur[0]][cur[1]] :

                    queue.append((cur[0], cur[1] - 1))

            image[cur[0]][cur[1]] = color

        
        return image

        
        

