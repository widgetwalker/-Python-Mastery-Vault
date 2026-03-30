x = int(input("enter the no.of movies: "))
import csv
file = open("diary.txt","a+")
file.write("HI AAKASH I AM YOUR VOICE ASSISTANT")
file.close()
file = open("diary.csv","a+",newline="")
csv = csv.writer(file)
for i in range(x):
    movie_name = input("enter the movie name: ")
    collection = int(input("enter the collection of movie in crores: "))
    csv.writerow([movie_name,collection])
file.close()