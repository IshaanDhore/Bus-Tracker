🚌 Smart Bus Transport System
A real-time, interactive web application designed to optimize urban commuting. This project uses Dijkstra's Algorithm to calculate the shortest path between bus stops and integrates the OpenRouteService API to provide actual road-network geometry, distance, and estimated travel times.

🚀 Features
Interactive Map: Powered by Leaflet.js, featuring custom bus and stop icons.

Shortest Path Routing: Uses Dijkstra's algorithm to find the most efficient route through a predefined graph of bus stops.

Real-Road Geometry: Fetches precise driving coordinates and metadata (km/min) from the OpenRouteService API.

Live Bus Animation: Simulates real-time bus movement along the calculated path.

Glassmorphism UI: A modern, sleek interface with blur effects and responsive panels.

Flask Backend: A Python-based API to serve route data and manage application logic.

🛠️ Tech Stack
Frontend: HTML5, CSS3 (Glassmorphism), JavaScript (ES6)

Mapping: Leaflet.js

Backend: Flask (Python)

API: OpenRouteService (Directions API)

Data Format: JSON (for route and stop definitions)

📂 Project Structure
Bash
├── app.py              # Flask server & API endpoints
├── routes.json         # Logical bus route definitions (Node-Link)
├── templates/
│   └── index.html      # Main frontend application
└── static/             # (Optional) CSS/JS files if externalized
⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/your-username/smart-bus-system.git
cd smart-bus-system
Install dependencies:

Bash
pip install flask
API Configuration:
The project uses an OpenRouteService API key. While a key is included in index.html for demonstration, it is recommended to sign up for your own key and replace the API_KEY constant in the script section.

Run the application:

Bash
python app.py
Access the app:
Open your browser and navigate to http://127.0.0.1:5000.

🚦 How to Use
Select Start/End: Click anywhere on the map to select your starting point. Click a second time to select your destination.

Automatic Snap: The system automatically snaps your clicks to the nearest physical bus stop.

View Route: The shortest path will be highlighted in neon green, and a route card will appear in the left panel showing the stop sequence, total distance (km), and travel time (min).

Simulate: Watch the bus icons travel along the road network in real-time.

Reset: Click a third time anywhere on the map to reset the selection.

🧮 Logic Behind the System
Dijkstra's Algorithm
The system builds a weighted graph where:

Nodes: Bus stops (lat/lng coordinates).

Edges: Existing bus routes connecting the stops.

Weights: The Euclidean distance between connected stops.

API Integration
Once the logical path is found (e.g., Stop A → Stop B → Stop C), the app sends a POST request to OpenRouteService to get the actual road coordinates, ensuring the path follows streets rather than drawing straight lines.
