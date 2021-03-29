# Após dar run no code, existe um intervalo de tempo até sair o resultado
import imdb
ia = imdb.IMDb()
pesquisa = ia.get_top250_movies()
for i in range(10):
    print(pesquisa[i])

# Copiei o código para treinar desse video: https://www.youtube.com/watch?v=6hWvoIaoL30
