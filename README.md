## 📦 Bank Telegram Bot

* **Language:** Python 3.8
* **Frameworks & Libraries:** Flask, Flask-SocketIO, MongoDB
* **Key Directories:**

  * `common_utils`: Utility functions and shared resources.
  * `models`: Database models and schemas.
  * `modules`: Modular components handling specific functionalities.
  * `project_pay2world`: Core logic pertaining to the Pay2World project.
  * `static` & `templates`: Front-end assets and HTML templates.
  * `views`: Route handlers and view functions.
* **Entry Points:**

  * `create_app.py`: Application factory for initializing the Flask app.
  * `app_pay2w.py`: Main application script.
  * `manage.py`: Script for managing application tasks.
* **Configuration Files:**

  * `requirements.txt`: List of Python dependencies.
  * `.gitignore`: Specifies files and directories to be ignored by Git.

---

## 🚀 Features

* **Telegram Bot Integration:** Handles user interactions via Telegram.
* **Web Interface:** Provides a web-based interface for administrative tasks or user interactions.
* **Real-time Communication:** Utilizes Socket.IO for real-time updates and notifications.
* **Database Management:** Employs MongoDB for storing and retrieving data.
* **Modular Architecture:** Structured in a way that promotes scalability and maintainability.([GitHub][1])

---

## 🛠️ Setup & Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/aimaster-dev/p2w_bk_telegram_bot.git
   cd p2w_bk_telegram_bot
   ```



2. **Create a Virtual Environment:**

   ```bash
   python3.8 -m venv venv
   source venv/bin/activate
   ```



3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```



4. **Configure Environment Variables:**
   Set up necessary environment variables for Flask, MongoDB, and Telegram API tokens.

5. **Initialize the Database:**
   Ensure MongoDB is running and accessible.

6. **Run the Application:**

   ```bash
   python manage.py run
   ```



---

## 📄 License

This project is licensed under the MIT License.

---
