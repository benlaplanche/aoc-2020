# expenses.py

def calculate_total(expense_list):

    for index, current_val in enumerate(expense_list):
        temp_list = expense_list
        temp_list.pop(index)

        for i, v in enumerate(temp_list):
            if current_val + v == 2020:
                return current_val * v
