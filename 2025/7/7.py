with open('input', 'r') as file:
    lines = file.read().splitlines()
    beams = set()
    split = 0
    for i in range(0, len(lines[0])):
        if lines[0][i] == 'S':
            beams.add(i)
    lines = lines[1:]
    for row_num in range(0, len(lines)):
        row = lines[row_num]
        hit_beams = set()
        for beam in beams:
            if row[beam] == '^':
                hit_beams.add(beam)
        split += len(hit_beams)
        for hit_beam in hit_beams:
            beams.remove(hit_beam)
            beams.add(hit_beam - 1)
            beams.add(hit_beam + 1)
    print(split)