# exemplo 1 - bicicletas elétricas

class BicicletaInterna:
    def __init__(self, modelo, nivel_bateria):
        self.modelo = modelo
        self.nivel_bateria = nivel_bateria

    def calcular_distancia(self):
        return self.nivel_bateria * 0.5

    def obter_mensagem(self):
        distancia_restante = self.calcular_distancia()
        return f"{self.modelo}: Distancia estimada = {distancia_restante:.1f} km"

def main():
    modelo = input()
    nivel_str = input()
    nivel_bateria = int(nivel_str)

    bicicleta = BicicletaInterna(modelo, nivel_bateria)
    print(bicicleta.obter_mensagem())

if __name__ == "__main__":
    main()


# exemplo 2 - carros
class VerificadorCarro:
  @staticmethod

  def verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual):
    
    idade_carro = ano_atual - ano_fabricacao

    if idade_carro <= 10:
      return f"{modelo}: Apto"
    else:
      return f"{modelo}: Nao apto"

def main():
    modelo = input()
    ano_fabricacao = int(input())
    ano_atual = int(input())

    carro = VerificadorCarro.verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual)
    print(carro)

if __name__ == "__main__":
    main()