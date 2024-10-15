## Analysis Bike Sharing 🚲

Proyek ini bertujuan untuk menganalisis pola penggunaan sepeda dari dataset Bike Sharing. 
Analisis dilakukan untuk memahami faktor-faktor yang mempengaruhi jumlah sewa sepeda seperti waktu, hari kerja vs akhir pekan, dan hari dalam seminggu. Proyek ini mencakup proses analisis data, eksplorasi data, serta visualisasi untuk mendapatkan insight lebih dalam.

## Project Structure
- `dashboard/`: Contains the Streamlit dashboard code (`dashboard.py`).
- `data/`: Includes the dataset files (`day.csv`, `hour.csv`).
- `venv/`: Virtual environment folder.
- `Analisis_Data.ipynb`: Jupyter Notebook for data analysis.
- `requirements.txt`: Python dependencies for the project.

## Setup Environment
### Using VSCode and Virtual Environment
1. Create a new project directory:
   ```bash
   mkdir Analysis-Bike-Sharing-Bangkit
   cd Analysis-Bike-Sharing-Bangkit
2. Set up a virtual environment
   ```bash
   python -m venv venv
3. Activate the virtual environment
   ```bash
   venv\Scripts\activate
4. Install the require dependencies
   ```bash
   pip install -r requirements.txt
5. Run Streamlit App
   ```bash
   cd dashboard
   streamlit run dashboard.py