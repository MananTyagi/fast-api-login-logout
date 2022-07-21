# fast-api-login-logout
this is authentication feed system in fastapi (python).
1: Install all the dependencies with python Python 3.8.6
2: run the server by opening terminal in project root directory which contains all the files as shown in github.
3: "uvicorn main:app --reload" run thsi command without quotes
4: now the development server will start at  http://127.0.0.1:8000
![image](https://user-images.githubusercontent.com/63817084/180109536-903d618b-c435-4790-b36f-3c2d436e5b73.png)

5: this is API based project, (frontend is having some issues)
6:  "http://127.0.0.1:8000/docs" now this link will forward to you Swagger UI which is like "Postman" as shown below.
![image](https://user-images.githubusercontent.com/63817084/180109307-acb48ec8-9529-4d44-8e11-0439a7e301cb.png)

7: Rightnow there is only one user saved in the database whose credentials are in the file (main.py) itself.
8: once the user gets logged in, you will be able to get to "/private" endpoint, else you will get as shown below.
![image](https://user-images.githubusercontent.com/63817084/180109108-1c9631c0-f53a-4d64-ab75-72413af0a75d.png)
9: this session based authorization so, after successfully testing the login and private endpoint, you can logout the current user.

Happy coding!
         
