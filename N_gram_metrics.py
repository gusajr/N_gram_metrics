def create_ngrams(word, n):
  # se convierten las palabras en tokens
  tokens = [token for token in word]
  # se generan los ngramas usando zip
  ngrams = zip(*[tokens[i:] for i in range(n)])
  # se juntan con un espacio y se devuelve
  return [''.join(ngram) for ngram in ngrams]

#número de gramas
N=2

#uso de función para crear gramas
cadena_1 = create_ngrams("Rata", N)
cadena_2 = create_ngrams("Ratón", N)

#se calculan los bigramas en común
sum_bigram = 0
for bigram in cadena_1:
  if(bigram in cadena_2):
    sum_bigram = sum_bigram + 1

#se calculan los bigramas totales
total_bigrams = len(cadena_1)+len(cadena_2)

#fórmula para calcular la distancia
distance_bigram = N * sum_bigram / total_bigrams

#se imprime la distancia
distance_bigram