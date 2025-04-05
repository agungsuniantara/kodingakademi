test = {
    1 : "test1",
    2 : "test2",
    3 : "test3"
}

for key,value in test.items():
    if key % 2 != 0:
        test[key] = "hewan"

print(test)