# ==============================================
# Project: Minimum Arrows to Burst Balloons
# Language: Python 3
# Author: ChatGPT
# ==============================================

from typing import List

class BalloonShooter:
    """
    This class provides a method to find the minimum number of arrows
    required to burst all balloons, where each balloon is represented
    as an interval [start, end].
    """

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # No balloons
        if not points:
            return 0
        
        # Sort balloons by their ending coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow needed
        current_end = points[0][1]

        for i in range(1, len(points)):
            # If the next balloon starts after the last arrow range,
            # we need a new arrow
            if points[i][0] > current_end:
                arrows += 1
                current_end = points[i][1]

        return arrows


# ==============================================
# Main program for demonstration
# ==============================================
if __name__ == "__main__":
    shooter = BalloonShooter()

    print("===============================================")
    print("      MINIMUM ARROWS TO BURST BALLOONS")
    print("===============================================")

    # Example 1
    points1 = [[10,16],[2,8],[1,6],[7,12]]
    print("\nExample 1:")
    print("Input balloons:", points1)
    print("Minimum arrows needed:", shooter.findMinArrowShots(points1))

    # Example 2
    points2 = [[1,2],[3,4],[5,6],[7,8]]
    print("\nExample 2:")
    print("Input balloons:", points2)
    print("Minimum arrows needed:", shooter.findMinArrowShots(points2))

    # Example 3
    points3 = [[1,2],[2,3],[3,4],[4,5]]
    print("\nExample 3:")
    print("Input balloons:", points3)
    print("Minimum arrows needed:", shooter.findMinArrowShots(points3))

    print("\n===============================================")
    print("Program Finished Successfully!")
    print("===============================================")
