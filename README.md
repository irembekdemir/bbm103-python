# Python Beginner Projects Collection 

Welcome to my Python playground! This repository is created as the repository of my coursework during HU CS/AI BBM101-103 journey. Later on I'll be adding new beginner friendly project. Stay tuned!

Each project focuses on clean code practices, logical data structures, and user-centric designs.

---

## 📂 Project Showcases

### 1. Simple Contact Manager 📇 (`contact-manager`)
A command-line terminal application built around structural dictionary-to-list matching.
- **Interface:** Interactive, looped Command-Line Interface (CLI).
- **Key Feature:** Uses a tuple-based configuration matrix (`CONTACT_INFOS`) to dynamically parse custom attributes (Name, Phone, Email, Country) across addition, editing, and visualization modules.
- **Highlights:** Built-in error boundary loops ensuring strict inputs (e.g., telephone inputs isolated to exactly 11 numeric characters). 

### 2. Smart Shopping Cart System 🛒 (`shopping-cart`)
An advanced, multi-featured shopping cart software that bridges modular business logic with a desktop layout.
- **Interface:** Built using Python's comprehensive **PyQt5** framework with customized CSS injection for a sleek corporate layout.
- **Logic Matrix:** Integrates algorithmic discounts for bulk purchases (quantity > 3), automatic price tagging for promotional items, and conditional verification codes (`WELCOME10`, `SAVE20`, etc.).
- **Highlights:** Uses strict input type-guards (`is_int`, `is_float`) to ensure data sanitization.
- **Note:** *The foundational PyQt5 GUI template was provided by the course instructor; all core computational backend functions, cart control algorithms, and logic integrations were independently engineered and implemented by me.*
  
### 3. Cute To-Do List Application ✨ (`cute-todo-app`)
A charming desktop task organizer featuring a light pastel aesthetic.
- **Interface:** Built with `CustomTkinter` for a smooth, modern visual layout.
- **Key Feature:** Automates spreadsheet updates by compiling active tasks into a color-coded, custom-styled Excel sheet (`todo_list.xlsx`) saved directly to your desktop.
- **Highlights:** Dynamic checklist widget destruction on removal and auto-fitted Excel table dimensions using `openpyxl`.
- **Note:** *The CustomTkinter GUI layout, widget structures were co-designed and generated using AI (Gemini) assistance, while the complete app architecture, environment structure, and spreadsheet automation logic were implemented by me.*
  
---

## 🛠️ Global Core Technologies

- **Core Engine:** Python 3.14 (or Python 3.x)
- **GUI Frameworks:** PyQt5, CustomTkinter
- **Data Engineering:** OpenPyXL (Excel engine)
- **System Utilities:** Native `sys` streams, OS paths

---

## 🚀 Environment Setup & Deployment

Every project inside this collection is optimized to run efficiently within separate local sandboxes.

1. **Clone the entire portfolio:**
   ```bash
   git clone [https://github.com/irembekdemir/python-beginner-projects.git](https://github.com/irembekdemir/python-beginner-projects.git)
   cd python-beginner-projects
   ```

2. **Navigate to your chosen project folder:**

```bash
# Example for the Shopping Cart
cd folder_name_of_smart_cart
```

3. **Establish a lightweight virtual sandbox:**

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate
```

4. **Install necessary project requirements:**

```bash
# For GUI applications
pip install PyQt5         # if running the Smart Cart
pip install customtkinter openpyxl  # if running the Cute To-Do App
```

✍️ Developer Profile
@irembekdemir


