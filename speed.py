import time

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
c = 0

add_start = time.perf_counter_ns()
c = a + b
add_stop = time.perf_counter_ns()

mul_start = time.perf_counter_ns()
c = a * b
mul_stop = time.perf_counter_ns()

print("czas dodawania to: {0}".format(add_stop-add_start))
print("czas mnożenia to: {0}".format(mul_stop-mul_start))
print("różnica tych czasów to {0}".format((mul_stop-mul_start) - (add_stop-add_start)))
