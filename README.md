# Web application project arXiv

arXiv is an open-access repository of articles. Authors can post their demo versions of articles, so users can buy it.
At this moment there are 3 main categories of articles: math, physics and computer science.

## Backend
* Language: **Python3**
* Main framework: **Django REST framework**
* Data Base: **SQLite**


Additional functionality:
* REST API methods: **GET/POST/PUT** available by address _http://\<your IP>:\<you port>/api/articles/_
* Implemented a **search method** on the backend side: e.g. _/api/articles/?min_price=100&max_price=500&text=backpropagation_ will find articles which costs
between 100$ and 500$ having text «backpropataion» in title.
* Autorization by generating **CSRF token** using **Сookie** session
* Using Django **ORM** to interact with the database

## Frontend
* Language: **Java Script + HTML + CSS**
* Main framework: **React**

Additional functionality:
* Using **Redux** store for temporary data
* **Autorization / Registration** functionality
* Supports additional functionality to **edit article** title if you logged in as an **admin**

Also implemented **Progressive Web Application** that connects to the web service from phone.

## Demonstration
### Start page
![image](https://user-images.githubusercontent.com/90476839/218650212-57227e2b-f804-4363-8b52-5dc6769c3f77.png)
### Main categories of articles
![image](https://user-images.githubusercontent.com/90476839/218650389-cb4ec1bf-59d3-43f8-9e77-00fb4fa1dce4.png)
### Computer Science articles
![image](https://user-images.githubusercontent.com/90476839/218650822-a33bdcb5-9313-49d4-a185-1b04e4702df0.png)
### We can create an account for buying articles
![image](https://user-images.githubusercontent.com/90476839/218651541-7c40bdf2-d182-438d-8b48-ed04bc2f48f5.png)
### Or we can login
![image](https://user-images.githubusercontent.com/90476839/218651642-42e7a998-cc8a-4012-867d-639721556ae6.png)
### When we logged in we can buy many articles
![image](https://user-images.githubusercontent.com/90476839/218652088-323ad4ef-e1aa-4d1a-974b-04523e228681.png)
### You can search specific article if needed
![image](https://user-images.githubusercontent.com/90476839/218652286-2c0466b2-6838-472d-9f10-cca0c611deea.png)
### If you logged in as an admin - you can chang articles titles, and changes will be uploaded on server
![image](https://user-images.githubusercontent.com/90476839/218652490-52df77c5-ca83-48db-a784-ea96f5a3bf42.png)


