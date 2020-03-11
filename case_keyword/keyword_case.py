# coding = utf-8
from action.action_method import ActionMethod
from report.excel_util import ExcelUtil
from selenium.webdriver.support import expected_conditions as EC


class KeyWordCase:

    def __init__(self):
        self.a_m = ActionMethod()

    def run_main(self):

        handle_excel = ExcelUtil("../config/key_word.xlsx")
        case_lines = handle_excel.get_rows()
        if case_lines is not None:
            for i in range(1, case_lines):
                is_run = handle_excel.get_colum_value(i, 3)
                if is_run is not None:
                    case_method = handle_excel.get_colum_value(i, 4)
                    input_data = handle_excel.get_colum_value(i, 5)
                    # except_result = handle_excel.get_colum_value(i)
                    operation_element = handle_excel.get_colum_value(i, 6)
                    print(
                        "方法名：%s，输入数据：%s，操作元素：%s" %
                        (case_method, input_data, operation_element))
                    if case_method == "open_browser" or case_method == "send_value" or case_method == "click_element" or case_method == "get_url" or case_method == "sleep_time" or case_method == "driver_close":
                        if input_data is not None:
                            # and operation_element is not None
                            self.run_method(
                                case_method, input_data, operation_element)
                            # self.a_m.sleep_time(2)

                        # elif operation_element is not None and input_data is None:
                        #     self.run_method(case_method, operation_element)
                        # elif operation_element is None:
                        #     self.run_method(case_method, input_data)
                        # else:
                        #     self.run_method(case_method)

                    else:
                        print("请检查您的用例文件，方法名是否正确")
                        return

        else:
            print("请检查您的用例文件")
            return
        # self.a_m.driver_close()

        # 获取行数
        # 循环行数，执行用例
        # 执行
            # 输入
            # 获取执行方法
            # 获取操作数据
            # 获取操作元素
            # 执行方法（数据，元素）
            # 不输入
            # 获取执行方法
            # 获取操作元素
            # 执行方法

    def run_method(self, method, input_data=None, operation_element=None):

        mehtod_value = getattr(self.a_m, method)
        i_data = str(input_data)
        print(len(i_data))
        if operation_element is not None:
            mehtod_value(operation_element, i_data)
        elif input_data is not None:
            mehtod_value(i_data)
        # else:
        #     mehtod_value()


if __name__ == '__main__':

    kwc = KeyWordCase()
    kwc.run_main()
