import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

def gerar_pdf(nome_arquivo):
    """
    Gera um arquivo PDF com o cronograma de estudos.
    """
    try:
        # Cria o objeto Canvas para desenhar no PDF
        c = canvas.Canvas(nome_arquivo, pagesize=A4)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(A4[0] / 2, A4[1] - 50, "Cronograma de Estudos – Comissária de Voo")
        c.setFont("Helvetica", 10)
        c.drawCentredString(A4[0] / 2, A4[1] - 70, "Nível Iniciante")

        styles = getSampleStyleSheet()
        style = styles['Normal']
        style.leading = 14 # Espaçamento entre linhas

        y_pos = A4[1] - 100

        cronograma = {
            "SEMANA 1 – CONHECIMENTOS BÁSICOS DE AVIAÇÃO": """
História da aviação no Brasil e no mundo
Partes da aeronave (fuselagem, asas, motores, trem de pouso etc.)
Órgãos reguladores: ANAC, ICAO, IATA
Tipos de voos: doméstico e internacional
Funções e responsabilidades do comissário(a)
Noções básicas de meteorologia

📝 Exercício:
Crie um glossário com 20 siglas ou termos técnicos da aviação.
""",
            "SEMANA 2 – REGULAMENTAÇÃO DA AVIAÇÃO CIVIL": """
Código Brasileiro de Aeronáutica (CBA)
RBAC 61 e 121 (Regulamentos da ANAC)
Documentos obrigatórios de voo (tripulação e aeronave)
Direitos e deveres dos tripulantes
Normas da ICAO (Organização da Aviação Civil Internacional)

📝 Exercício:
Monte um resumo com os principais direitos e deveres de um comissário.
""",
            "SEMANA 3 – SEGURANÇA DE VOO E EMERGÊNCIAS": """
Tipos de emergência (fogo, despressurização, pouso forçado, evacuação)
Equipamentos de segurança da aeronave (máscaras de oxigênio, extintores, escorregadores etc.)
Procedimentos de evacuação
Comunicação com a cabine
Checklist de segurança

📝 Exercício:
Simule (no papel) uma evacuação de emergência com os comandos que você daria aos passageiros.
""",
            "SEMANA 4 – PRIMEIROS SOCORROS E SOBREVIVÊNCIA": """
Noções de primeiros socorros (hemorragias, fraturas, parada cardíaca)
Atendimento a passageiros com doenças a bordo
Equipamentos médicos de bordo (kit de primeiros socorros, desfibrilador)
Técnicas de sobrevivência (selva, mar, montanha, deserto)

📝 Exercício:
Crie um “kit de sobrevivência” com itens essenciais para cada tipo de ambiente (mar, selva etc.)
"""
        }

        for semana, conteudo in cronograma.items():
            if y_pos < 100: # Se o espaço na página for insuficiente, cria uma nova página
                c.showPage()
                y_pos = A4[1] - 50

            # Título da semana
            c.setFont("Helvetica-Bold", 12)
            c.drawString(50, y_pos, f"✅ {semana}")
            y_pos -= 20

            # Conteúdo da semana
            c.setFont("Helvetica", 10)
            linhas = conteudo.strip().split('\n')
            for linha in linhas:
                p = Paragraph(linha.strip(), style)
                largura, altura = p.wrapOn(c, A4[0] - 100, 0)
                if y_pos < altura + 10:
                    c.showPage()
                    y_pos = A4[1] - 50
                p.drawOn(c, 50, y_pos - altura)
                y_pos -= (altura + 5)
            y_pos -= 10

        c.save()
        messagebox.showinfo("Sucesso", f"O cronograma de estudos foi gerado com sucesso!\n\nSalvo como:\n{os.path.abspath(nome_arquivo)}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o PDF: {e}")

def criar_janela():
    """
    Cria a janela principal da aplicação.
    """
    root = tk.Tk()
    root.title("Gerador de Cronograma")
    root.geometry("400x150")
    root.resizable(False, False)

    # Label com as instruções
    label = tk.Label(root, text="Clique no botão para gerar o cronograma em PDF.", wraplength=350, pady=10)
    label.pack()

    # Botão para gerar o PDF
    botao = tk.Button(root, text="Gerar PDF", command=lambda: gerar_pdf("cronograma_comissaria.pdf"))
    botao.pack(pady=10)

    # Inicia o loop da aplicação
    root.mainloop()

if __name__ == "__main__":
    criar_janela()
