class Hospital:
    def __init__(self, nome_Hospital, endereco_Hospital, telefone_Hospital, medico_no_hospital):
        self.nome_Hospital = nome_Hospital
        self.endereco_Hospital = endereco_Hospital
        self.telefone_Hospital = telefone_Hospital
        self.medico_no_hospital = medico_no_hospital

    def __str__(self) -> str:
        pass

    def exibir_status_medico_no_hospital(self):
        if self.medico_no_hospital:
            print(f"✅O medico esta no hospital!")
        else:
            print(f"❎O medico encontra-se AUSENTE do hospital. Contate-o.")




        #if paciente_hospital.status_medico_no_hospital == "crítico":
       # print("Estado: Em estado crítico. Requer atenção imediata.")
   # elif paciente.estado == "alerta":
       # print("Estado: Em estado de alerta. Monitoramento necessário.")
    #elif paciente.estado == "alta":
        #print("Estado: Em estado de alta. Estável.")
        #else:
        # print("") 
            
