def main():
    f = open("puzzle5-input.txt", "r")
    max_seat_id = 0
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
        seat_id = int(row_bin, 2) * 8 + int(col_bin , 2)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
          
    print(max_seat_id)

main()