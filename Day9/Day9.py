

lst_data = []
for i in range(1, 11):
    lst_data.append(i)

def remove_even_nums(num):
    if (num % 2 != 0): 
        return num
    else: 
        return None


def calc_demian(lst_data):
    if len(lst_data) % 2 == 0:
        x1 = len(lst_data) / 2
        x2 = x1 - 1
        demian = (lst_data[x1] + lst_data[x2]) / 2
        return demian

