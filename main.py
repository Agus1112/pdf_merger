import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from PyPDF2 import PdfMerger

# Class to merge PDF files.
class PDFMergerApp:
    def __init__(self, root):
        # Main window characterization.
        self.root = root
        self.root.title("Unir PDFs")
        self.root.resizable(False, False)
        self.root.iconbitmap("images/app_icon.ico")
        self.root.geometry("600x450")
        
        # Frame to contain the Listbox and Scrollbars.
        listbox_frame = tk.Frame(root)
        listbox_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Scrollbars.
        self.scroll_y = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
        self.scroll_x = tk.Scrollbar(listbox_frame, orient=tk.HORIZONTAL)
        
        # Listbox to show the PDF files.
        self.listbox = tk.Listbox(listbox_frame, selectmode=tk.SINGLE, width=90, height=15, font=("arial", 12), 
                                  yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)
        
        self.scroll_y.config(command=self.listbox.yview)
        self.scroll_x.config(command=self.listbox.xview)
        
        # Pack the widgets.
        self.scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Frame to place the buttons.
        frame = tk.Frame(root)
        frame.pack()
        
        # Load the images for the buttons.
        self.load_images()
        
        # Buttons characteristics. 
        btn_width = 120
        btn_height = 40
        
        self.btn_add = tk.Button(frame, image=self.img_add, text="  Agregar", font=("arial", 12), compound=tk.LEFT, command=self.add_pdfs, width=btn_width, height=btn_height)
        self.btn_add.grid(row=0, column=0, padx=5)
        
        self.btn_remove = tk.Button(frame, image=self.img_remove, text="  Eliminar", font=("arial", 12), compound=tk.LEFT, command=self.remove_pdf, width=btn_width, height=btn_height)
        self.btn_remove.grid(row=0, column=1, padx=5)
        
        self.btn_up = tk.Button(frame, image=self.img_up, text="  Subir", font=("arial", 12), compound=tk.LEFT, command=self.move_up, width=btn_width, height=btn_height)
        self.btn_up.grid(row=0, column=2, padx=5)
        
        self.btn_down = tk.Button(frame, image=self.img_down, text="  Bajar", font=("arial", 12), compound=tk.LEFT, command=self.move_down, width=btn_width, height=btn_height)
        self.btn_down.grid(row=0, column=3, padx=5)
        
        self.btn_merge = tk.Button(root, image=self.img_merge, text="  Unir PDFs", font=("arial", 12), compound=tk.LEFT, command=self.merge_pdfs, width=btn_width, height=btn_height)
        self.btn_merge.pack(pady=10)
        
        self.pdf_files = []

    def load_images(self):
        scale_factor = 0.5  # Reducir las imágenes al 50%
        
        self.img_add = ImageTk.PhotoImage(Image.open("images/add.png").resize((int(32 * scale_factor), int(32 * scale_factor))))
        self.img_remove = ImageTk.PhotoImage(Image.open("images/delete.png").resize((int(32 * scale_factor), int(32 * scale_factor))))
        self.img_up = ImageTk.PhotoImage(Image.open("images/up.png").resize((int(32 * scale_factor), int(32 * scale_factor))))
        self.img_down = ImageTk.PhotoImage(Image.open("images/down.png").resize((int(32 * scale_factor), int(32 * scale_factor))))
        self.img_merge = ImageTk.PhotoImage(Image.open("images/pdf_download.png").resize((int(32 * scale_factor), int(32 * scale_factor))))

    def add_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])
        if files:
            for file in files:
                if file not in self.pdf_files:
                    self.pdf_files.append(file)
                    self.listbox.insert(tk.END, file)
    
    def remove_pdf(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            del self.pdf_files[index]
            self.listbox.delete(index)
    
    def move_up(self):
        selected = self.listbox.curselection()
        if selected and selected[0] > 0:
            index = selected[0]
            self.pdf_files[index], self.pdf_files[index - 1] = self.pdf_files[index - 1], self.pdf_files[index]
            self.listbox.delete(index)
            self.listbox.insert(index - 1, self.pdf_files[index - 1])
            self.listbox.selection_set(index - 1)
    
    def move_down(self):
        selected = self.listbox.curselection()
        if selected and selected[0] < len(self.pdf_files) - 1:
            index = selected[0]
            self.pdf_files[index], self.pdf_files[index + 1] = self.pdf_files[index + 1], self.pdf_files[index]
            self.listbox.delete(index)
            self.listbox.insert(index + 1, self.pdf_files[index + 1])
            self.listbox.selection_set(index + 1)
    
    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("Error", "No hay archivos PDF seleccionados")
            return
        
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])
        if not output_file:
            return
        
        merger = PdfMerger()
        for pdf in self.pdf_files:
            merger.append(pdf)
        
        merger.write(output_file)
        merger.close()
        
        messagebox.showinfo("Éxito", f"PDFs unidos en: {output_file}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()