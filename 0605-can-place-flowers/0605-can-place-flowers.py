class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if not n : return True

        if len(flowerbed) == 1 and flowerbed[0] == 0 and n <=1 : return True

        flowers_left = n

        if flowerbed[0] == 0 and flowerbed[1] == 0 : 
            flowerbed[0] = 1
            flowers_left -=1
            if flowers_left == 0 : return True

        if flowerbed[-1] == 0 and flowerbed[-2] == 0 : 
            flowerbed[-1] = 1
            flowers_left -=1

            if flowers_left == 0 : return True

        for i in range(1, len(flowerbed)-1):

            if flowerbed[i] == 0 :

                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:

                    flowerbed[i] = 1
                    flowers_left -= 1

                    if flowers_left == 0 : return True

        return flowers_left == 0
            

