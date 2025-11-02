import tkinter as tk
from tkinter import messagebox, ttk

# Lista para armazenar os equipamentos
equipamentos = []

# Função para cadastrar um novo equipamento
def cadastrar_equipamento():
    nome = entry_nome.get()
    if not nome:
        messagebox.showwarning("Aviso", "Digite o nome do equipamento!")
        return

    equipamento = {
        "id": len(equipamentos) + 1,
        "nome": nome,
        "disponivel": True,
        "reservado_por": "",
        "data_reserva": ""
    }
    equipamentos.append(equipamento)
    entry_nome.delete(0, tk.END)
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Equipamento cadastrado com sucesso!")

# Função para listar os equipamentos na Treeview
def atualizar_lista():
    for item in tree.get_children():
        tree.delete(item)
    for equip in equipamentos:
        status = "Disponível" if equip["disponivel"] else "Reservado"
        detalhes = f"{equip['reservado_por']} - {equip['data_reserva']}" if not equip["disponivel"] else ""
        tree.insert("", tk.END, values=(equip["id"], equip["nome"], status, detalhes))

# Função para reservar um equipamento
def reservar_equipamento():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Aviso", "Selecione um equipamento!")
        return

    item = tree.item(selected[0])
    id_equip = int(item["values"][0])
    equipamento = next(equip for equip in equipamentos if equip["id"] == id_equip)

    if not equipamento["disponivel"]:
        messagebox.showwarning("Aviso", "Equipamento já está reservado!")
        return

    janela_reserva = tk.Toplevel(root)
    janela_reserva.title("Reservar Equipamento")
    janela_reserva.geometry("300x200")

    tk.Label(janela_reserva, text="Nome do professor:").pack(pady=5)
    entry_prof = tk.Entry(janela_reserva)
    entry_prof.pack(pady=5)

    tk.Label(janela_reserva, text="Data (DD/MM/AAAA):").pack(pady=5)
    entry_data = tk.Entry(janela_reserva)
    entry_data.pack(pady=5)

    def confirmar_reserva():
        prof = entry_prof.get()
        data = entry_data.get()
        if not prof or not data:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return

        equipamento["disponivel"] = False
        equipamento["reservado_por"] = prof
        equipamento["data_reserva"] = data
        atualizar_lista()
        janela_reserva.destroy()
        messagebox.showinfo("Sucesso", "Reserva realizada com sucesso!")

    tk.Button(janela_reserva, text="Confirmar", command=confirmar_reserva).pack(pady=10)

# Função para liberar um equipamento
def liberar_equipamento():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Aviso", "Selecione um equipamento!")
        return

    item = tree.item(selected[0])
    id_equip = int(item["values"][0])
    equipamento = next(equip for equip in equipamentos if equip["id"] == id_equip)

    if equipamento["disponivel"]:
        messagebox.showwarning("Aviso", "Equipamento já está disponível!")
        return

    equipamento["disponivel"] = True
    equipamento["reservado_por"] = ""
    equipamento["data_reserva"] = ""
    atualizar_lista()
    messagebox.showinfo("Sucesso", "Equipamento liberado com sucesso!")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Reserva de Equipamentos")
root.geometry("600x400")

# Frame para cadastro
frame_cadastro = tk.Frame(root)
frame_cadastro.pack(pady=10)

tk.Label(frame_cadastro, text="Nome do Equipamento:").pack(side=tk.LEFT, padx=5)
entry_nome = tk.Entry(frame_cadastro, width=30)
entry_nome.pack(side=tk.LEFT, padx=5)
tk.Button(frame_cadastro, text="Cadastrar", command=cadastrar_equipamento).pack(side=tk.LEFT, padx=5)

# Frame para botões de ação
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

tk.Button(frame_botoes, text="Reservar", command=reservar_equipamento).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Liberar", command=liberar_equipamento).pack(side=tk.LEFT, padx=5)

# Treeview para listar equipamentos
tree = ttk.Treeview(root, columns=("ID", "Nome", "Status", "Detalhes"), show="headings", height=15)
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Status", text="Status")
tree.heading("Detalhes", text="Detalhes da Reserva")
tree.column("ID", width=50)
tree.column("Nome", width=200)
tree.column("Status", width=100)
tree.column("Detalhes", width=200)

    root = tk.Tk()
    app = InterfaceReservas(root, sistema)
    root.mainloop()
