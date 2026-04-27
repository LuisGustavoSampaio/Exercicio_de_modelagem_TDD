import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model import Cliente, ContaPoupanca


class TestInvestimentoPoupanca(unittest.TestCase):
    def test_deve_aplicar_rendimento_na_poupanca(self):
        # Arrange
        cliente = Cliente("Luis", "12345678900", "01/01/2000", "Salvador")
        conta_poupanca = ContaPoupanca(cliente, numero=1)
        conta_poupanca.depositar(1000)

        # Act
        rendimento = conta_poupanca.aplicar_rendimento()

        # Assert
        self.assertAlmostEqual(rendimento, 5)
        self.assertAlmostEqual(conta_poupanca.saldo, 1005)


if __name__ == "__main__":
    unittest.main()
