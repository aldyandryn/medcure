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

## Tugas 3

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
- GET: Di Django, data dari form GET bisa diakses menggunakan request.GET.
- POST: Sedangkan untuk form POST, Anda mengambilnya dengan request.POST.

Berikut tabel perbedaan GET dan POST dari [W3Schools](https://www.w3schools.com/tags/ref_httpmethods.asp "W3Schools")
![image](https://github.com/aldyandryn/medcure/assets/73996348/a9e249d4-4f53-4531-ac24-4defcb67efdc)

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
**JSON:**

1. Dalam banyak situasi, JSON jelas lebih mudah dibaca dibandingkan XML, terutama dalam bentuk yang sudah diperluas.
2. JSON biasanya memiliki jumlah karakter yang lebih sedikit, mengurangi beban dalam transfer data.
3. Mengurai JSON jauh lebih mudah. Namun, hal ini hanya relevan jika seseorang sedang menulis parser, yang saat ini bukanlah aktivitas yang umum.

**XML:**

1. Teknologi XML memiliki standar universal yang tidak dimiliki oleh JSON.
2. XML memiliki struktur data yang lebih kokoh dibandingkan JSON.
3. XML lebih cocok untuk menggabungkan set informasi dari berbagai sistem dibandingkan JSON.
4. XML mendukung ekstensi dari tipe dasar yang tidak didukung oleh JSON.
5. Berbeda dengan JSON, XML ditinjau oleh komite standar universal.
6. HTML adalah tata bahasa XML, khususnya HTML5, yang harus sesuai dengan definisi XML yang "baik".
7. XML mendukung penambahan komentar, sedangkan JSON tidak.

**HTML:**

1. HTML membantu membangun struktur situs web dan merupakan Bahasa Markup yang banyak digunakan.
2. Semua browser mendukung bahasa HTML.
3. HTML ringan dan cepat dimuat.
4. Penyimpanan file besar diizinkan berkat fitur cache aplikasi.
5. Tidak perlu membeli perangkat lunak tambahan karena sudah tersedia secara default di setiap sistem operasi jendela.
6. Sintaksis yang fleksibel (meski terlalu fleksibel mungkin tidak sesuai dengan standar).
7. HTML mudah diedit karena berupa teks biasa.
8. Mudah diintegrasikan dengan bahasa lain seperti JavaScript, CSS, dan lainnya.
9. HTML mudah untuk dikodekan bahkan oleh pemrogram pemula.
10. HTML memungkinkan penggunaan template, memudahkan desain halaman web.
11. Cepat diunduh karena teks dapat dikompresi.
12. Sangat bermanfaat bagi pemula di bidang desain web.
13. HTML didukung oleh hampir semua browser, jika bukan semua browser.
14. HTML digunakan pada hampir setiap situs web, jika bukan semua situs web.
15. HTML semakin sering digunakan untuk penyimpanan data seperti sintaks XML.
16. HTML memiliki banyak tag dan atribut yang dapat mempersingkat baris kode Anda.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern

- **Kejelasan Struktur**: JSON menawarkan format yang intuitif dan jelas, memudahkan baik manusia maupun komputer untuk memahami. Desainnya yang berorientasi pada pasangan kunci-nilai sangat mirip dengan struktur data di banyak bahasa pemrograman, menjadikannya mudah untuk diintegrasikan.
- **Efisiensi Ukuran**: Jika dibandingkan dengan standar lain seperti XML, JSON cenderung lebih padat dan singkat. Hal ini berkontribusi pada transmisi data yang lebih efisien dan penggunaan bandwidth yang minimal.
- **Kompatibilitas Tinggi**: Sebagian besar bahasa pemrograman saat ini memiliki alat atau fitur bawaan untuk memproses JSON. Hal ini mempermudah pertukaran informasi antara sistem dengan teknologi yang beragam.
- **Sintaksis Sederhana**: Berbeda dengan XML yang membutuhkan tag tambahan untuk setiap elemen, JSON lebih langsung dalam pendekatannya.
- **Sinergi dengan JavaScript**: Mengingat latar belakang JSON yang berasal dari JavaScript, kerjasama antara keduanya di lingkungan web sangatlah erat.
- **Kemampuan Adaptasi**: JSON dapat merepresentasikan data dengan kompleksitas tinggi, seperti list atau objek bertingkat, tanpa memerlukan definisi tambahan.
- **Dominasi di RESTful APIs**: Sejumlah besar API yang menganut prinsip REST (Representational State Transfer) memilih JSON sebagai format standar respons mereka, yang memperkuat popularitas JSON di komunitas developer.
- **Aspek Keamanan** : Meski keamanan perlu selalu diperhatikan, menggunakan JSON—dengan pendekatan yang tepat—cenderung lebih terlindungi dari ancaman khusus yang mungkin muncul saat mengolah XML.

##  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [ ] Membuat input `form`
    1. Membuat `base.html` pada root/templates
    ```
    html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```
    Note: 
    - `{% something %}` dapat diisi dari file lain (seperti semacam placeholder)
    2. Membuat `forms.py` pada `vending_machine/main` dengan
    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "amount", "description"]
    ```
    Notes: 
    - `model = Product` menandakan bahwa isian form akan disimpan sebagai object Product
    - `fields` menandakan bahwa object Product memiliki 4 atribut yang dapat diisi melalui form (name, price, amount, description)
  
    3. Ubah function `show_main`
    ```python
    def show_main(request):
        products = Product.objects.all()
        context = {
            'name': 'Aldyandry',
            'class': 'PBP B'
            'products': products,
            'total_products': products.__len__(),
        }

        return render(request, "main.html", context)
    ```
    Notes:
    - `'products` akan menyimpan seluruh product
    - `total_products` akan menyimpan banyak product
    4. Buat `create_product.html` 
    ```html
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    Notes: 
    - `{% block content %} ... {% endblock %}` adalah konten yang akan mengisi placeholder block content pada `base.html`
<hr>

- [ ] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by ID*, dan JSON *by ID*.
    1. `create_product` untuk menerima input user
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)    
    ```
    2. `show_xml` untuk menampilkan products dalam format XML
    ```python
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    3. `show_json` untuk menampilkan products dalam format JSON
    ```python
    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")    
    ```
    4. `show_xml_by_id` untuk menampilkan product dengan id yang diinginkan dalam format XML
    ```python
    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    
    ```
    5. `show_json_by_id` untuk menampilkan product dengan id yang diinginkan dalam format JSON
    ```python
    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")    
    ```
<hr>

- [ ] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
    1. Isi urls.py yang ada pada templates dengan:
    ```python
    from django.urls import path
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id # , show_products

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'), 
        path('create-product', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```
    `urlpatterns` digunakan agar function-function yang telah dicantumkan pada `views.py` dapat diakses dengan url yang diinginkan, untuk project ini detailnya sebagai berikut:
    - `(url)/create-product`: Untuk user input product baru
    - `(url)/xml`: Untuk menampilkan products dalam format XML
    - `(url)/json`: Untuk menampilkan products dalam format JSON
    - `(url)/xml/(desired_id)`: Untuk menampilkan product dengan id yang diinginkan dalam format XML
    - `(url)/xml/(desired_id)`: Untuk menampilkan product dengan id yang diinginkan dalam format JSON
<hr>

## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
Note: Menghapus product ke-1 (pk="1") dan ke-5 (pk="5") sehingga tidak ada pk="1" dan pk="5"
1. HTML:
   ![image](https://github.com/aldyandryn/medcure/assets/73996348/167c0547-95bb-4b29-86a1-b46a4e01dc34)

2. XML:
   ![image](https://github.com/aldyandryn/medcure/assets/73996348/a0685db9-7fe1-4faa-919d-b6fc3f10d3b1)

3. JSON:
   ![image](https://github.com/aldyandryn/medcure/assets/73996348/39fd0ac1-3bdc-40bc-ab92-6c4266f43c9a)

4. XML by ID:
   ![image](https://github.com/aldyandryn/medcure/assets/73996348/c85db0f4-f3ac-4975-a9b3-35f1a4c89493)

5. JSON by ID:
    ![image](https://github.com/aldyandryn/medcure/assets/73996348/95d07fb6-3f89-47ad-8b0c-6ef5e1dff857)

## Diambil dari:
- [Get vs. Post](https://www.javatpoint.com/get-vs-post)
- [Tutorial 2](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-2)
- [Geeksforgeeks](https://www.geeksforgeeks.org)
- [Dataxml](https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/#:~:text=The%20differences%20between%20XML%2C%20JSON,how%20that%20data%20is%20displayed.)
  
===
