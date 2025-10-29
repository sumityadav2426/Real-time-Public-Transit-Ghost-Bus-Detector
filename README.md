# Nagpur Project (Final)

This package is a Nagpur-localized version of your original project. All coordinates and map defaults
are set to Nagpur (Sitabuldi / Civil Lines area).

## How to run (Windows)

### Backend
1. Open PowerShell or CMD and navigate to the project backend folder:
   ```powershell
   cd backend
   ```
2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies and run the ingest simulation and main app (adjust filenames if needed):
   ```powershell
   pip install -r requirements.txt
   python app\ingest_sim.py
   python app\main.py
   ```

### Frontend
1. Open a new terminal and go to the frontend folder:
   ```powershell
   cd frontend
   ```
2. Install and start the frontend:
   ```powershell
   npm install
   npm start
   ```

The frontend should open on http://localhost:3001 (or the port your setup uses). The project outputs will appear in the project folder,
and the provided simulated video is `output_nagpur.mp4` and frames are in `output_frames/`.

## Notes
- The included `output_nagpur.mp4` is the video you uploaded (renamed) if available, and `output_frames/` contains simulated frames for preview.
- For true live map tiles and exact replication of running the project, run the backend/frontend locally as described above.
