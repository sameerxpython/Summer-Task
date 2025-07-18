import psutil

mem = psutil.virtual_memory()

print(f"Total RAM     : {mem.total / (1024 ** 3):.2f} GB")
print(f"Available RAM : {mem.available / (1024 ** 3):.2f} GB")
print(f"Used RAM      : {mem.used / (1024 ** 3):.2f} GB")
print(f"RAM Usage     : {mem.percent} %")
