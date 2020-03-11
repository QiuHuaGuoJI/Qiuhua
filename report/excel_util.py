# coding = utf-8

import xlrd
from xlutils.copy import copy


class ExcelUtil:
    """读取Excel文件中的数据"""

    def __init__(self, excel_path=None, index=None):
        if excel_path is None:
            self.excel_path = "../config/key_word.xlsx"
        if index is None:
            index = 0

        self.case_data = xlrd.open_workbook(self.excel_path)
        self.case_table = self.case_data.sheets()[index]

    def get_rows(self):
        """获取表格的行数"""
        case_table_rows = self.case_table.nrows
        if case_table_rows >= 1:
            return case_table_rows
        return None

    def get_colum_value(self, row, cloum):
        self.case_data = xlrd.open_workbook(self.excel_path)
        """获取表格列的值"""
        if self.get_rows() is not None and self.get_rows() > row:

            case_rw_data = self.case_table.cell(row, cloum).value
            if len(str(case_rw_data)) > 0:
                return case_rw_data
        return None

    def get_data(self):
        """获取表格数据"""
        result = []
        rows = self.get_rows()
        if rows is not None:
            for i in range(rows):
                colum = self.case_table.row_values(i)
                result.append(colum)
                # print(colum)
                return result
        return None

    def write_value(self, row, value):
        """写入数据"""
        read_value = self.case_data
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row, 9, value)
        write_data.save(self.excel_path)


if __name__ == '__main__':
    ex = ExcelUtil("../config/key_word.xlsx")
    print("——————————————")
    print(ex.get_colum_value(1, 5))
    # ex.write_value(2, "ssss")
