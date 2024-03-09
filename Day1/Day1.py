year = input("When did u born: ")


def calc_can_chi_calendar(year):
    residual_can = year % 10
    residual_chi = year % 12

    # calc can
    Can = {
        0: "Canh",
        1: "Tan",
        2: "Nham",
        3: "Quy",
        4: "Giap",
        5: "At",
        6: "Binh",
        7: "Dinh",
        8: "Mau",
        9: "Ky",
    }

    # calc chi
    Chi = {
        0: "Than",
        1: "Dau",
        4: "Hoi",
        5: "Suu",
        6: "Dan",
        7: "Meo",
        8: "Thin",
        9: "Ty",
        10: "Ngo",
        11: "Mui",
    }

    return f"Result: {Can.get(residual_can)} {Chi.get(residual_chi)}"


print(calc_can_chi_calendar(int(year)))
