import tkinter as tk
from tkinter import ttk, messagebox

class Mahasiswa:
    def _init_(self, win):
        self.win = win
        self.win.title("Mahasiswa Sistem Informasi")
        self.win.geometry("600x600")
        self.win.configure(bg="#f0f0f0")

        self.kuliah = []

        self.detail_mahasiswa_frame = ttk. LabelFrame(self.win, text="Detail Mahasiswa",)
        self.detail_mahasiswa_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self. nama_label = ttk. Label(self.detail_mahasiswa_frame, text="Nama")
        self.nama_label.grid(row=0, column=0, padx=5, pady=5)

        self.nama_entry = ttk.Entry(self.detail_mahasiswa_frame, width=20)
        self.nama_entry.grid(row=0, column=1, padx=5, pady=5)

        self.no_hp_label = ttk. Label(self.detail_mahasiswa_frame, text="NPM")
        self.no_hp_label.grid(row=0, column=2, padx=5, pady=5)

        self.no_hp_entry = ttk.Entry(self.detail_mahasiswa_frame, width=20)
        self.no_hp_entry.grid(row=0, column=3, padx=5, pady=5)

        self.angkatan_label = ttk.Label(self.detail_mahasiswa_frame, text="Angkatan")
        self.angkatan_label.grid(row=0, column=4, padx=5, pady=5)

        self.angkatan_entry = ttk.Entry(self.detail_mahasiswa_frame, width=20)
        self.angkatan_entry.grid(row=0, column=5, padx=5, pady=5)

        self.matkul_frame = ttk.LabelFrame(self.win, text="Detail Mata Kuliah")
        self.matkul_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.mata_kuliah_label = ttk.Label(self.matkul_frame, text="Mata Kuliah")
        self.mata_kuliah_label.grid(row=0, column=0, padx=5, pady=5)

        self.mata_kuliah_entry = ttk.Entry(self.matkul_frame, width=20)
        self.mata_kuliah_entry.grid(row=0, column=1, padx=5, pady=5)

        self.dosen_label = ttk.Label(self.matkul_frame, text="Dosen")
        self.dosen_label.grid(row=0, column=2, padx=5, pady=5)

        self.dosen_entry = ttk.Entry(self.matkul_frame, width=20)
        self.dosen_entry.grid(row=0, column=3, padx=5, pady=5)

        self.nilai_label = ttk.Label(self.matkul_frame, text="Nilai")
        self.nilai_label.grid(row=0, column=4, padx=5, pady=5)

        self.nilai_entry = ttk.Entry(self.matkul_frame, width=20)
        self.nilai_entry.grid(row=0, column=5, padx=5, pady=5)

        self.button_frame = ttk.LabelFrame(self.win, text="Fungsi")
        self.button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.add_button = ttk.Button(self.button_frame, text="Add")
        self.add_button.grid(row=2, column=0, padx=10, pady=5)

        self.print_button = ttk.Button(self.button_frame, text="Print")
        self.print_button.grid(row=2, column=1, padx=10, pady=5)
        
        self.update_button = ttk.Button(self.button_frame, text="Update")
        self.update_button.grid(row=2, column=2, padx=10, pady=5)

        self.delete_button = ttk.Button(self.button_frame, text="Delete")
        self.delete_button.grid(row=2, column=3, padx=10, pady=5)

        self.perkuliahan_list = tk.Listbox(self.win, width=80, height=10)
        self.perkuliahan_list.grid(row=3, column=0, columnspan=4, padx=10, pady=10)
        self.perkuliahan_list.bind("<<listBoxSelect>>", self.on_perkuliahan_select)

        self.mahasiswa_frame = ttk.LabelFrame(self.win, text="Mahasiswa")
        self.mahasiswa_frame.gird(row=4, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.mahasiswa_text = tk.Text(self.mahasiswa_frame, width=60, height=15)
        self.mahasiswa_text.pack(fill="both", expand=True)

        self.print_button.config(command=self.print_mahasiswa)

    def print_mahasiswa(self):
        self.mahasiswa_text.delete(1.0, tk.END)
        ke = 1
        for perkuliahan in self.kuliah:
             mahasiswa_text = (
                f"--------- Mahasiswa ke-{ke} --------\n"
                f"Nama \t\t: {perkuliahan[ 'Nama']} \n"
                f"NPM \t\t: {perkuliahan['NPM']}\n"
                f"Angkatan \t\t: {perkuliahan[ 'Angkatan'] }\n"
                f"------ Mata Kuliah yang Diambil ------\n" 
                f"Mata Kuliah \t\t: {perkuliahan['Mata Kuliah']}\n"
                f"Dosen \t\t: {perkuliahan[ 'Dosen']}\n"
                f"Nilai \t\t: {perkuliahan['Nilai']}\n"
             )
        self.mahasiswa_text.insert(tk.END, mahasiswa_text + "\n\n")
        ke = ke+1

    
if __name__ == "_main_":
    win = tk.Tk()
    app = Mahasiswa(win)
    win.mainloop()