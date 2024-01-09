class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])
        days_of_month = [0, 31, 28 + self.isLeapYear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(days_of_month[0:month]) + day

    def isLeapYear(self, year: int) -> int:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 1
        else:
            return 0



