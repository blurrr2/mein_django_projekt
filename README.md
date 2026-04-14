markdown
# Sally – Personal Blog

A clean, elegant personal blog documenting my journey from China to Germany.  
Sharing my experiences learning German, exploring German culture & life, and growing as a developer.

**Live Site**: [https://sallymomo.pythonanywhere.com](https://sallymomo.pythonanywhere.com)

---

## ✨ Features

- **Modern & Clean Design** with excellent readability
- **Three main sections**:
  - Deutschland verstehen (German life & culture)
  - Deutsch lernen (German learning journey & B2 exam prep)
  - Coding Journey (programming tutorials and experiences)
- Built with **Wagtail CMS** – easy to manage content with rich text and Raw HTML support
- Fully responsive and mobile-friendly
- Fast and lightweight deployment on PythonAnywhere

---

## 🛠 Tech Stack

- **Backend**: Django 6.0 + Wagtail 7.3
- **Frontend**: HTML5 + Tailwind / Bootstrap (simple and clean)
- **Database**: SQLite (easy to deploy)
- **Deployment**: PythonAnywhere
- **Editor**: Wagtail Admin (beautiful rich text + Raw HTML block support)

---

## 🚀 Quick Start (Local Development)

```bash
# 1. Clone the repository
git clone https://github.com/blurrr2/mein_django_projekt.git
cd mein_django_projekt

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
# source venv/bin/activate # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Start development server
python manage.py runserver
```

Open http://127.0.0.1:8000 in your browser.

---

## 📝 How to Add a New Article

1. Go to `/admin/`
2. Login with your superuser account
3. Click **Pages** → **Add child page** under Home → Choose **Blog Post**
4. Fill in title, date, category, and write content using the rich text editor
5. Publish

---

## 📂 Project Structure

```
mein_django_projekt/
├── meinprojekt/          # Main Django project
├── posts/                # Blog app
│   ├── models.py         # Post model (Wagtail Page)
│   ├── views.py
│   └── templates/posts/  # post_detail.html & posts_list.html
├── templates/
├── static/               # CSS, images
├── media/                # Uploaded images
├── db.sqlite3
└── requirements.txt
```

---

## 🌟 Author

**Sally**  
From China → Living in Germany  
Documenting my language learning, life in Germany, and coding journey.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

**Made with ❤️ and lots of German learning motivation**

需要我再加中文版本、或者加上项目截图、或者修改某些描述吗？随时告诉我！
