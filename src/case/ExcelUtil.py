#-*-coding:utf-8-*-

import xlrd


class ExcelUtil(object):

    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)

        # get titles
        self.row = self.table.row_values(0)

        # get rows number
        self.rowNum = self.table.nrows

        # get columns number
        self.colNum = self.table.ncols

        # the current column
        self.curRowNo = 1

    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

#这里实现的就是一个循环的功能，某表，某sheet，用data[字段名]的方式引用case数据；
if __name__ == "__main__":
    filepath = "case.xlsx"
    sheetName = "Sheet1"
    data = ExcelUtil(filepath, sheetName)
    print data.hasNext()




