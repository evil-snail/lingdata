lines = []
elements = []
with open ("def.txt", encoding="utf-8") as f:
    for line in f:
        elements = line.split()
        lines.append(elements[0].strip(","))
        elements = []
with open ("new_def.txt", "w", encoding='utf-8') as f:
    for line in lines:
        f.write(line)
        f.write("\n")
