"""An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the
pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same
color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        def _change_color(image, sr, sc, color, original_color):
            if not (0 <= sr < len(image) and 0 <= sc < len(image[0])) or image[sr][sc] != original_color:
                return
            else:
                image[sr][sc] = color
                _change_color(image, sr - 1, sc, color, original_color)
                _change_color(image, sr, sc - 1, color, original_color)
                _change_color(image, sr + 1, sc, color, original_color)
                _change_color(image, sr, sc + 1, color, original_color)

        original_color = image[sr][sc]
        if color != original_color:
            _change_color(image, sr, sc, color, original_color)
        return image
