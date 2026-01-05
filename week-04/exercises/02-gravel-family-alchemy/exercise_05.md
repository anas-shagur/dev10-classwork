# Stretch Goal: Class-based SQLAlchemy

No pressure, but if you're up for it, think about class-based database patterns.

1. Create a `data.py` module.

2. Create classes that use these patterns:

    - Model-specific repositories
    - A generic repository
    - Active record (That won't go in `data.py`. It should go in `models.py`.)
    - Unit of work
    - Model-specific query classes

3. Use those classes to Create, Read, Update, and Delete in `main.py`.