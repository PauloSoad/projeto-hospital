from modelos.medico import Medico
from modelos.hospital import Hospital
from modelos.paciente import Paciente


# Instanciando a classe Medico 10 vezes com status vari�vel
medicos = [
    Medico("Dr. Carlos", "Cardiologia", "45656444", True),
    Medico("Dra. Ana", "Pediatria", "987654321", True),
    Medico("Dr. Maria", "Neurologia", "456789123", True),
    Medico("Dra. Joana", "Dermatologia", "321654987", True),
    Medico("Dr. Jose", "Ortopedia", "789123456", True),
    Medico("Dr. Pedro", "Oncologia", "654987321", True),
    Medico("Dra. Sofia", "Ginecologia", "147258369", True),
    Medico("Dr. Lucas", "Oftalmologia", "369258147", True),
    Medico("Dra. Beatriz", "Clínico Geral", "258369147", False),
    Medico("Dr. Guilherme", "Urologia", "159263478", False)
]

# Testando a fun��o exibir_local_medico para cada m�dico
for medico in medicos:
    medico.exibir_local_medico()

print("\n")



# Instanciando a classe Paciente 5 vezes com status vari�vel
pacientes = [
    Paciente("Joao", True, "Clinica Medica"),
    Paciente("Maria", True, "Pediatria"),
    Paciente("Carlos", False, "Ortopedia"),
    Paciente("Ana", True, "Cardiologia"),
    Paciente("Pedro", False, "Neurologia")
]

# Testando a fun��o exibir_status_paciente para cada paciente
for paciente in pacientes:
    paciente.exibir_status_paciente()

print("\n")


# Instanciando a classe Hospital 4 vezes com medico_no_hospital vari�vel
hospitais = [
    Hospital("Unimed", "Rua da unimed, 1", "6-6666-6666", True),
    Hospital("Ceam", "Rua do ceam, 2", "7-7777-7777", False),
    Hospital("Hospital Público", "Rua do hospital, 3", "8-8888-8888", True),
    Hospital("Hospital Vai na Fé", "Av. Esperança - São Paulo, 4", "9-9999-9999", False)
]

# Testando a fun��o exibir_status_medico_no_hospital para cada hospital
for hospital in hospitais:
    hospital.exibir_status_medico_no_hospital()