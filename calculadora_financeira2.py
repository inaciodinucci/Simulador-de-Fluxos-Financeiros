import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from modulos.anuidade import calcular_anuidade
from modulos.perpetuidade import calcular_perpetuidade
from modulos.amortizacao import calcular_amortizacao

class CalculadoraFinanceira:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Financeira")
        self.root.geometry("400x400")

        # Variáveis
        self.tipo_calculo = tk.StringVar()
        self.tipo_anuidade = tk.StringVar()
        
        # Frame principal
        self.frame_principal = ttk.Frame(root, padding="10")
        self.frame_principal.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Seleção do tipo de cálculo
        ttk.Label(self.frame_principal, text="Selecione o tipo de cálculo:").grid(row=0, column=0, pady=5)
        self.combo_tipo = ttk.Combobox(self.frame_principal, textvariable=self.tipo_calculo)
        self.combo_tipo['values'] = ('Anuidade', 'Perpetuidade', 'Amortização')
        self.combo_tipo.grid(row=0, column=1, pady=5)
        self.combo_tipo.bind('<<ComboboxSelected>>', self.atualizar_campos)

        # Frame para campos de entrada
        self.frame_campos = ttk.Frame(self.frame_principal)
        self.frame_campos.grid(row=1, column=0, columnspan=2, pady=10)

        # Frame para resultados
        self.frame_resultados = ttk.Frame(self.frame_principal)
        self.frame_resultados.grid(row=2, column=0, columnspan=2, pady=10)

        # Inicialização dos campos
        self.criar_campos_anuidade()
        self.campos_anuidade.grid_remove()
        self.criar_campos_perpetuidade()
        self.campos_perpetuidade.grid_remove()
        self.criar_campos_amortizacao()
        self.campos_amortizacao.grid_remove()

    def criar_campos_anuidade(self):
        self.campos_anuidade = ttk.Frame(self.frame_campos)
        self.campos_anuidade.grid(row=0, column=0)

        # Tipo de anuidade
        ttk.Label(self.campos_anuidade, text="Tipo de Anuidade:").grid(row=0, column=0, pady=5)
        self.radio_ordinaria = ttk.Radiobutton(self.campos_anuidade, text="Ordinária", variable=self.tipo_anuidade, value="ordinaria")
        self.radio_ordinaria.grid(row=0, column=1)
        self.radio_vencida = ttk.Radiobutton(self.campos_anuidade, text="Vencida", variable=self.tipo_anuidade, value="vencida")
        self.radio_vencida.grid(row=0, column=2)
        self.tipo_anuidade.set("ordinaria")

        # Campos de entrada
        ttk.Label(self.campos_anuidade, text="PMT (Pagamento):").grid(row=1, column=0, pady=5)
        self.pmt_anuidade = ttk.Entry(self.campos_anuidade)
        self.pmt_anuidade.grid(row=1, column=1, columnspan=2)

        ttk.Label(self.campos_anuidade, text="Taxa de Juros (%):").grid(row=2, column=0, pady=5)
        self.taxa_anuidade = ttk.Entry(self.campos_anuidade)
        self.taxa_anuidade.grid(row=2, column=1, columnspan=2)

        ttk.Label(self.campos_anuidade, text="Número de Períodos:").grid(row=3, column=0, pady=5)
        self.periodos_anuidade = ttk.Entry(self.campos_anuidade)
        self.periodos_anuidade.grid(row=3, column=1, columnspan=2)

        ttk.Button(self.campos_anuidade, text="Calcular", command=self.calcular_anuidade).grid(row=4, column=0, columnspan=3, pady=10)

    def criar_campos_perpetuidade(self):
        self.campos_perpetuidade = ttk.Frame(self.frame_campos)
        self.campos_perpetuidade.grid(row=0, column=0)

        ttk.Label(self.campos_perpetuidade, text="PMT (Pagamento):").grid(row=0, column=0, pady=5)
        self.pmt_perpetuidade = ttk.Entry(self.campos_perpetuidade)
        self.pmt_perpetuidade.grid(row=0, column=1)

        ttk.Label(self.campos_perpetuidade, text="Taxa de Juros (%):").grid(row=1, column=0, pady=5)
        self.taxa_perpetuidade = ttk.Entry(self.campos_perpetuidade)
        self.taxa_perpetuidade.grid(row=1, column=1)

        ttk.Button(self.campos_perpetuidade, text="Calcular", command=self.calcular_perpetuidade).grid(row=2, column=0, columnspan=2, pady=10)

    def criar_campos_amortizacao(self):
        self.campos_amortizacao = ttk.Frame(self.frame_campos)
        self.campos_amortizacao.grid(row=0, column=0)

        ttk.Label(self.campos_amortizacao, text="Valor do Empréstimo:").grid(row=0, column=0, pady=5)
        self.valor_emprestimo = ttk.Entry(self.campos_amortizacao)
        self.valor_emprestimo.grid(row=0, column=1)

        ttk.Label(self.campos_amortizacao, text="Taxa de Juros (%):").grid(row=1, column=0, pady=5)
        self.taxa_amortizacao = ttk.Entry(self.campos_amortizacao)
        self.taxa_amortizacao.grid(row=1, column=1)

        ttk.Label(self.campos_amortizacao, text="Número de Períodos:").grid(row=2, column=0, pady=5)
        self.periodos_amortizacao = ttk.Entry(self.campos_amortizacao)
        self.periodos_amortizacao.grid(row=2, column=1)

        ttk.Label(self.campos_amortizacao, text="Valor da Parcela:").grid(row=3, column=0, pady=5)
        self.parcela_amortizacao = ttk.Entry(self.campos_amortizacao)
        self.parcela_amortizacao.grid(row=3, column=1)

        ttk.Button(self.campos_amortizacao, text="Calcular", command=self.calcular_amortizacao).grid(row=4, column=0, columnspan=2, pady=10)

    def atualizar_campos(self, event=None):
        # Esconder todos os campos
        self.campos_anuidade.grid_remove()
        self.campos_perpetuidade.grid_remove()
        self.campos_amortizacao.grid_remove()

        # Mostrar campos relevantes
        if self.tipo_calculo.get() == 'Anuidade':
            self.campos_anuidade.grid()
        elif self.tipo_calculo.get() == 'Perpetuidade':
            self.campos_perpetuidade.grid()
        elif self.tipo_calculo.get() == 'Amortização':
            self.campos_amortizacao.grid()

    def calcular_anuidade(self):
        try:
            pmt = float(self.pmt_anuidade.get())
            taxa = float(self.taxa_anuidade.get()) / 100
            periodos = int(self.periodos_anuidade.get())
            tipo = self.tipo_anuidade.get()

            resultado = calcular_anuidade(pmt, taxa, periodos, tipo)
            self.mostrar_resultado(f"Valor Presente da Anuidade: R$ {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def calcular_perpetuidade(self):
        try:
            pmt = float(self.pmt_perpetuidade.get())
            taxa = float(self.taxa_perpetuidade.get()) / 100

            resultado = calcular_perpetuidade(pmt, taxa)
            self.mostrar_resultado(f"Valor Presente da Perpetuidade: R$ {resultado:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def calcular_amortizacao(self):
        try:
            valor = float(self.valor_emprestimo.get())
            taxa = float(self.taxa_amortizacao.get()) / 100
            periodos = int(self.periodos_amortizacao.get())
            parcela = float(self.parcela_amortizacao.get())

            tabela = calcular_amortizacao(valor, taxa, periodos, parcela)
            self.mostrar_tabela_amortizacao(tabela)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos.")

    def mostrar_resultado(self, texto):
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()
        ttk.Label(self.frame_resultados, text=texto).grid(row=0, column=0)

    def mostrar_tabela_amortizacao(self, tabela):
        # Limpar resultados anteriores
        for widget in self.frame_resultados.winfo_children():
            widget.destroy()

        # Criar tabela
        tree = ttk.Treeview(self.frame_resultados, columns=('Período', 'Prestação', 'Juros', 'Amortização', 'Saldo'), show='headings')
        
        # Definir cabeçalhos
        tree.heading('Período', text='Período')
        tree.heading('Prestação', text='Prestação')
        tree.heading('Juros', text='Juros')
        tree.heading('Amortização', text='Amortização')
        tree.heading('Saldo', text='Saldo')

        # Configurar colunas
        for col in ('Período', 'Prestação', 'Juros', 'Amortização', 'Saldo'):
            tree.column(col, width=100)

        # Inserir dados
        for linha in tabela:
            tree.insert('', 'end', values=linha)

        # Adicionar scrollbar
        scrollbar = ttk.Scrollbar(self.frame_resultados, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Posicionar elementos
        tree.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')

if __name__ == '__main__':
    root = tk.Tk()
    app = CalculadoraFinanceira(root)
    root.mainloop()