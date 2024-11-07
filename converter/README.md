# Project Title:
CLOUD CONVERTER
# Description:
An advanced Django-based web application that allows users to convert images from JPG or JPEG formats to PNG formats.

# Installation:
1. Clone the repository:
```bash
 git clone https://github.com/yourusername/yourproject.git
```
2. Install Requirement.txt file:
```bash
 pip install -r requirements.txt
 ```
## Usage
To run the project, you have to install Redis from https://github.com/tporadowski/redis/releases 
after opening this you have to download this version Redis-x64-5.0.14.1.msi of redis 
open 3 terminals of vscode.
In the first one run the command
   ```bash
        python manage.py runserver
   ```
On the second terminal go to the path where redis is install and run the command
 ```bash
        redis-server.exe
   ```
On the third terminal you to run the command for the Celery worker
```bash
     celery -A image_converter  worker --loglevel=info --pool=solo
 ```