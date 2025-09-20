class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = [[0] * 26 for _ in range(rows)]

    def getCell(self, cell: str):
        return ord(cell[0]) - 65, int(cell[1:]) - 1

    def setCell(self, cell: str, value: int) -> None:
        col, row = self.getCell(cell)
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col, row = self.getCell(cell)
        self.sheet[row][col] = 0

    def getValue(self, formula: str) -> int:
        val1, val2 = formula[1:].split("+")
        if all([val1.isdigit(), val2.isdigit()]):
            return int(val1) + int(val2)

        rtn = 0

        if not val1.isdigit():
            col, row = self.getCell(val1)
            rtn += self.sheet[row][col]

        else:
            rtn += int(val1)

        if not val2.isdigit():
            col, row = self.getCell(val2)
            rtn += self.sheet[row][col]

        else:
            rtn += int(val2)

        return rtn


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
