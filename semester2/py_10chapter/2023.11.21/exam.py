import json

infile = open("./exam/score.json", "r")
outfile = open("./exam/grade,json", "w")

sum = 0
count = 0


    

outfile.write("총매출 = " + str(sum) + "\n")
outfile.write("평균 입매출 = " + str(sum/count) + "\n")

infile.close()
outfile.close()