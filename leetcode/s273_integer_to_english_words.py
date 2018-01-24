class Solution(object):

    digit_en = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "one hundred"
    }

    place_en = {
        0: "ones",
        1: "ten",
        2: "hundred",
        3: "thousand",
        4: "ten thousand",
        5: "hundred thousand",
        6: "million",
        7: "ten million",
        8: "hundred million",
        9: "billion"
    }

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        s_num = str(num)
        num_length = len(s_num)
        
        if num_length == 1:
            return self.digit_en[num].title()
        
        # We will work backward to match place_en which is the natural way
        # to look at place value in English.
        s_num = list(reversed(s_num))

        output_list = []
        # three-intger chunk per call
        for i in range(0, num_length, 3):
            output_list.append(
                self._num_to_words(s_num, i))

        # remember the words in the list are in reverse order, so concate backward
        output = " ".join(filter(None, reversed(output_list)))
        return output.title()

    def _num_to_words(self, snum, start):
        # work three chunks at a time: p1, p2, p3
        # if the original num = 123, the snum in the recrusion is 321
        # then p1 = 3, p2 = 2, p3 = 1
        p1_slot = True
        p2_slot, p3_slot = False, False
        p1 = int(snum[start])
        p2, p3 = None, None

        if start + 1 < len(snum):
            p2 = int(snum[start + 1])
            p2_slot = True
            if start + 2 < len(snum):
                p3 = int(snum[start + 2])
                p3_slot = True

        #import pdb; pdb.set_trace()
        # we are still working with three chunks
        if p1_slot and p2_slot and p3_slot:
            if int(p3 * 100 + p2 * 10 + p1) == 0:
                return ""
            # [321] -> one hundred twenty three
            elif start < 3 and int(p3 * 100 + p2 * 10 + p1) <= 999:
                output = [self.digit_en[p3],
                          self.place_en[start + 2].split()[-1]]
                if p2 != 0:
                    if int(p2 * 10 + p1) > 20 and p1 != 0:
                        output += [self.digit_en[p2*10],
                             self.digit_en[p1]]
                    else:
                        output.append(self.digit_en[p2 * 10 + p1])
                if p2 == 0 and p1 != 0:
                    output += [self.digit_en[p1]]
            else:
                output = [self.digit_en[p3],
                 self.place_en[start + 2].split()[0],
                 self.digit_en[p2 * 10],
                 self.digit_en[p1],
                 self.place_en[start].split()[-1]
            ]
            return " ".join(output)

        elif p1_slot and p2_slot:
            s1 = p2 * 10 + p1
            if s1 in self.digit_en:
                s1 = self.digit_en[s1]
            else:
                # thirty eight for example
                s1 = self.digit_en[p2 * 10] + " " + self.digit_en[p1]
            if start + 1 == 1:
                output = [s1]
            else:
                output = [s1, self.place_en[start + 1].split()[-1]]
            return " ".join(output)

        # p1 and p3 -> 302 -> two hundred and three
        elif p1_slot and p3_slot:
            output = [self.digit_en[p1],
                     self.place_en[start + 1].split()[-1],
                     self.digit_en[p3]
            ]
            return " ".join(output)
        else:
            if start == 0:
                return self.digit_en[p1]
            else:
                output = [self.digit_en[p1],
                    self.place_en[start]]
                return " ".join(output)
so = Solution()

op = so.numberToWords(123)
print(op)
assert op == "One Hundred Twenty Three"


op = so.numberToWords(12345)
print(op)
assert op == "Twelve Thousand Three Hundred Forty Five"


op = so.numberToWords(21)
print(op)
assert op == "Twenty One"

op = so.numberToWords(1234567)
print(op)
assert op == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

op = so.numberToWords(10)
print(op)
assert op == "Ten"


op = so.numberToWords(100)
print(op)
assert op == "One Hundred"

op = so.numberToWords(101)
print(op)
assert op == "One Hundred One"


op = so.numberToWords(111)
print(op)
assert op == "One Hundred Eleven"

op = so.numberToWords(130)
print(op)
assert op == "One Hundred Thirty"

op = so.numberToWords(1000)
print(op)
assert op == "One Thousand"
