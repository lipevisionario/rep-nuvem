import random 
quant_intervalo = int(input("coloque a quantidade de intervalos de 1 a 1000:"))
while quant_intervalo < 1 or quant_intervalo > 1000:
  quant_intervalo = int(input("coloque a quantidade de intervalos de 1 a 1000: "))
for i in range(1, quant_intervalo+1):
   tempo_t = random.randint(1, 100)
   velocidade_v = random.randint(1, 100)
   print(f"intervalo {i}| tempo_t {tempo_t} velocidade_v{velocidade_v} distancia{tempo_t*velocidade_v}")
total_percorrido = tempo_t * velocidade_v
soma = (tempo_t * velocidade_v)
print (f"O km total percorrido foi: {total_percorrido}")
