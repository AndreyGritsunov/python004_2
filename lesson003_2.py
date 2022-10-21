def result_print(sum_result):

    print("Сумма: " + str(sum_result))

def result_program():
    i = 0
    j = len(n) - 1
    if j == 0:
        print("Массив пуст")    
    else:
        while i <= j:
            result_print(n[i] + n[j])
            i += 1
            j -= 1 

        
def list_creat():
    i = 0
    while i < 1:
        input_man = int(input("Введите число для добавления в массив или 0 для завершения: "))
        if input_man == 0:
            print(n)
            result_program()
            break
        else:
             n.append(input_man)

n = []
list_creat()