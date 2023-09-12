# MedCure
Nama: Aldyandry N ||
NPM: 2206809936 ||
Kelas: PBP B

# Cara Mengimplementasi Checklist di Tugas Ini
 1. Membuat Sebuah Proyek Django Baru
    - Membuat direktori dan mengaktifkan *Virtual Environment*
      Cara mengaktifkan *Virtual Environment* : `python -m venv env` lalu `env\Scripts\activate.bat`
      VE perlu diaktifkan agar tidak mengganggu dependencies lain
    - Membuat berkas `requirements.txt` dalam direktori yang sama lalu tambahkan depedencies berikut:
     ```
     django
     gunicorn
     whitenoise
     psycopg2-binary
     requests
     urllib3
     ```
     - Install dependencies dengan `pip install -r requirements.txt`
     - Inisiasi proyek Django MedCure `django-admin startproject MedCure .`
     - Menambahkan `"*"` pada `ALLOWED_HOST` di `settings.py` untuk keperluan deploymet
     - Jalankan *Server* Django dengan `python manage.py runserver`
     - Sebagai tanda aplikasi Django telah dibuat, buka <http://localhost:8000> pada *browser* web
     - Tambahkan berkas `.gitignore` dengan teks berikut
       ```
        # Django
        *.log
        *.pot
        *.pyc
        __pycache__
        db.sqlite3
        media
        
        # Backup files
        *.bak 

        # If you are using PyCharm
        # User-specific stuff
        .idea/**/workspace.xml
        .idea/**/tasks.xml
        .idea/**/usage.statistics.xml
        .idea/**/dictionaries
        .idea/**/shelf
        
        # AWS User-specific
        .idea/**/aws.xml
        
        # Generated files
        .idea/**/contentModel.xml
        
        # Sensitive or high-churn files
        .idea/**/dataSources/
        .idea/**/dataSources.ids
        .idea/**/dataSources.local.xml
        .idea/**/sqlDataSources.xml
        .idea/**/dynamic.xml
        .idea/**/uiDesigner.xml
        .idea/**/dbnavigator.xml
        
        # Gradle
        .idea/**/gradle.xml
        .idea/**/libraries
        
        # File-based project format
        *.iws
        
        # IntelliJ
        out/
        
        # JIRA plugin
        atlassian-ide-plugin.xml
        
        # Python
        *.py[cod] 
        *$py.class 
        
        # Distribution / packaging 
        .Python build/ 
        develop-eggs/ 
        dist/ 
        downloads/ 
        eggs/ 
        .eggs/ 
        lib/ 
        lib64/ 
        parts/ 
        sdist/ 
        var/ 
        wheels/ 
        *.egg-info/ 
        .installed.cfg 
        *.egg 
        *.manifest 
        *.spec 
        
        # Installer logs 
        pip-log.txt 
        pip-delete-this-directory.txt 
        
        # Unit test / coverage reports 
        htmlcov/ 
        .tox/ 
        .coverage 
        .coverage.* 
        .cache 
        .pytest_cache/ 
        nosetests.xml 
        coverage.xml 
        *.cover 
        .hypothesis/ 
        
        # Jupyter Notebook 
        .ipynb_checkpoints 
        
        # pyenv 
        .python-version 
        
        # celery 
        celerybeat-schedule.* 
        
        # SageMath parsed files 
        *.sage.py 
        
        # Environments 
        .env 
        .venv 
        env/ 
        venv/ 
        ENV/ 
        env.bak/ 
        venv.bak/ 
        
        # mkdocs documentation 
        /site 
        
        # mypy 
        .mypy_cache/ 
        
        # Sublime Text
        *.tmlanguage.cache 
        *.tmPreferences.cache 
        *.stTheme.cache 
        *.sublime-workspace 
        *.sublime-project 
        
        # sftp configuration file 
        sftp-config.json 
        
        # Package control specific files Package 
        Control.last-run 
        Control.ca-list 
        Control.ca-bundle 
        Control.system-ca-bundle 
        GitHub.sublime-settings 
        
        # Visual Studio Code
        .vscode/* 
        !.vscode/settings.json 
        !.vscode/tasks.json 
        !.vscode/launch.json 
        !.vscode/extensions.json 
        .history
        ```

2. Membuat aplikasi 'main'
   - Inisiasi dahulu dengan perintah `python manage.py startapp main'
   - Membuat folder baru bernama `templates` dalam folder `main`
   - Membuat file `main.html` di dalam folder `templates`

3. Lakukan routing agar dapat menjalankan aplikasi `main`
   - Buat berkas `urls.py` pada folder aplikasi `main`. Isinya sebagai berikut.
     ```
        app_name = main
        urlpatterns = [
                      path('', show_main, name='show_main'),
        ]
      ```
     - Edit berkas `urls.py` pada folder `MedCure`dengan menambahkan `path('main/', include('main.urls'))` pada list `urlpatterns`

4. Buat model `item` di `main` dengan cara menginisiasinya dengan kode `class Item(models.Model):` yang memiliki atribut:
     - `name` berupa `CharField`
     - `amount` berupa `IntegerField`
     - `description` berupa `TextField`
     - `date_added` berupa `DateField`
     - `price` berupa `IntegerField`
       Setelah itu, migrasikan model dengan `python manage.py makemigrations` dan apply ke database dengan `python manage.py migrate`

5. Ubah berkas `views.py` dengan membuat fungsi `show-main` yang mereturn `render(request, "main.html", context)` untuk menampilkan `main.html` menggunakan data dari dictionary `context` sewaktu ada `request` dari user

6. Deployment ke `adaptable.io`
   - Seperti biasa, lakukan `add, commit, dan push` dan deploy sebagaimana yang dijelaskan pada **tutorial 0**


  
## Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
*Virtual Environment* merupakan alat yang membantu para *developer* dalam mengembangkan *software* di mana mereka dapat menginstal hal-hal yang diperlukan dalam proyeknya. Hal ini supaya *dependencies* tidak terganggu satu sama lain. Beberapa alasan mengapa kita menggunakan VE:
1. Menggunakan *virtual environment* memungkinkan kita untuk memiliki *dependencies* yang berbeda untuk proyek yang berbeda tanpa masalah. Misalnya, jika satu proyek membutuhkan versi Django tertentu dan proyek lain memerlukan *dependencies* yang berbeda, virtual environment memungkinkan kita untuk menjalankan kedua proyek tersebut pada *device* yang sama tanpa masalah.
2. Menggunakan VE dapat memudahkan kita untuk memahami *dependencies* apa saja yang diperlukan oleh sebuah proyek. Jika kita menghapus *virtual environment*, kita dapat yakin bahwa kita memanglah tidak menghapus *dependencies* atau perangkat lunak yang mungkin diperlukan oleh proyek lain.
3. Ada kemungkinan *hardware* kita memiliki *dependencies* yang sudah diinstal, tetapi tidak *compatible* atau mungkin kontras dengan proyek yang sedang dibuat. Jadi, VE dapat mencegah dari konflik tersebut.
4.  *Virtual environment* memudahkan *testing* dengan berbagai *dependencies*, sehingga  dapat memastikan bahwa aplikasi dapat berfungsi di berbagai konfigurasi.
      
 5. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur veniam minus saepe obcaecati qui sit, ipsam commodi iste itaque nostrum accusamus maiores dolore amet molestiae. Animi eos sapiente ipsa quis!


 1. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dolor odit, iste, totam accusamus deleniti soluta. Doloremque adipisci blanditiis nobis cupiditate quam expedita, consequatur nam neque vel tenetur tempore, sint aperiam.
 2. Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur veniam minus saepe obcaecati qui sit, ipsam commodi iste itaque nostrum accusamus maiores dolore amet molestiae. Animi eos sapiente ipsa quis!

## This Is *Markdown* Sample File
Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam accusantium nam impedit explicabo excepturi suscipit iste tempore quae, iure, eaque laboriosam fugit, assumenda nostrum et. Rem eaque, cupiditate consequatur tempora!  
`membuat` <b>Bold</b> 
