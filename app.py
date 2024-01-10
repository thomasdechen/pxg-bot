# config_gui.py

import tkinter as tk
import os
import shutil
from tkinter import filedialog
import threading
import parasect
from time import time
from time import sleep
from parasect import start_bot
from parasect import start_bot
from bot_state import BotState

pxg_title = "PokeXGames"

FOOD1_POS = 529, 630
FOOD2_POS = 569, 632
POS_AMARELA = 1454, 363, 28, 8
POS1_BATTLE = 1407, 381, 21, 14
POS1_VIDA = 1458, 392, 10, 6

SAFE = False

VIDA_AMARELA = 'pokexgames/vida_amarela.png'
DEF_BATTLE = 'pokexgames/def_battle.png'
VIDA_1 = 'pokexgames/vida1.png'

# Config
FOOD_EAT = 'config/food_img.png'
MOB1 = 'config/first_name.png'
MOB_BATTLE = 'config/mob_battle_img.png'
MOB_HUNT = 'prints/parasect.PNG'
POKE1 = 'prints/poke_1.PNG'


class ConfigGUI:
    def __init__(self, master):
        self.bot_state = BotState()
        self.pause_event = threading.Event()
        self.master = master
        self.master.title("Configuração do Bot")

        self.config_name_label = tk.Label(self.master, text="Nome da Configuração:")
        self.config_name_label.pack()

        self.config_name_entry = tk.Entry(self.master, width=30)
        self.config_name_entry.insert(tk.END, "parasect_config")
        self.config_name_entry.pack()

        self.food_eat_label = tk.Label(self.master, text="Imagem para Comida:")
        self.food_eat_label.pack()

        self.food_eat_button = tk.Button(self.master, text="Selecionar Imagem", command=self.select_food_image)
        self.food_eat_button.pack()

        self.mob1_label = tk.Label(self.master, text="Imagem para MOB1:")
        self.mob1_label.pack()

        self.mob1_button = tk.Button(self.master, text="Selecionar Imagem", command=self.select_mob1_image)
        self.mob1_button.pack()

        self.mob_battle_label = tk.Label(self.master, text="Imagem para Batalha MOB:")
        self.mob_battle_label.pack()

        self.mob_battle_button = tk.Button(self.master, text="Selecionar Imagem", command=self.select_mob_battle_image)
        self.mob_battle_button.pack()

        self.load_config_button = tk.Button(self.master, text="Carregar Configuração", command=self.load_config)
        self.load_config_button.pack()

        self.save_config_button = tk.Button(self.master, text="Salvar Configuração", command=self.save_config)
        self.save_config_button.pack()

        self.pause_button = tk.Button(self.master, text="Pausar Bot", command=self.pause_bot)
        self.pause_button.pack()

        self.start_button = tk.Button(self.master, text="Iniciar Bot", command=self.start_bot)
        self.start_button.pack()

        # Configurações padrão
        self.food_eat_path = FOOD_EAT
        self.mob1_path = MOB1
        self.mob_battle_path = MOB_BATTLE

        # Variáveis para controle do estado do bot
        self.bot_paused = False
        self.last_pause_time = 0

    def select_food_image(self):
        file_path = filedialog.askopenfilename(title="Selecionar Imagem para Comida")
        if file_path:
            self.food_eat_path = file_path

    def select_mob1_image(self):
        file_path = filedialog.askopenfilename(title="Selecionar Imagem para MOB1")
        if file_path:
            self.mob1_path = file_path

    def select_mob_battle_image(self):
        file_path = filedialog.askopenfilename(title="Selecionar Imagem para Batalha MOB")
        if file_path:
            self.mob_battle_path = file_path

    def load_config(self):
        folder_path = filedialog.askdirectory(title="Selecionar Pasta de Configuração")
        if folder_path:
            # Adapte este método conforme necessário para carregar as configurações da pasta
            self.load_config_from_folder(folder_path)

    def save_config(self):
        folder_path = filedialog.askdirectory(title="Selecionar Pasta para Salvar Configuração")
        if folder_path:
            # Adapte este método conforme necessário para salvar as configurações na pasta
            self.save_config_to_folder(folder_path)


    def start_bot(self):
        self.pause_event.set()  # Libera o evento de pausa
        start_bot(self.bot_state, self.pause_event)

    def pause_bot(self):
        self.pause_event.clear()  # Define o evento de pausa
        self.bot_state.bot_paused = True

    global bot_paused
    bot_paused = False

    def load_config_from_file(self, file_path):
        # Implemente a lógica para carregar as configurações do arquivo aqui
        pass

    def load_config_from_folder(self, folder_path):
        # Implemente a lógica para carregar as configurações da pasta aqui
        pass

    def save_config_to_folder(self, folder_path):
        # Certifique-se de que o folder_path seja válido
        if not folder_path:
            return

        # Obtém o nome da pasta da Entry
        config_name = self.config_name_entry.get()

        # Certifique-se de que config_name não seja vazio
        if not config_name:
            return

        # Crie um diretório para as configurações
        config_folder_path = os.path.join(folder_path, config_name)
        os.makedirs(config_folder_path, exist_ok=True)

        # Salve as imagens e configurações no diretório
        shutil.copy("config/food_img.png", config_folder_path)
        shutil.copy("config/first_name.png", config_folder_path)
        shutil.copy("config/mob_battle_img.png", config_folder_path)
        shutil.copy("prints/parasect.PNG", config_folder_path) 
        shutil.copy("prints/poke_1.PNG", config_folder_path)

        # Salve as posições em um arquivo de texto
        positions_file_path = os.path.join(config_folder_path, "positions.txt")
        with open(positions_file_path, "w") as file:
            file.write("FOOD1_POS = 529, 630\n")
            file.write("FOOD2_POS = 569, 632\n")
            file.write("POS_AMARELA = 1454, 363, 28, 8\n")
            file.write("POS1_BATTLE = 1407, 381, 21, 14\n")
            file.write("POS1_VIDA = 1458, 392, 10, 6\n")

        print(f"Configuração salva em: {config_folder_path}")


if __name__ == "__main__":
    # Inicialização da GUI
    root = tk.Tk()
    config_gui = ConfigGUI(root)

    root.mainloop()
