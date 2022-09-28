import imdb
import csv

ia = imdb.IMDb()

code1 = '20880628'
series1 = ia.get_movie(code1)
imdbID1 = series1.data['imdbID']
title1 = series1.data['title']
year1 = series1.data['year']
genres1 = series1.data['genres']
kind1 = series1.data['kind']

code2 = '10872600'
series2 = ia.get_movie(code2)
imdbID2 = series2.data['imdbID']
title2 = series2.data['title']
year2 = series2.data['year']
genres2 = series2.data['genres']
kind2 = series2.data['kind']

code3 = '3501632'
series3 = ia.get_movie(code3)
imdbID3 = series3.data['imdbID']
title3 = series3.data['title']
year3 = series3.data['year']
genres3 = series3.data['genres']
kind3 = series3.data['kind']

code4 = '9419884'
series4 = ia.get_movie(code4)
imdbID4 = series4.data['imdbID']
title4 = series4.data['title']
year4 = series4.data['year']
genres4 = series4.data['genres']
kind4 = series4.data['kind']

code5 = '7131622'
series5 = ia.get_movie(code5)
imdbID5 = series5.data['imdbID']
title5 = series5.data['title']
year5 = series5.data['year']
genres5 = series5.data['genres']
kind5 = series5.data['kind']


colunas = ['imdbID', 'title', 'year', 'genres', 'kind']

linhas = [
    [imdbID1, title1, year1, genres1, kind1],
    [imdbID2, title2, year2, genres2, kind2],
    [imdbID3, title3, year3, genres3, kind3],
    [imdbID4, title4, year4, genres1, kind4],
    [imdbID5, title5, year5, genres5, kind5]
]

with open('lista_filmes.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(colunas)
    write.writerows(linhas)

"""
# O arquivo .csv deve ter os seguintes dados:

imdbID,title,year,genres,kind

20880628,Top Gun Maverick,2022,['Comedy'],podcast episode

10872600,Spider-Man: No Way Home,2021,"['Action', 'Adventure', 'Fantasy', 'Sci-Fi']",movie

3501632,Thor: Ragnarok,2017,"['Action', 'Adventure', 'Comedy', 'Fantasy', 'Sci-Fi']",movie

9419884,Doctor Strange in the Multiverse of Madness,2022,['Comedy'],movie

7131622,Once Upon a Time in Hollywood,2019,"['Comedy', 'Drama']",movie
"""