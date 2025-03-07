# Clean Architecture Refactor

Repository ini merupakan hasil refactor dari implementasi hands-on berbasis MVC ke Clean Architecture dengan menggunakan Flask dan SQLAlchemy.

## Perubahan Utama dari MVC ke Clean Architecture

- **Pemisahan Layer Berdasarkan Tanggung Jawab**
  - **Domain Layer:**  
    - Dibuat entitas `UserEntity` di file `domain/user.py`.
  - **Repository Layer:**  
    - Didefinisikan interface `UserRepository` di file `repository/user_repository.py`.
    - Implementasi (`UserRepositoryImpl`) dibuat di file `repository/user_repository_impl.py`.
  - **Use Case Layer (Business Logic):**  
    - Dibuat file `usecase/user_usecase.py` untuk logika bisnis, memproses request, dan menghubungkan ke repo 
    - Logika bisnis yang sebelumnya berada di controller pada arsitektur MVC dipindahkan ke sini.
  - **Controller dan Routing:**  
    - Controller (`controllers/user_controller.py`) diperbarui untuk menggunakan use case.
    - File routing (`routes/routes.py`) hanya mengubah inisialisasi saja dari perubahan controller.


