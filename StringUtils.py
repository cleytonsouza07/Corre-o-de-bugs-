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

