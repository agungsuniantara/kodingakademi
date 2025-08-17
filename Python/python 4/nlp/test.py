def reverse(src, dst):
    collect = [] 
    with open(f"{src}.txt", "r") as file:
        for line in file:
            collect.append(line)
    
    reverse_collect = collect[::-1]
    with open(f"{dst}.txt", "w") as file:
        for line in reverse_collect:
            file.write(line)

reverse("input", "output")