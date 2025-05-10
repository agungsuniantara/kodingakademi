import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import json
import os
import numpy as np

class NutritionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Nutrisi")
        self.root.geometry("1000x750")

        # Variabel untuk asupan kalori mingguan
        self.calorie_data = {}
        
        # Load calorie history data if available
        self.data_file = "calorie_data.json"
        self.load_calorie_data()
        
        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Tab 1: Pelacak Makronutrien
        self.tab_macronutrients = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_macronutrients, text="Pelacak Makronutrien")
        
        # Tab 2: Asupan Kalori Harian
        self.tab_calories = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_calories, text="Asupan Kalori Harian")
        
        # Setup the tabs
        self.setup_macronutrients_tab()
        self.setup_calories_tab()
        
        # Footer
        self.footer_label = tk.Label(self.root, 
                                   text=f"©️ {datetime.now().year} Aplikasi Nutrisi - v2.0",
                                   font=('Helvetica', 8),
                                   fg='gray')
        self.footer_label.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

    def setup_macronutrients_tab(self):
        # Main container for macronutrients tab
        self.macro_frame = tk.Frame(self.tab_macronutrients, padx=20, pady=20)
        self.macro_frame.pack(expand=True, fill=tk.BOTH)
        
        # Configure grid weights
        self.macro_frame.grid_columnconfigure(0, weight=1)
        self.macro_frame.grid_columnconfigure(1, weight=1)
        
        # Title
        self.macro_title = tk.Label(self.macro_frame, 
                                 text="PELACAK MAKRONUTRIEN",
                                 font=('Helvetica', 18, 'bold'),
                                 fg='#2c3e50')
        self.macro_title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='ew')
        
        # Input frame
        self.macro_input_frame = tk.LabelFrame(self.macro_frame, 
                                             text="Input Makronutrien",
                                             padx=15,
                                             pady=15,
                                             font=('Helvetica', 10, 'bold'))
        self.macro_input_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        
        # Input fields
        tk.Label(self.macro_input_frame, text="Karbohidrat (g):", anchor='w').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.carbs_entry = ttk.Entry(self.macro_input_frame, width=15)
        self.carbs_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(self.macro_input_frame, text="Protein (g):", anchor='w').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.protein_entry = ttk.Entry(self.macro_input_frame, width=15)
        self.protein_entry.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(self.macro_input_frame, text="Lemak (g):", anchor='w').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.fat_entry = ttk.Entry(self.macro_input_frame, width=15)
        self.fat_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        # Calculate button
        self.calculate_macro_button = ttk.Button(self.macro_input_frame, 
                                               text="Hitung Makronutrien", 
                                               command=self.calculate_macros)
        self.calculate_macro_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky='ew')
        
        # Chart frame
        self.macro_chart_frame = tk.LabelFrame(self.macro_frame, 
                                             text="Visualisasi Makronutrien",
                                             padx=15,
                                             pady=15,
                                             font=('Helvetica', 10, 'bold'))
        self.macro_chart_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        
        # Figure for pie chart
        self.macro_figure = Figure(figsize=(5, 4), dpi=100)
        self.macro_plot = self.macro_figure.add_subplot(111)
        self.macro_canvas = FigureCanvasTkAgg(self.macro_figure, self.macro_chart_frame)
        self.macro_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Initial pie chart (empty)
        self.macro_plot.pie([1], labels=['Input data'], colors=['#f5f5f5'])
        self.macro_plot.set_title('Distribusi Makronutrien')
        self.macro_canvas.draw()
        
        # Results frame
        self.macro_result_frame = tk.LabelFrame(self.macro_frame, 
                                              text="Hasil Analisis Makronutrien",
                                              padx=15,
                                              pady=15,
                                              font=('Helvetica', 10, 'bold'))
        self.macro_result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
        
        # Results label
        self.macro_result_label = tk.Label(self.macro_result_frame, 
                                         text="Masukkan data makronutrien untuk melihat analisis", 
                                         font=('Helvetica', 12),
                                         anchor='w')
        self.macro_result_label.pack(fill=tk.X, pady=5)
        
        self.macro_detail_label = tk.Label(self.macro_result_frame, 
                                         text="", 
                                         font=('Helvetica', 12),
                                         anchor='w')
        self.macro_detail_label.pack(fill=tk.X, pady=5)

    def setup_calories_tab(self):
        # Main container for calories tab
        self.calories_frame = tk.Frame(self.tab_calories, padx=20, pady=20)
        self.calories_frame.pack(expand=True, fill=tk.BOTH)
        
        # Configure grid weights
        self.calories_frame.grid_columnconfigure(0, weight=1)
        self.calories_frame.grid_columnconfigure(1, weight=1)
        
        # Title
        self.calories_title = tk.Label(self.calories_frame, 
                                    text="PENGECEK ASUPAN KALORI HARIAN",
                                    font=('Helvetica', 18, 'bold'),
                                    fg='#2c3e50')
        self.calories_title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='ew')
        
        # Input frame
        self.calories_input_frame = tk.LabelFrame(self.calories_frame, 
                                               text="Input Asupan Kalori",
                                               padx=15,
                                               pady=15,
                                               font=('Helvetica', 10, 'bold'))
        self.calories_input_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        
        # Input fields
        tk.Label(self.calories_input_frame, text="Usia:", anchor='w').grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.calories_age_entry = ttk.Entry(self.calories_input_frame, width=15)
        self.calories_age_entry.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.calories_age_entry.insert(0, "30")  # Default value
        
        tk.Label(self.calories_input_frame, text="Jenis Kelamin:", anchor='w').grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.calories_gender_var = tk.StringVar(value='Pria')
        self.calories_gender_combo = ttk.Combobox(self.calories_input_frame, textvariable=self.calories_gender_var, width=15, state="readonly")
        self.calories_gender_combo['values'] = ('Pria', 'Wanita')
        self.calories_gender_combo.grid(row=1, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(self.calories_input_frame, text="Tingkat Aktivitas:", anchor='w').grid(row=2, column=0, padx=5, pady=5, sticky='w')
        self.calories_activity_var = tk.StringVar(value='Sedang')
        self.calories_activity_combo = ttk.Combobox(self.calories_input_frame, textvariable=self.calories_activity_var, width=15, state="readonly")
        self.calories_activity_combo['values'] = ('Sedentary', 'Ringan', 'Sedang', 'Aktif', 'Sangat Aktif')
        self.calories_activity_combo.grid(row=2, column=1, padx=5, pady=5, sticky='w')
        
        tk.Label(self.calories_input_frame, text="Kalori Hari Ini:", anchor='w').grid(row=3, column=0, padx=5, pady=5, sticky='w')
        self.today_calories_entry = ttk.Entry(self.calories_input_frame, width=15)
        self.today_calories_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')
        self.today_calories_entry.insert(0, "2500")  # Default value
        
        # Calculate button
        self.calculate_calories_button = ttk.Button(self.calories_input_frame, 
                                                 text="Periksa Asupan Kalori", 
                                                 command=self.check_calories)
        self.calculate_calories_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky='ew')
        
        # Chart frame
        self.calories_chart_frame = tk.LabelFrame(self.calories_frame, 
                                               text="Visualisasi Asupan Kalori Mingguan",
                                               padx=15,
                                               pady=15,
                                               font=('Helvetica', 10, 'bold'))
        self.calories_chart_frame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
        
        # Figure for bar chart
        self.calories_figure = Figure(figsize=(5, 4), dpi=100)
        self.calories_plot = self.calories_figure.add_subplot(111)
        self.calories_canvas = FigureCanvasTkAgg(self.calories_figure, self.calories_chart_frame)
        self.calories_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Results frame
        self.calories_result_frame = tk.LabelFrame(self.calories_frame, 
                                                text="Hasil Analisis Kalori",
                                                padx=15,
                                                pady=15,
                                                font=('Helvetica', 10, 'bold'))
        self.calories_result_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
        
        # Results label
        self.calories_result_label = tk.Label(self.calories_result_frame, 
                                           text="Masukkan data untuk melihat analisis kalori", 
                                           font=('Helvetica', 12),
                                           anchor='w')
        self.calories_result_label.pack(fill=tk.X, pady=5)
        
        self.calories_detail_label = tk.Label(self.calories_result_frame, 
                                           text="", 
                                           font=('Helvetica', 12),
                                           anchor='w')
        self.calories_detail_label.pack(fill=tk.X, pady=5)
        
        # Initial bar chart
        self.update_bar_chart()
        
    def calculate_macros(self):
        """Calculate and display macronutrients distribution"""
        try:
            # Get input values
            carbs = float(self.carbs_entry.get())
            protein = float(self.protein_entry.get())
            fat = float(self.fat_entry.get())
            
            # Convert to calories
            carbs_cal = carbs * 4  # 4 calories per gram of carbs
            protein_cal = protein * 4  # 4 calories per gram of protein
            fat_cal = fat * 9  # 9 calories per gram of fat
            
            total_cal = carbs_cal + protein_cal + fat_cal
            
            # Calculate percentages
            carbs_pct = (carbs_cal / total_cal) * 100
            protein_pct = (protein_cal / total_cal) * 100
            fat_pct = (fat_cal / total_cal) * 100
            
            # Update pie chart
            self.macro_plot.clear()
            values = [carbs_pct, protein_pct, fat_pct]
            labels = [f'Karbohidrat\n({carbs_pct:.1f}%)', 
                      f'Protein\n({protein_pct:.1f}%)', 
                      f'Lemak\n({fat_pct:.1f}%)']
            colors = ['#ff9999', '#66b3ff', '#99ff99']
            explode = (0.05, 0.05, 0.05)
            
            self.macro_plot.pie(values, labels=labels, autopct='%1.1f%%', 
                             startangle=90, explode=explode, colors=colors, shadow=True)
            self.macro_plot.set_title('Distribusi Makronutrien')
            self.macro_figure.tight_layout()
            self.macro_canvas.draw()
            
            # Check if balanced according to recommended values
            # Recommended: 50% carbs, 20% protein, 30% fat
            carbs_diff = abs(carbs_pct - 50)
            protein_diff = abs(protein_pct - 20)
            fat_diff = abs(fat_pct - 30)
            
            avg_diff = (carbs_diff + protein_diff + fat_diff) / 3
            
            if avg_diff <= 5:
                status = "sangat dekat dengan"
            elif avg_diff <= 10:
                status = "mendekati"
            elif avg_diff <= 15:
                status = "sedikit berbeda dari"
            else:
                status = "jauh berbeda dari"
            
            message = f"Keseimbangan makronutrien Anda {status} asupan yang direkomendasikan."
            details = f"Rincian Anda: {carbs_pct:.0f}% Karbohidrat, {protein_pct:.0f}% Protein, {fat_pct:.0f}% Lemak."
            recommendation = f"Rekomendasi: 50% Karbohidrat, 20% Protein, 30% Lemak."
            
            # Update result labels
            self.macro_result_label.config(text=message)
            self.macro_detail_label.config(text=f"{details}\n{recommendation}")
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai numerik yang valid.")
    
    def load_calorie_data(self):
        """Load calorie history data from file"""
        # Default data
        today = datetime.now()
        for i in range(7):
            date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
            self.calorie_data[date] = 0
        
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    
                    # Ensure we have data for past 7 days
                    for i in range(7):
                        date = (today - timedelta(days=i)).strftime("%Y-%m-%d")
                        if date not in data:
                            data[date] = 0
                    
                    # Only keep the last 7 days
                    keys_to_keep = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
                    self.calorie_data = {k: data[k] for k in keys_to_keep if k in data}
                    
                    # Load user profile if it exists
                    if 'user_profile' in data:
                        self.user_profile = data['user_profile']
                    else:
                        self.user_profile = {}
            except Exception as e:
                print(f"Error loading data: {e}")
                self.user_profile = {}
        else:
            self.user_profile = {}
    
    def save_calorie_data(self):
        """Save calorie history data to file"""
        data = {
            **self.calorie_data,
            'user_profile': self.user_profile
        }
        try:
            with open(self.data_file, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving data: {e}")
            messagebox.showerror("Error", f"Gagal menyimpan data: {e}")
    
    def check_calories(self):
        """Check daily caloric intake"""
        try:
            # Get input values
            age = int(self.calories_age_entry.get())
            gender = self.calories_gender_var.get()
            activity = self.calories_activity_var.get().lower()
            today_calories = float(self.today_calories_entry.get())
            
            # Default weight and height based on gender (following the second program)
            if gender.lower() == 'pria':
                weight = 70  # kg
                height = 170  # cm
            else:  # wanita
                weight = 60  # kg
                height = 160  # cm
            
            # Save to user profile
            self.user_profile = {
                'age': age,
                'gender': gender,
                'activity': activity
            }
            
            # Calculate BMR using Mifflin-St Jeor Equation (as in the second program)
            if gender.lower() == 'pria':
                s = 5
                bmr = (10 * weight) + (6.25 * height) - (5 * age) + s
            else:  # wanita
                s = -161
                bmr = (10 * weight) + (6.25 * height) - (5 * age) + s
            
            # Activity multiplier
            activity_factors = {
                'sedentary': 1.2,
                'ringan': 1.375,
                'sedang': 1.55,
                'aktif': 1.725,
                'sangat aktif': 1.9
            }
            
            # Calculate recommended daily calories
            rec_calories = bmr * activity_factors.get(activity, 1.2)
            
            # Set range (±10% of recommended)
            min_calories = rec_calories * 0.9
            max_calories = rec_calories * 1.1
            
            # Save today's calories
            today = datetime.now().strftime("%Y-%m-%d")
            self.calorie_data[today] = today_calories
            
            # Save data to file
            self.save_calorie_data()
            
            # Update bar chart
            self.update_bar_chart()
            
            # Determine status message
            if today_calories < min_calories:
                status = f"rendah (kurang dari rentang yang direkomendasikan {min_calories:.0f}-{max_calories:.0f} kkal)"
            elif today_calories > max_calories:
                status = f"tinggi (di atas rentang yang direkomendasikan {min_calories:.0f}-{max_calories:.0f} kkal)"
            else:
                status = f"normal (dalam rentang yang direkomendasikan {min_calories:.0f}-{max_calories:.0f} kkal)"
            
            # Update result labels
            message = f"Asupan kalori Anda ({today_calories:.0f} kkal) {status} untuk profil Anda."
            self.calories_result_label.config(text=message)
            
            details = f"Rekomendasi kalori harian berdasarkan: {age} tahun, {gender}, aktivitas {activity}."
            self.calories_detail_label.config(text=details)
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan nilai numerik yang valid.")
    
    def update_bar_chart(self):
        """Update the bar chart with the latest calorie data"""
        self.calories_plot.clear()
        
        # Get last 7 days as day names with dates
        today = datetime.now()
        dates = [(today - timedelta(days=i)) for i in range(6, -1, -1)]
        x_labels = [d.strftime("%d/%m") for d in dates]
        date_keys = [d.strftime("%Y-%m-%d") for d in dates]
        
        # Get calorie values
        calories = [self.calorie_data.get(date, 0) for date in date_keys]
        
        # Plot with color based on calorie range
        x = np.arange(len(x_labels))
        bars = self.calories_plot.bar(x, calories, width=0.6, color="#3498db")
        
        # Add value labels above bars
        for i, bar in enumerate(bars):
            height = bar.get_height()
            if height > 0:
                self.calories_plot.text(bar.get_x() + bar.get_width()/2., height + 50,
                                      f"{height:.0f}", ha='center', va='bottom')
        
        # Set y-axis limit
        max_calorie = max(calories) if max(calories) > 0 else 3000
        self.calories_plot.set_ylim(0, max_calorie * 1.2)
        
        # Set x-axis labels
        self.calories_plot.set_xticks(x)
        self.calories_plot.set_xticklabels(x_labels)
        
        # Add labels and title
        self.calories_plot.set_xlabel("Tanggal")
        self.calories_plot.set_ylabel("Kalori")
        self.calories_plot.set_title('Asupan Kalori 7 Hari Terakhir')
        self.calories_figure.tight_layout()
        self.calories_canvas.draw()
    
    def on_closing(self):
        # Save data before closing
        self.save_calorie_data()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NutritionApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()