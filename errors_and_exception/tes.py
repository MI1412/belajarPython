class ErrorA(Exception):
    pass

class ErrorB(Exception):
    pass

# Simulasi fungsi yang mengangkat kelompok eksepsi
def run_tasks():
    raise ExceptionGroup("Multiple errors", [
        ErrorA("Error A occurred"),
        ErrorB("Error B occurred"),
        ErrorB("Another Error B occurred")
    ])

try:
    run_tasks()
except* ErrorA as e:
    print(f"Caught an ErrorA: {e}")
except* ErrorB as e:
    print(f"Caught an ErrorB: {e}")

# Menangkap semua ExceptionGroup dan menghitung subeksepsi
except ExceptionGroup as eg:
    print(f"Caught an ExceptionGroup with {len(eg.exceptions)} subexceptions:")
    for sub_exception in eg.exceptions:
        print(f"- {sub_exception}")

