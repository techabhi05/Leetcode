class Solution:
    def flipAndInvertImage(self, image):

        # for reverse each row
        for img in image:
            i,j = 0,len(img)-1

            while i <= j:
                img[i],img[j] = img[j],img[i]
                i += 1
                j -= 1

        # for inverting the image
        for num in image:
            n = len(num)
            for i in range(n):
                if num[i] == 0:
                    num[i] = 1
                else:
                    num[i] = 0
        return image    