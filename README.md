### Overview
<div style = "display: flex">
  <img src = "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src = "https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
</div>

This repository contains basic REST API which is created with Flask backend

### Setup guide
**All setup guide assumes that you are using Linux**

Clone this repository
```
>>> git clone https://github.com/egesabanci/bilisim-school-app
```
Change directory into the project folder
```
>>> cd bilisim-school-app
```
Create a virtual environment for avoid conflicts with other local Python projects
```
>>> python3 -m venv env
```
Activate virtual environment
```
>>> source env/bin/activate
```
Install dependencies for virtual environment
```
>>> pip3 install -r requirements.txt 
```
Change directory into the source code
```
>>> cd src
```
Run the server
```
>>> python3 main.py
```

#### Additional notes
- You can change the configuration of the server via `src/config.json`
but all the Postman collections have been created for `localhost:8000`.
**Changes may be a problem for Postman testing environment**.