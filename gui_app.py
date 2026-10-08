import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk

class CloudAtlasInsightGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Cloud Atlas Insight')
        self.geometry('1200x800')
        self.configure(bg='#2E3440')

        self.create_widgets()

    def create_widgets(self):
        # Top Panel
        top_panel = ctk.CTkFrame(self, fg_color='#3B4252', height=100)
        top_panel.pack(fill='x', padx=10, pady=10)

        self.service_status = ctk.CTkLabel(top_panel, text='Service Status: Online', text_color='#A3BE8C', font=('Arial', 16))
        self.service_status.pack(side='left', padx=20, pady=20)

        self.anomaly_alert = ctk.CTkLabel(top_panel, text='No Anomalies Detected', text_color='#BF616A', font=('Arial', 16))
        self.anomaly_alert.pack(side='right', padx=20, pady=20)

        # Main Content
        main_content = ctk.CTkFrame(self, fg_color='#4C566A')
        main_content.pack(fill='both', expand=True, padx=10, pady=10)

        # Topology Map
        topology_map_frame = ctk.CTkFrame(main_content, fg_color='#434C5E')
        topology_map_frame.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        topology_label = ctk.CTkLabel(topology_map_frame, text='Topology Map', text_color='#ECEFF4', font=('Arial', 14))
        topology_label.pack(pady=10)

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([0, 1, 2, 3], [0, 1, 0, 1], marker='o', color='#88C0D0')
        ax.set_facecolor('#434C5E')
        fig.patch.set_facecolor('#434C5E')
        ax.tick_params(colors='#ECEFF4')

        canvas = FigureCanvasTkAgg(fig, master=topology_map_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        # Performance Charts
        performance_frame = ctk.CTkFrame(main_content, fg_color='#434C5E')
        performance_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)

        performance_label = ctk.CTkLabel(performance_frame, text='Performance Charts', text_color='#ECEFF4', font=('Arial', 14))
        performance_label.pack(pady=10)

        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.bar(['CPU', 'Memory', 'Network'], [75, 60, 85], color='#81A1C1')
        ax2.set_facecolor('#434C5E')
        fig2.patch.set_facecolor('#434C5E')
        ax2.tick_params(colors='#ECEFF4')

        canvas2 = FigureCanvasTkAgg(fig2, master=performance_frame)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill='both', expand=True)

        # Bottom Panel
        bottom_panel = ctk.CTkFrame(self, fg_color='#3B4252', height=100)
        bottom_panel.pack(fill='x', padx=10, pady=10)

        self.cost_analytics = ctk.CTkLabel(bottom_panel, text='Cost Analytics: $1500.00', text_color='#ECEFF4', font=('Arial', 16))
        self.cost_analytics.pack(side='left', padx=20, pady=20)

        refresh_button = ctk.CTkButton(bottom_panel, text='Refresh Data', fg_color='#81A1C1', hover_color='#5E81AC')
        refresh_button.pack(side='right', padx=20, pady=20)

if __name__ == '__main__':
    app = CloudAtlasInsightGUI()
    app.mainloop()