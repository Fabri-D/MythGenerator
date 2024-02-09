import tkinter as tk
from tkinter import ttk
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Inicializar el modelo y el tokenizador de GPT-2 fine-tuneado
model_folder = "model"
model = GPT2LMHeadModel.from_pretrained(model_folder)
tokenizer = GPT2Tokenizer.from_pretrained(model_folder)


# Función para generar el mito
def generate_mito():
    # Obtener el texto del prompt
    prompt_text = prompt_entry.get()

    # Tokenizar el prompt
    input_ids = tokenizer.encode(prompt_text, return_tensors="pt")

    output = model.generate(
    input_ids=input_ids,
    max_length=1024,
    no_repeat_ngram_size=1,
    pad_token_id=tokenizer.eos_token_id,
    use_cache=True,
    )

    # Decodificar y mostrar el texto generado
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    generated_textbox.delete(1.0, tk.END)
    generated_textbox.insert(tk.END, generated_text)


# Crear la ventana principal
root = tk.Tk()
root.title("MythGenerator")
# Cambiar el color de fondo de la ventana principal
root.configure(bg="#192841")  # Fondo azul marino

# Configurar el tamaño de la ventana
window_width = root.winfo_screenwidth() * 0.7
window_height = root.winfo_screenheight() * 0.87
root.geometry(f"{int(window_width)}x{int(window_height)}")


# Crear el estilo para el marco principal
style = ttk.Style()
style.configure("Main.TFrame", background="#192841")

# Crear el marco principal con el estilo configurado
main_frame = ttk.Frame(root, style="Main.TFrame")
main_frame.pack(fill=tk.BOTH, expand=True)

# Estilo para los widgets
style = ttk.Style()
style.configure("TLabel", background="#192841", foreground="white")  # Estilo para las etiquetas
style.configure("TEntry", background="white")  # Estilo para la entrada de texto
style.configure("TButton", background="#1976D2", foreground="white")  # Estilo para el botón
style.configure("TText", background="white")  # Estilo para el cuadro de texto

# Etiqueta para el título
title_label = ttk.Label(main_frame, text="MythGenerator", font=("Bahnschrift Condensed", 22))
title_label.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

# Entry para ingresar el prompt
prompt_label = ttk.Label(main_frame, text="Prompt:", font=("Helvetica", 12))
prompt_label.grid(row=1, column=0, padx=(250,10) , pady=35, sticky="e")

prompt_entry = tk.Entry(main_frame, width=50, font=("Helvetica", 12))
prompt_entry.grid(row=1, column=1, padx=10, pady=35, columnspan=2, sticky="w")
prompt_entry.configure(background="#CCCCCC")  # Cambiar color de fondo

# Botón para generar el mito
generate_button = tk.Button(main_frame, text="Generate", command=generate_mito, width=15, font=("Agency FB", 16))
generate_button.grid(row=2, column=0, columnspan=4, padx=(100, 10), pady=7)
generate_button.configure(background="#CCCCCC")  # Cambiar color de fondo

# Textbox para mostrar el mito generado
generated_textbox = tk.Text(main_frame, wrap="word", width=83, height=25)
generated_textbox.grid(row=3, column=0, columnspan=2, padx=(100, 20), pady=5)
generated_textbox.configure(background="#CCCCCC")  # Cambiar color de fondo

# Label para indicar que el texto generado es ficticio
fictitious_label = ttk.Label(main_frame, text="* All the AI generates is fictitious.", font=("Helvetica", 10))
fictitious_label.grid(row=4, column=0, columnspan=2, padx=(100, 20), pady=5)
fictitious_label.configure(background="#192841", foreground="white")  # Cambiar color de fondo y color del texto


# Ejecutar el bucle principal de la aplicación
root.mainloop()
