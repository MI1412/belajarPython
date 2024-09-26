# seperti switch di python disebut match, digunakan untuk mengambil pola dari kondisi


# default match jika tidak diatur akan mengembalikan none
def http_status(status):
    match status:
        case 400:
            return "req gagal"
        case 404:
            return "resource tidak ada"
        case 200:
            return "sukses"
        case _:
            return "null"
        # case langsung
        # case 400 | 404 | 200:
        #     return "idk"

print(http_status(44))

point = (0,0)
match point:
    case (0,0):
        print("null")
    case _:
        raise ValueError("not a poin")

