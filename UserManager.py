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

