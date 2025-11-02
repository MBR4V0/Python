import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Classe Equipamento
class Equipamento:
    def __init__(self, nome, id_equip):
        self.nome = nome
        self.id_equip = id_equip
        self.disponivel = True
        self.reserva = None  # Armazena a reserva atual (se houver)

    def cadastrar(self, nome):
        self.nome = nome
        self.nome = {"equipamento": equipamento}

    def reservar(self, professor, data):
        if self.disponivel:
            self.disponivel = False
            self.reserva = {"professor": professor, "data": data}
            return True
        return False

    def liberar(self):
        self.disponivel = True
        self.reserva = None

    def __str__(self):
        status = "Disponível" if self.disponivel else f"Reservado por {self.reserva['professor']} em {self.reserva['data']}"
        return f"{self.nome} (ID: {self.id_equip}) - {status}"

# Classe Sistema de Reservas
class SistemaReservas:
    def __init__(self):
        self.equipamentos = []

    def cadastrar_equipamento(self, nome):
        for equip in self.equipamentos:
            if equip.nome == nome_equip:
                if equip.cadastrar(nome):
                   return "Equipamento cadastrado com sucesso!"

    def listar_equipamentos(self):
        return [str(equip) for equip in self.equipamentos]

    def fazer_reserva(self, id_equip, professor, data):
        for equip in self.equipamentos:
            if equip.id_equip == id_equip:
                if equip.reservar(professor, data):
                    return f"Reserva confirmada: {equip.nome} para {professor} em {data}"
                return "Equipamento indisponível!"
        return "Equipamento não encontrado!"

    def liberar_equipamento(self, id_equip):
        for equip in self.equipamentos:
            if equip.id_equip == id_equip and not equip.disponivel:
                equip.liberar()
                return f"Equipamento {equip.nome} liberado!"
        return "Equipamento não encontrado ou já disponível!"

# Interface Gráfica
class InterfaceReservas:
    def __init__(self, root, sistema):
        self.sistema = sistema
        self.root = root
        self.root.title("Sistema de Reserva de Equipamentos")

     # Labels e Entradas
        tk.Label(root, text="ID do Equipamento:").grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(root, text="Nome do Professor:").grid(row=1, column=0, padx=5, pady=5)
        self.professor_entry = tk.Entry(root)
        self.professor_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(root, text="Nome do Equipamento:").grid(row=2, column=0, padx=5, pady=5)
        self.equipamento_entry = tk.Entry(root)
        self.equipamento_entry.grid(row=2, column=1, padx=5, pady=5)

        # Botões
        tk.Button(root, text="Listar Equipamentos", command=self.listar).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(root, text="Reservar", command=self.reservar).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(root, text="Liberar", command=self.liberar).grid(row=4, column=0, padx=5, pady=5)
        tk.Button(root, text="Cadastrar", command=self.cadastrar).grid(row=4, column=1, padx=5, pady=5)
        
        # Área de texto para exibir resultados
        self.resultado = tk.Text(root, height=10, width=50)
        self.resultado.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def listar(self):
        self.resultado.delete(1.0, tk.END)
        for equip in self.sistema.listar_equipamentos():
            self.resultado.insert(tk.END, equip + "\n")

    def reservar(self):
        id_equip = self.id_entry.get()
        professor = self.professor_entry.get()
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        resultado = self.sistema.fazer_reserva(id_equip, professor, data)
        messagebox.showinfo("Resultado", resultado)
        self.listar()

    def liberar(self):
        id_equip = self.id_entry.get()
        resultado = self.sistema.liberar_equipamento(id_equip)
        messagebox.showinfo("Resultado", resultado)
        self.listar()

    def cadastrar(self):
        nome = self.equipamento_entry.get()
        resultado = self.sistema.cadastrar_equipamentos(nome)
        messagebox.showinfo("Resultado", resultado)
        self.listar()

# Inicialização do Sistema
if __name__ == "__main__":
    # Criar sistema e adicionar equipamentos iniciais
    sistema = SistemaReservas()
    
    # Criar interface gráfica
    root = tk.Tk()
    app = InterfaceReservas(root, sistema)
    root.mainloop()
