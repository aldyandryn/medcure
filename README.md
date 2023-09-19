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
<<<<<<< HEAD

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
   - Setelah itu, migrasikan model dengan `python manage.py makemigrations` dan apply ke database dengan `python manage.py migrate`

5. Ubah berkas `views.py` dengan membuat fungsi `show-main` yang mereturn `render(request, "main.html", context)` untuk menampilkan `main.html` menggunakan data dari dictionary `context` sewaktu ada `request` dari user

6. Deployment ke `adaptable.io`
   - Seperti biasa, lakukan `add, commit, dan push` dan deploy sebagaimana yang dijelaskan pada **tutorial 0**


  
## Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya 
![image](https://github.com/aldyandryn/medcure/assets/73996348/abd6981a-e303-4bb4-a5bd-b4a88524c73b)


## Mengapa kita menggunakan virtual environment? 
*Virtual Environment* merupakan alat yang membantu para *developer* dalam mengembangkan *software* di mana mereka dapat menginstal hal-hal yang diperlukan dalam proyeknya. Hal ini supaya *dependencies* tidak terganggu satu sama lain. Beberapa alasan mengapa kita menggunakan VE:
1. Menggunakan *virtual environment* memungkinkan kita untuk memiliki *dependencies* yang berbeda untuk proyek yang berbeda tanpa masalah. Misalnya, jika satu proyek membutuhkan versi Django tertentu dan proyek lain memerlukan *dependencies* yang berbeda, virtual environment memungkinkan kita untuk menjalankan kedua proyek tersebut pada *device* yang sama tanpa masalah.
2. Menggunakan VE dapat memudahkan kita untuk memahami *dependencies* apa saja yang diperlukan oleh sebuah proyek. Jika kita menghapus *virtual environment*, kita dapat yakin bahwa kita memanglah tidak menghapus *dependencies* atau perangkat lunak yang mungkin diperlukan oleh proyek lain.
3. Ada kemungkinan *hardware* kita memiliki *dependencies* yang sudah diinstal, tetapi tidak *compatible* atau mungkin kontras dengan proyek yang sedang dibuat. Jadi, VE dapat mencegah dari konflik tersebut.
4.  *Virtual environment* memudahkan *testing* dengan berbagai *dependencies*, sehingga  dapat memastikan bahwa aplikasi dapat berfungsi di berbagai konfigurasi.


## Perbedaan MVC, MVT, dan MVVM
1. MVC (Model-View-Controller)
   - **Model** : Mewakili data atau logika bisnis karena merupakan bagian yang bertanggung jawab dalam mengakses data, pertanyaan *database*, dan pembaruan *database*
   - **View** : Menampilkan data karena merupakan antarmuka pengguna yang akan dilihat oleh pengguna
   - **Controller** : Menerima input dari pengguna melalui *view*, lalu memprosesnya (dengan bantuan *Model* jika diperlukan), kemudian akan mengembalikan tampilan yang pas
   - **Contoh** : *Framework* Spring (Java) dan Express (Javascript dengan Node.js)

 2. MVT (Model-View-Template):
    Konsepnya mirip dengan MVC. Namun, dalam konteks framework Django (yang populer menggunakan MVT), perbedaannya terutama ada pada bagian "View"
    - **Model**: Sama seperti dalam MVC, mewakili data atau logika bisnis.
    - **View**: Dalam MVT, View lebih mendekati *controller* pada MVC. *View*
menangani logika bisnis dan menetapkan tampilan mana yang harus
ditampilkan.
    - **Template**: Ini adalah bagian yang menampilkan informasi untuk pengguna (mirip dengan View dalam MVC).
    - **Contoh**: Django adalah contoh utama dari *framework* yang mengikuti pola MVT.

3. MVVM (Model-View-ViewModel): Biasanya digunakan untuk aplikasi yang mengandalkan binding data dua arah.
   - **Model**: Mewakili data atau logika bisnis.
   - **View**: Menampilkan data, tetapi dengan MVVM, View adalah yang pasif dan hanya bertanggung jawab untuk menampilkan apa yang diberitahu oleh ViewModel.
   - **ViewModel**: Bertindak sebagai perantara antara Model dan View. ViewModel menyediakan data dalam format yang mudah digunakan oleh View dan dapat merespons terhadap perubahan data yang dilakukan oleh View.
   - **Contoh**: *Frameworks* seperti KnockoutJS, Angular, dan Xamarin sering kali mengikuti pola MVVM.


 ## Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Ya, bisa. Namun, ketika jumlah proyek dan dependencies yang kita kerjakan
meningkat, akan ada kemungkinan ditemukannya suatu masalah dan risiko akan
adanya *problem* juga semakin meningkat. Oleh karenanya, *virtual
environment* disarankan digunakan karena dapat menjaga konsistensi dan
mengoptimalkan proses pengembangan menjadi lebih lancar.

=======

# Tugas 3

## Apa perbedaan antara form `POST` dan form `GET` dalam Django?

**Fungsi:**
- GET: Lebih sering diterapkan untuk memperoleh informasi dari server. Misalnya, ketika Anda melakukan pencarian di web atau menjelajahi laman, Anda mungkin menggunakan metode GET.
- POST: Lebih ditujukan untuk menyampaikan informasi ke server. Situasinya mirip ketika Anda mengisikan sebuah formulir online, mungkin untuk pendaftaran atau memberi komentar.
  
**Cara Menyimpan Informasi:**
- GET: Informasi dikirim melalui parameter di alamat web. Misalnya, saat Anda mencari "Django", alamat web mungkin menjadi: http://example.com/search?query=Django.
- POST: Informasi ditempatkan dalam bagian tubuh permintaan dan oleh karena itu tidak muncul di alamat web.

**Kapasitas Informasi:**
- GET: Terdapat keterbatasan dalam panjang alamat web yang varianya tergantung pada browser dan server. Ini membatasi berapa banyak informasi yang dapat dikirim dengan metode GET.
- POST: Tidak ada pembatasan panjang seperti yang ditemui di GET, sehingga memungkinkan pengiriman informasi dalam volume yang lebih besar.
  
**Aspek Keamanan:**
- GET: Mengingat informasi muncul di alamat web, metode GET tidak ideal untuk informasi sensitif, misalnya password. Juga, alamat web berisiko tersimpan di riwayat browser atau difavoritkan.
- POST: Ini lebih aman karena informasi disembunyikan dari alamat web. Walaupun demikian, keamanan tambahan seperti penggunaan HTTPS tetap dianjurkan.
  
**Konsistensi:**
- GET: Harus konsisten atau idempoten, artinya permintaan GET yang sama harus menghasilkan respons yang sama tanpa merubah apapun di server.
- POST: Tidak selalu konsisten. Permintaan POST yang sama mungkin menghasilkan respons yang berbeda, seperti penambahan data baru di database.
  
**Integrasi dengan Django:**
GET: Di Django, data dari form GET bisa diakses menggunakan request.GET.
POST: Sedangkan untuk form POST, Anda mengambilnya dengan request.POST.

Berikut tabel perbedaan GET dan POST dari [W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp "W3Schools")
![image](https://github.com/aldyandryn/medcure/assets/73996348/a9e249d4-4f53-4531-ac24-4defcb67efdc)

# Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

# Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

#  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
