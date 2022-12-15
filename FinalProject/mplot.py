import csv

index_now = 0
movie_id = []

with open('mplot_final.csv',newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        catch = []  #存當下的摘要
        movie_id = []
        index_now = int(row[0])
        movie_id.append(row[1])
        catch.append(row[2])

        filename = str(movie_id[0]) + '.txt'
        fk = open('data/' + filename,'a')
        fk.write(catch[0])
        fk.close