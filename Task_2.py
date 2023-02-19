def print_operation_table(operation, num_rows=6, num_columns=6):
    work_list = []
    for i in range(1, num_rows + 1):
        work_row = ''
        for j in range(1, num_columns + 1):
            work_row += str(operation(i, j)) + ' ' 
        print(work_row)

print_operation_table(lambda x, y: x * y)