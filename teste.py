# Correções e testes para as classes fornecidas

# FibonacciGenerator corrigido
class FibonacciGenerator:
    def generate_sequence(self, n):
        """
        Gera os primeiros n números da sequência de Fibonacci.
        :param n: Número de elementos na sequência.
        :return: Lista contendo a sequência de Fibonacci.
        """
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        
        sequence = [0, 1]
        for _ in range(2, n):  # Corrigir o loop para iniciar de 2, pois os dois primeiros já estão na lista
            next_number = sequence[-1] + sequence[-2]  # Corrigir para somar os dois últimos elementos corretamente
            sequence.append(next_number)
        return sequence

    def get_nth_number(self, n):
        """
        Retorna o enésimo número da sequência de Fibonacci (baseado em índice 1).
        :param n: Posição do número na sequência (1-indexed).
        :return: Número correspondente na sequência.
        """
        if n <= 0:
            return None
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b  # Corrigir a atualização dos valores corretamente
        return b

# StringUtils corrigido
class StringUtils:
    def reverse_string(self, s):
        """
        Reverte a string fornecida.
        :param s: String a ser revertida.
        :return: String revertida.
        """
        return s[::-1]  # Corrigir para retornar a string invertida

    def is_palindrome(self, s):
        """
        Verifica se a string é um palíndromo.
        :param s: String a ser verificada.
        :return: True se for palíndromo, False caso contrário.
        """
        return s == s[::-1]

# UserManager corrigido
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        """
        Adiciona um usuário à lista, caso ele não exista.
        :param user: Usuário a ser adicionado.
        :return: Mensagem se o usuário já existir.
        """
        if user not in self.users:
            self.users.append(user)
        else:
            return "User already exists"

    def remove_user(self, user):
        """
        Remove um usuário da lista, caso ele exista.
        :param user: Usuário a ser removido.
        :return: Mensagem se o usuário não existir.
        """
        if user in self.users:
            self.users.remove(user)
        else:
            return "User does not exist"

# Testes automatizados utilizando unittest
import unittest

class TestFibonacciGenerator(unittest.TestCase):
    def setUp(self):
        self.fib = FibonacciGenerator()

    def test_generate_sequence(self):
        self.assertEqual(self.fib.generate_sequence(0), [])
        self.assertEqual(self.fib.generate_sequence(1), [0])
        self.assertEqual(self.fib.generate_sequence(5), [0, 1, 1, 2, 3])

    def test_get_nth_number(self):
        self.assertIsNone(self.fib.get_nth_number(0))
        self.assertEqual(self.fib.get_nth_number(1), 0)
        self.assertEqual(self.fib.get_nth_number(6), 5)

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    def test_reverse_string(self):
        self.assertEqual(self.utils.reverse_string("hello"), "olleh")
        self.assertEqual(self.utils.reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(self.utils.is_palindrome("madam"))
        self.assertFalse(self.utils.is_palindrome("hello"))

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserManager()
        self.manager.add_user("Alice")

    def test_add_user(self):
        self.assertIsNone(self.manager.add_user("Bob"))
        self.assertEqual(self.manager.add_user("Alice"), "User already exists")

    def test_remove_user(self):
        self.assertIsNone(self.manager.remove_user("Alice"))
        self.assertEqual(self.manager.remove_user("Bob"), "User does not exist")

if __name__ == "__main__":
    unittest.main()
