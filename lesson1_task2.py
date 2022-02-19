time = int(input("Введите время в секундах:"))
hh = time // 3600
mm = (time % 3600) // 60
ss = (time % 3600) % 60
print(f"{hh:02d}",":",f"{mm:02d}",":",f"{ss:02d}")

