# 📝 Flask Task Manager

A lightweight, multi-user Task Manager website built with Python (Flask) and Vanilla JavaScript. It features user authentication, real-time UI updates, and a persistent Dark Mode theme.

**Live Demo:** https://sf-task-manager.vercel.app/

## ✨ Features

* **Multi-User Support:** Users can register and log in to manage their own private list of tasks.
* **Dark Mode:** A toggle switch that saves your preference (Light/Dark) using LocalStorage.
* **Responsive Design:** specific CSS styling for a clean, modern card-based layout.
* **Instant Interaction:** Uses JavaScript (Fetch API) for adding/deleting tasks without refreshing the page.
* **Cloud Ready:** optimized for serverless deployment on Vercel.

## 🛠 Tech Stack

* **Backend:** Python 3, Flask
* **Frontend:** HTML5, CSS3 (Variables & Flexbox), Vanilla JavaScript
* **Database:** In-Memory Python Lists (optimized for Vercel stateless environment)

## 🚀 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/task-manager.git](https://github.com/your-username/task-manager.git)
    cd task-manager
    ```

2.  **Install Requirements**
    You need Python installed. Then run:
    ```bash
    pip install flask
    ```

3.  **Start the App**
    ```bash
    python app.py
    ```

4.  **Open in Browser**
    Visit `http://127.0.0.1:5000` to see the app running.

## ☁️ Deployment (Vercel)

This project is configured for easy deployment on [Vercel](https://vercel.com).

1.  Push your code to a GitHub repository.
2.  Import the repository in Vercel.
3.  Vercel will detect `app.py` and `vercel.json` and deploy automatically.

**⚠️ Important Note:** This version uses **In-Memory Storage** to comply with Vercel's read-only file system. 
* **Consequence:** All users and tasks are deleted if the server restarts or "sleeps" after inactivity.
* **Fix:** For permanent data, connect the app to a remote database like PostgreSQL or MongoDB Atlas.

## 📜 Changelog

All notable changes to this project will be documented in this section.

### [v0.4.0] - 2025-12-29
**Deployed & Patched**
* **Refactor:** Switched database from SQLite to In-Memory Python dictionaries to support Vercel's stateless environment.
* **Fix:** Resolved `SyntaxError` regarding global variable declarations (`tasks_db`) in `app.py`.
* **Docs:** Added `vercel.json` and `requirements.txt` for cloud build configuration.

### [v0.3.0] - 2025-12-29
**Theming Update**
* **Feature:** Added Dark Mode toggle switch.
* **Tech:** Implemented CSS Variables (`:root`) for instant theme switching.
* **UX:** Added `localStorage` logic to remember user theme preference on refresh.

### [v0.2.0] - 2025-12-29
**UI Overhaul**
* **Style:** Added `static/style.css` with a card-based layout.
* **UI:** Added flexbox positioning, button styles (Primary/Secondary/Delete), and basic responsive padding.

### [v0.1.0] - 2025-12-29
**Initial Release**
* **Core:** Basic Flask server set up with `app.py`.
* **Auth:** User registration and login functionality (hashing passwords).
* **DB:** SQLite integration (later removed in v1.0.0).
* **Frontend:** Basic HTML structure with Fetch API integration.