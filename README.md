# kick-street
https://valerian-hizkia-kick-street.pbp.cs.ui.ac.id/

## Checklist implementation

### a. Pembuatan file django baru
Hal ini dilakukan dengan menjalankan perintah ```django-admin startproject <nama projek> <direktori projek>```.

### b. Pembuatan aplikasi main
Hal ini dilakukan dengan menjalankan perintah ```python manage.py startapp <nama aplikasi>```.


### c. Routing untuk aplikasi main
Dilakukan dengan menambahkan ```'main'``` di akhir array ```'INSTALLED_APPS'``` di file ```settings.py```.

### d. Pembuatan model
Dilakukan dengan mengisi file ```models.py``` dengan properti objek yang telah ditentukan. Syntax mengikuti 

### e. Pembuatan fungsi view
Dilakukan dengan membuat fungsi yang memanggil fungsi ```render()``` dengan parameter file HTML dan context. Template HTML mengikuti arahan dari dokumentasi Django dan dipercantik dengan Tailwind CSS.

Penggunaan file static juga dijelaskan di dokumentasi Django dengan menambahkan file path pada ```settings.py```. Gambar dihasilkan oleh Nano Banana milik Google.

### f. Routing
Dilakukan dengan menambahkan file ```urls.py``` pada aplikasi ```main``` dan mendaftarkannya di file ```urls.py``` pada direktori projek utama di ```kick_street```



## Helpful URLs
https://docs.djangoproject.com/en/5.2/
https://tailwindcss.com/