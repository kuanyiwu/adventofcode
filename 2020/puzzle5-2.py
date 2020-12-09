def main():
    f = open("puzzle5-input.txt", "r")
    seat_set = set()
    for line in f:
        row_bin = ''
        for i in range(7):
            if line[i] == 'F':
                row_bin += '0'
            else:
                row_bin += '1'
        col_bin = ''
        for i in range(7, 10):
            if line[i] == 'L':
                col_bin += '0'
            else:
                col_bin += '1'
        seat_bin = row_bin + col_bin
        seat_set.add(seat_bin)
    seat_list = sorted(seat_set)
    prev = int(seat_list[0], 2)
    for seat in seat_list:
        seat_num = int(seat, 2)
        if prev + 1 != seat_num:
            seat_id = int(seat[:7], 2) * 8 + int(seat[7:] , 2) - 1
            print(seat_id)
        prev = seat_num

main()