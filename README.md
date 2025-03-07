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

- **Hasilnya:**
- ![Screenshot 2025-03-07 134304](https://github.com/user-attachments/assets/89622bd2-75fc-4ad0-9ad6-68c69f0a8599)
- ![Screenshot 2025-03-07 134339](https://github.com/user-attachments/assets/badc1740-0df3-4a1e-8721-3a7f2294ca5f)



