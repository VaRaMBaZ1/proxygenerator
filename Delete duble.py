f1 = input("Введите название файла: ")

with open(f1) as input_:
    result = dict.fromkeys(input_).keys()
    
with open(f1, "w") as output:
    print(*result, file=output, sep="")
    
print("Все дубликаты удалены!")