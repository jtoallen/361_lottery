import csv


with open('/Users/jason/cs361/Aaron_Project/output.txt') as fin, \
        open('output.csv', 'wb') as fout:
        csvin = csv.reader(fin)
        csvout = csv.writer(fout, delimiter='\t')

        for row in csvin:
            if row[1].strip(" ' ") == 'Toronto Maple Leafs':
                print("The Toronto Maple Leafs score is", row[2])
                score = row[2].strip("[]")
                score = score.strip()
                with open('hockeyscore.txt', 'w') as inscore:
                    inscore.write(score)
            elif row[3].strip(" ' ") == 'Toronto Maple Leafs':
                score = row[4].strip("[]")
                print("Toronto Maple Leafs score is", score)
                score = score.strip()
                with open('hockeyscore.txt', 'w') as inscore:
                    inscore.write(score)



