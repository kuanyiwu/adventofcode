class Node:
    def __init__(self, color, holder_color):
        self.color = color
        self.holder_color = []
        self.holder_color.extend(holder_color)

def main():
    f = open("puzzle7-input.txt", "r")
    input = set()
    for line in f:
        contain = line.split(" contain ")
        holder = contain[0].replace(" bags", "")
        holder_split = holder.split(" ")
        holder_color = holder_split[0] + holder_split[1]
        bags = contain[1].split(", ")
        for bag in bags:
            parse = bag.split(" ")
            # num = parse[0]
            color = parse[1] + parse[2]
            input.add(color + " "+ holder_color)
    




main()