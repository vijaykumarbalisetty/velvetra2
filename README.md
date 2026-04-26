# VELVETRA – Where Fabric Meets Artistry

## 📌 Overview

VELVETRA is a full-stack web application designed to help fashion designers create, manage, and visualize textile and clothing designs. It combines creativity with technology by integrating project management features and AI-based design concepts.

This project currently represents a **prototype (glimpse/trailer)** of the full Velvetra platform, with core functionalities implemented and advanced features planned for future development.


## 🎯 Features

* 🎨 Design Studio
  Upload patterns and explore design concepts.

* 📂 Project Management
  Manage and organize all design projects in one place.

* 🤖 AI Design Generation
  Generate fabric design ideas based on text descriptions.

* 👤 Admin Control
  Currently managed by admin (designer details & projects).

* 📊 Designer Tracking
  Tracks number of designers visiting the platform.



## 🛠️ Tech Stack

### Frontend

* React (with Vite)
* HTML, CSS, JavaScript

### Backend

* Django
* Django REST Framework

### Database

* SQLite (db.sqlite3)



## 🏗️ Project Structure

* **Frontend:** React + Vite (main project folder)
* **Backend:** Django project (`velvetra1`)
* **App:** `velvetra2` (handles designers & design projects)
* **Database:** SQLite


## 🔄 How It Works (Data Flow)

1. User opens the application in browser
2. React loads the UI
3. User performs an action (form submit, upload, etc.)
4. React sends API request to Django
5. Django processes request using ViewSets
6. Serializers validate and convert data
7. Models store data in SQLite
8. Django sends JSON response
9. React updates UI dynamically


## ⚙️ Key Django Components

* **Models:** Define database structure
* **Serializers:** Convert data (Python ↔ JSON)
* **ViewSets:** Handle CRUD operations
* **Routers:** Generate API endpoints


## 📁 Media & Static Files

* Static files (CSS, JS) are generated from React build
* Media files (images) are stored in `/media/` folder


## 🚧 Current Status

This project is a **prototype version** of Velvetra.
It demonstrates:

* Basic project management
* Admin control system
* Initial AI design concept integration


## 🔮 Future Scope

* Full AI-based fabric design generation
* User login system (designers & customers)
* Cloth customization services
* Advanced design tools
* Real-time designer interaction


## 💡 Conclusion

VELVETRA aims to bridge the gap between fashion and technology by providing a platform where designers can innovate, manage, and visualize their ideas efficiently.


## 👨‍💻 Author

Vijay Kumar
