import os
from Modelos.Restaurante import Resturante

restaurante_praca = Resturante('praca', 'Gourmet')
restaurante_mexicano = Resturante('mexican food', 'Mexicana')
restaurante_japones = Resturante('Japan food', 'Japonesa')

restaurante_mexicano.alternar_estado()
restaurante_japones.alternar_estado()
restaurante_japones.receber_avaliacao('Gui', 2)
restaurante_praca.receber_avaliacao('Laís', 5)
restaurante_mexicano.receber_avaliacao('Will', 4)

def main():
    os.system('cls')
    Resturante.listar_restaurentes()
    print()
    


if __name__ == '__main__':
    main()