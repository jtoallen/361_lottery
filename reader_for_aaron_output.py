import csv


with open('/Users/jason/cs361/Aaron_Project/output.txt') as fin, open('output.csv', 'wb') as fout:
        csvin = csv.reader(fin)
        csvout = csv.writer(fout, delimiter='\t')
        csvout = csv.writer(fout)

        for row in csvin:
            # print("row type is ", type(row))
            # print(" row[3] type is ", type(row[3]))
            # print(row[3].strip('[]'))
            # row[3].strip("[]")
            # print("row 3 is type", type(row[3]), (row[3].strip("'")))

            #row 1 is teams
            #row 2 is scores
            # print(row[2:3]) #score as string
            if row[1].strip(" ' ") == 'Nashville Predators':
                print("Row 1 is ", row[1])
                print("Nashville Predators score is", row[2])
                print(type(row[2]))
                score = row[2].strip()
                # print(score)
                print("type of score is ", type(score))
                with open('hockeyscore.txt', 'w') as inscore:
                    inscore.write(score)
                    print("score written to hockey_score is ", score)
            #     random_nums.append(score)
        # print("Powerball", random_nums)
        # with open('numbers.txt', 'w') as outfile:
            # outfile.write(str(random_nums))
            # if row[1] == " 'Florida Panthers' ":
            #     print("scores for TBL " , row[2])
             # csvout.writerow([','.join(row[:5], ','.join(row[5:]))])



    # reader = reader.strip()

    # print(reader[0][38])
    # try:
    #     for row in reader:
    #         # if count <=10:
    #             # count +=1
    #         # if row == "search":
    #         # print(', '.join(row))
    #
    #             print(row[36:38])
    # #         else:
    # #             break
    # except UnicodeDecodeError:
    #     print("problem", row)
    #     # print(row[0][3])
    # print("The number of rows printed is {}".format(count))