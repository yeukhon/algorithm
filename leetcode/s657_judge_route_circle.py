# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# 657. Judge Route Circle
# Initially, there is a Robot at position (0, 0). Given a sequence of
# its moves, judge if this robot makes a circle, which means it moves
# back to the original place.
#
# The move sequence is represented by a string. And each move is
# represent by a character. The valid robot moves are R (Right),
# L (Left), U (Up) and D (down). The output should be true or false
# representing whether the robot makes a circle.
#
# Example 1:
# Input: "UD"
# Output: true
#
# Example 2:
# Input: "LL"
# Output: false

from functools import partial

def position_calc(x=False, y=False, move=0, position=None):
    if x:
        return (position[0]+move, position[1])
    elif y:
        return (position[0], position[1]+move)
    else:
        raise Exception("I don't think you know how to calculate position.")

moveYUp = partial(position_calc, y=True, move=1)
moveYDown = partial(position_calc, y=True, move=-1)
moveXLeft = partial(position_calc, x=True, move=-1)
moveXRight = partial(position_calc, x=True, move=1)

MOVES_MAPPING = {
    'U': moveYUp,
    'D': moveYDown,
    'L': moveXLeft,
    'R': moveXRight
    
}
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        position = (0,0)
        for m in moves:
            position = MOVES_MAPPING[m](position=position)
        if position == (0,0):
            return True
        else:
            return False
