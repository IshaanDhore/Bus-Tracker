# 🚌 Smart Bus Transport System

This project optimizes urban commuting through a real-time, interactive web application. It uses Dijkstra's Algorithm to calculate the shortest path between bus stops and integrates the OpenRouteService API to provide actual road network geometry, distance, and estimated travel times.

## 🚀 Features

* **Interactive Map:** Powered by Leaflet.js, featuring custom bus and stop icons.
* **Shortest Path Routing:** Uses Dijkstra's algorithm to find the most efficient route through a predefined graph of bus stops.
* **Real-Road Geometry:** Fetches precise driving coordinates and metadata (km/min) from the OpenRouteService API.
* **Live Bus Animation:** Simulates real-time bus movement along the calculated path.
* **Glassmorphism UI:** Features a modern, sleek interface with blur effects and responsive panels.
* **Flask Backend:** Serves route data and manages application logic via a Python API.

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (ES6)
* **Mapping:** Leaflet.js
* **Backend:** Flask (Python)
* **API:** OpenRouteService (Directions API)
* **Data Format:** JSON (for route and stop definitions)

## 📂 Project Structure

```bash
├── app.py             # Flask server & API endpoints
├── routes.json        # Logical bus route definitions (Node-Link)
├── templates/
│   └── index.html     # Main frontend application
└── static/            # (Optional) CSS/JS files if externalized
