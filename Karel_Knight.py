import tkinter as tk
from PIL import Image, ImageTk, ImageSequence 
import random
import os
from Enemies import generar_objetos, ObjetoJuego
import tkinter.messagebox as msgbox
from Questions import obtener_pregunta_aleatoria

TILE_SIZE = 140
TILE_SPACING = 20  
VISIBLE_TILES = 10
TOTAL_TILES = 100

class KarelKnightGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Karel Knight")
        self.root.geometry("1200x700")

        self.ventanas_secundarias = []

        self.canvas = tk.Canvas(root, width=1200, height=500, bg="lightblue")
        self.canvas.pack()

        self.status_label = tk.Label(root, text="Roll the dices, discover your luck.", font=("Arial", 18))
        self.status_label.pack(pady=10)

        self.roll_button = tk.Button(root, text="Go!", command=self.play_dice_animation, font=("Arial", 20))
        self.roll_button.pack()

        # Cargar imágenes
        self.tile_img = ImageTk.PhotoImage(Image.open("Assets/tile.png").resize((TILE_SIZE, TILE_SIZE)))
        self.karel_img = ImageTk.PhotoImage(Image.open("Assets/karel.png").resize((TILE_SIZE - 5, TILE_SIZE - 1)))
        self.background_img = ImageTk.PhotoImage(Image.open("Assets/background.png").resize((1200, 500)))
        self.dark_background_img = ImageTk.PhotoImage(Image.open("Assets/dark_background.png").resize((1200, 500)))
        self.darker_background_img = ImageTk.PhotoImage(Image.open("Assets/darker_background.png").resize((1200, 500)))
        self.compilador_img = ImageTk.PhotoImage(Image.open("Assets/Friend_compiler.png").resize((TILE_SIZE, TILE_SIZE)))
        self.bug_img = ImageTk.PhotoImage(Image.open("Assets/Betrayer_bug.png").resize((TILE_SIZE, TILE_SIZE)))
        self.enemigo_img = ImageTk.PhotoImage(Image.open("Assets/Enemy.png").resize((TILE_SIZE, TILE_SIZE)))
        self.enemigo_derrotado_img = ImageTk.PhotoImage(Image.open("Assets/enemy_defeated.png").resize((TILE_SIZE, TILE_SIZE)))

        self.background_id = None  

        # Animación del dado
        self.dice_gif = Image.open("Assets/rolling_dices.gif")
        self.dice_frames = [ImageTk.PhotoImage(frame.copy().resize((200, 200))) for frame in ImageSequence.Iterator(self.dice_gif)]
        self.dice_frame_index = 0
        self.dice_sprite = None

        self.karel_pos = 0
        self.visible_margin_ahead = 5
        self.offset = max(0, min(self.karel_pos - (VISIBLE_TILES - self.visible_margin_ahead), TOTAL_TILES - VISIBLE_TILES))
        
        self.tile_ids = []
        self.karel_sprite = None
        
        self.root.withdraw()
        self.mostrar_intro()
        self.mostrar_instrucciones()
    


        self.objetos_juego = generar_objetos()

        self.health_points = 10  # Vida inicial del jugador
        self.health_images = []  # Lista de corazones

        # Cargar imagen de corazones
        self.heart_img = ImageTk.PhotoImage(Image.open("Assets/heart.png").resize((30, 30)))


        self.draw_tiles()
        self.draw_karel()

    def draw_tiles(self):
        self.tile_ids.clear()
        self.canvas.delete("all")

        if self.karel_pos >= 66:
            bg = self.darker_background_img
        elif self.karel_pos >= 33:
            bg = self.dark_background_img
        else:
            bg = self.background_img

        self.background_id = self.canvas.create_image(0, 0, image=bg, anchor='nw')


        # Dibujar corazones en fila
        self.draw_health_bar()

        for i in range(VISIBLE_TILES):
            tile_index = self.offset + i
            if tile_index >= TOTAL_TILES:
                break
            x = i * (TILE_SIZE + TILE_SPACING)
            y = 400
            tile = self.canvas.create_image(x, y, image=self.tile_img, anchor='nw')
            self.canvas.create_text(x + TILE_SIZE//2, y + TILE_SIZE//2, text=str(tile_index + 1), font=("Arial", 12), fill="white")
            self.tile_ids.append(tile)

            for obj in self.objetos_juego:
                if obj.posicion == tile_index and obj.activo:
                    object_y = y - 120
                    if obj.tipo == "compilador":
                        self.canvas.create_image(x, object_y, image=self.compilador_img, anchor='sw')
                    elif obj.tipo == "bug":
                        self.canvas.create_image(x, object_y, image=self.bug_img, anchor='sw')
                    elif obj.tipo == "enemigo":
                        self.canvas.create_image(x, object_y, image=self.enemigo_img, anchor='nw')
                    elif obj.tipo == "enemigo_derrotado":
                        self.canvas.create_image(x, object_y, image=self.enemigo_derrotado_img, anchor='nw')    

    
    #Draws Karel in the canva according to relative possition
    def draw_karel(self): 
        if self.karel_sprite:
            self.canvas.delete(self.karel_sprite)

        relative_index = self.karel_pos - self.offset
        if 0 <= relative_index < VISIBLE_TILES:
            x = relative_index * (TILE_SIZE + TILE_SPACING) + 5
            tile_y = 400
            karel_height = self.karel_img.height()
            y = tile_y + (TILE_SIZE - karel_height * 1.5)
            self.karel_sprite = self.canvas.create_image(x, y, image=self.karel_img, anchor='nw')

    def draw_health_bar(self):
        for img in self.health_images:
            self.canvas.delete(img)  # Eliminar corazones anteriores
    
        self.health_images = []  # Vaciar lista

        posicion_inicial_x = 20  # Ajusta este valor según necesites
        posicion_y = 10

        for i in range(self.health_points):
            img = self.canvas.create_image(posicion_inicial_x + (i * 35), posicion_y, image=self.heart_img, anchor='nw')
            self.health_images.append(img)

    def reducir_vida(self):
        if self.health_points > 0:
            self.health_points -= 1
            self.draw_health_bar()  # Redibujar corazones
            self.status_label.config(text="Oh no, you have been attacked! You lost 1 HP.")

            if self.health_points == 0:
                self.game_over()       

    def game_over(self):
        self.status_label.config(text="Game Over! Karel has fallen.")
        self.roll_button.config(state="disabled")  # Bloquear el juego             
       

    def update_offset(self):
         self.offset = max(0, min(self.karel_pos - 1, TOTAL_TILES - VISIBLE_TILES))

    def roll_dice(self):
        steps = random.randint(2, 12)
        self.show_personalized_roll(steps)

    #Plays the gif of rolling the dices
    def play_dice_animation(self):
        self.status_label.config(text="Rolling dices...")
        self.dice_frame_index = 0
        self.animate_dice()

    def animate_dice(self):
        if self.dice_sprite:
            self.canvas.delete(self.dice_sprite)

        frame = self.dice_frames[self.dice_frame_index]
        canvas_center_x = self.canvas.winfo_width() // 2 - 75
        canvas_center_y = self.canvas.winfo_height() // 2 - 75
        self.dice_sprite = self.canvas.create_image(canvas_center_x, canvas_center_y, image=frame, anchor='nw')

        self.dice_frame_index += 1
        if self.dice_frame_index < len(self.dice_frames):
            self.root.after(100, self.animate_dice)
        else:
            self.canvas.delete(self.dice_sprite)
            self.root.after(300, self.roll_dice)

    def show_personalized_roll(self, steps):
        popup = tk.Toplevel(self.root)
        popup.title("Your Dice Roll")
        popup.configure(bg="#f8fdff")

        width, height = 300, 200
        root_x = self.root.winfo_x()
        root_y = self.root.winfo_y()
        root_width = self.root.winfo_width()
        root_height = self.root.winfo_height()
        x = root_x + (root_width // 2) - (width // 2)
        y = root_y + (root_height // 2) - (height // 2)
        popup.geometry(f"{width}x{height}+{x}+{y}")

        label = tk.Label(popup, text=f"You rolled a {steps}!", font=("Arial", 22, "bold"), bg="#f8fdff", fg="black")
        label.pack(pady=30)

        def continuar():
            popup.destroy()
            proposed_pos = self.karel_pos + steps

            if proposed_pos >= TOTAL_TILES: 
                self.karel_pos = TOTAL_TILES - 1
                self.update_offset()
                self.draw_tiles()
                self.draw_karel()
                self.status_label.config(text=f"You advanced {steps} steps and you have finally saved princess Lovelace from the castle! 🏰")
                self.roll_button.config(state="disabled")

                finalizar_popup = tk.Toplevel(self.root)
                finalizar_popup.title("Congratulations!")
                finalizar_popup.configure(bg="#1f5a8e")

               # Dimensiones y posición centrada
                width, height = 1200, 800
                x = (self.root.winfo_screenwidth() // 2) - (width // 2)
                y = (self.root.winfo_screenheight() // 2) - (height // 2)
                finalizar_popup.geometry(f"{width}x{height}+{x}+{y}")
   
                # Cargar imagen de finalización
                final_img = ImageTk.PhotoImage(Image.open("Assets/the_end.png").resize((1200, 800)))
                label_img = tk.Label(finalizar_popup, image=final_img)
                label_img.image = final_img  # Evita que la imagen se elimine por el recolector de basura
                label_img.pack()

                 # Cerrar la ventana después de unos segundos
                self.root.after(5000, finalizar_popup.destroy)
  

            else:
                self.karel_pos = proposed_pos
                self.update_offset()
                self.draw_tiles()
                self.draw_karel()
                self.status_label.config(text=f"You move forward {steps} steps.")
                self.verify_current_pos()

        close_button = tk.Button(popup, text="Continue", font=("Arial", 14), command=continuar)
        close_button.pack(pady=10)
        
        popup.transient(self.root)
        popup.grab_set()
        self.root.wait_window(popup)

     
    def verify_current_pos(self):
        print(f"Verificando casilla: {self.karel_pos}")
    
        while True:  # Bucle para efectos encadenados
            efecto_aplicado = False
        
            for obj in self.objetos_juego:
                if obj.posicion == self.karel_pos and obj.activo:
                    print(f"Objeto activado: {obj.tipo}")
                    obj.activo = False  # Lo marcamos como ya visitado
                
                    if obj.tipo == "enemigo":
                        self.mostrar_alerta_imagen("Assets/alert_enemy1.png")
                        pregunta = obtener_pregunta_aleatoria()
                        self.mostrar_pregunta(pregunta, self.resultado_pregunta_enemigo)

                    elif obj.tipo == "bug":
                        self.mostrar_alerta_imagen("Assets/alert_bug1.png")
                        self.root.after(4000, lambda: self.aplicar_efecto_bug())
                        efecto_aplicado = True  # Señalamos que hubo movimiento

                    elif obj.tipo == "compilador":
                        self.mostrar_alerta_imagen("Assets/alert_compiler1.png")
                        self.root.after(4000, lambda: self.aplicar_efecto_compilador())
                        efecto_aplicado = True  # Señalamos que hubo movimiento
                
                    break  # Solo activamos un efecto por vez
        
                # Si se aplicó un efecto, verificamos la nueva posición
            if efecto_aplicado:
                print(f"Nuevo estado de Karel: {self.karel_pos}")
            else:
                break  # Si ya no hay efectos, terminamos el bucle   

    def aplicar_efecto_bug(self):
        self.karel_pos = max(0, self.karel_pos - 3)
        self.update_offset()
        self.draw_tiles()
        self.draw_karel()
        self.status_label.config(text="The bug made you step back 3 tiles!")

    def aplicar_efecto_compilador(self):
        self.karel_pos = min(TOTAL_TILES - 1, self.karel_pos + 3)
        self.update_offset()
        self.draw_tiles()
        self.draw_karel()
        self.status_label.config(text="The compiler pushed you forward 3 tiles!")

    
    def mostrar_alerta_imagen(self, path):
        top = tk.Toplevel(self.root)
        top.title("Alert")
        top.overrideredirect(True)

        img = ImageTk.PhotoImage(Image.open(path).resize((450, 450)))
        panel = tk.Label(top, image=img)
        panel.image = img
        panel.pack()
        self.root.after(4000, top.destroy)

          # Calcular dimensiones de la ventana emergente
        ancho_ventana = 450
        alto_ventana = 450

    # Obtener el tamaño de la pantalla
        ancho_pantalla = top.winfo_screenwidth()
        alto_pantalla = top.winfo_screenheight()

    # Calcular posición centrada
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Aplicar geometría para centrar
        top.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    # Cerrar la ventana después de 4 segundos
        self.root.after(4000, top.destroy)

    def mostrar_pregunta(self, data, callback):
        popup = tk.Toplevel(self.root)
        popup.title("Programming Challenge")
        popup.configure(bg="#f8fdff")
       
        popup.protocol("WM_DELETE_WINDOW", lambda: None)


        # Obtener el tamaño de la pantalla
        ancho_pantalla = self.root.winfo_screenwidth()
        alto_pantalla = self.root.winfo_screenheight()

        # Dimensiones de la ventana emergente
        ancho_ventana = 400  # Ajusta según tu diseño
        alto_ventana = 400

        # Calcular la posición centrada
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

    # Aplicar la posición centrada
        popup.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


        label = tk.Label(popup, text=data["pregunta"], font=("Arial", 18, "bold"), bg="#77a7bf", fg="black", wraplength=350)
        label.pack(pady=15)

        respuesta_var = tk.StringVar()
        respuesta_var.set(None)  # Inicialmente sin selección

        for opcion in data["opciones"]:
            rb = tk.Radiobutton(popup, text=opcion, variable=respuesta_var, value=opcion, font=("Arial", 14), bg="#f8fdff")
            rb.pack(anchor="w", padx=20)

        
        def verificar_respuesta():
            seleccion = respuesta_var.get()
            popup.destroy()

            respuesta_correcta = seleccion == data["respuesta_correcta"]

         # Llama al método que maneja lo que pasa con el enemigo
            self.resultado_pregunta_enemigo(respuesta_correcta)

         # Botón para enviar la respuesta
        boton_continuar = tk.Button(popup, text="Continue", font=("Arial", 14), command=verificar_respuesta)
        boton_continuar.pack(pady=10)

# Muestra la ventana emergente en modo modal
        popup.transient(self.root)
        popup.grab_set()
        self.root.wait_window(popup)

    

    def resultado_pregunta_enemigo(self, correcta):
        if correcta:
            path = "Assets/karel_attack.png"  # Imagen de Karel atacando
            self.status_label.config(text="You defeated the enemy! You may roll again.")

            # Primero desactiva al enemigo original
            for obj in self.objetos_juego:
                if obj.tipo == "enemigo" and obj.posicion == self.karel_pos:
                    obj.activo = False  

            #Luego crea el objeto enemigo derrotado correctamente
            enemy_defeated = ObjetoJuego(tipo="enemigo_derrotado", posicion=self.karel_pos)
            enemy_defeated.activo = True  
            self.objetos_juego.append(enemy_defeated)

            self.draw_tiles()

            self.draw_karel()
                
        else:
            path = "Assets/enemy_attack.png"  # Imagen del enemigo atacando
            self.reducir_vida()  # Quitar un corazón

    # Redimensionar la imagen
        img = Image.open(path).resize((170, 170))
        self.attack_img = ImageTk.PhotoImage(img)

    # Calcular posición relativa de Karel
        relative_index = self.karel_pos - self.offset
        x = relative_index * (TILE_SIZE + TILE_SPACING) + TILE_SIZE // 2
        y = 300  # Ajusta según la altura de Karel

    # Mostrar imagen sobre Karel
        self.attack_img_id = self.canvas.create_image(x, y, image=self.attack_img, anchor='center')

    # Eliminar imagen después de 2 segundos
        self.root.after(2000, lambda: self.canvas.delete(self.attack_img_id))


    def mostrar_intro(self):
        ventana_intro = tk.Toplevel(self.root)
        ventana_intro.geometry("1200x700")
        ventana_intro.title("Bienvenido")
        ventana_intro.overrideredirect(True)

        img = Image.open("Assets/intro_image.png").resize((800, 600))  # Ajusta al tamaño de la ventana
        img_tk = ImageTk.PhotoImage(img)

        fondo = tk.Label(ventana_intro, image=img_tk)
        fondo.image = img_tk
        fondo.place(relx=0.5, rely=0.5, anchor="center")  # Centra la imagen

        btn = tk.Button(ventana_intro, text="Continue", font=("Arial", 16),
        command=lambda: [ventana_intro.destroy(), self.mostrar_instrucciones()])
        btn.place(relx=0.5, rely=0.9, anchor="center")

    def mostrar_instrucciones(self):
        ventana_instrucciones = tk.Toplevel(self.root)
        ventana_instrucciones.geometry("1200x700")
        ventana_instrucciones.title("Instructions")
        ventana_instrucciones.overrideredirect(True)

        img = Image.open("Assets/instrucciones.png").resize((800, 600))
        img_tk = ImageTk.PhotoImage(img)

        fondo = tk.Label(ventana_instrucciones, image=img_tk)
        fondo.image = img_tk
        fondo.pack()

        self.ventanas_secundarias.append(ventana_instrucciones)

        btn = tk.Button(ventana_instrucciones, text="Start Game", font=("Arial", 16),
        command=lambda: [ventana_instrucciones.destroy(), self.root.after(100, self.cerrar_todo_e_iniciar_juego)])
        btn.place(relx=0.5, rely=0.9, anchor="center")

    def iniciar_juego(self):
        self.root.deiconify()  # Muestra la ventana principal
        self.draw_tiles()
        self.draw_karel()
 

    def cerrar_todo_e_iniciar_juego(self): # Cierra todas las ventanas secundarias registradas
        
        for ventana in self.ventanas_secundarias:
            ventana.destroy()
        self.ventanas_secundarias.clear()  # Limpia la lista

        self.iniciar_juego()  # Inicia el juego correctamente
  

# Lanzar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    game = KarelKnightGame(root)
    root.mainloop()