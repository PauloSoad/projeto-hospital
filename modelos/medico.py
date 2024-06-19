class Medico:
    def __init__(self, nome_Medico, especialidade_Medico, telefone_Medico, status_medico):
        self.nome_Medico = nome_Medico
        self.especialidade_Medico = especialidade_Medico
        self.telefone_Medico = telefone_Medico
        self.status_medico = status_medico

    def exibir_local_medico(self):
        if self.status_medico:
            print(f" 💚 O Médico {self.nome_Medico} se encontra no hospital.")

        elif self.status_medico:
            print(f" 💛 O Médico esta de férias {self.nome_Medico}")
        
        else:
            print(f" ❤️️ Alerta! O medico {self.nome_Medico} encontra-se ausente. Informe o medico de plantao para que ele alinhe com o titutar.")
        print(f"Telefone do medico: {self.telefone_Medico}")



        