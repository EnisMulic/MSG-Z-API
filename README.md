# MSG-Z-API

### Clone the repository and navigate to the application

```
git clone https://github.com/EnisMulic/MSG-Z-API.git
cd MSG-Z-API
```

### Install the python virtual environment

```
pip install pipenv 
```

### Start the virtual environment

```
pipenv shell 
```

### Install dependencies 

```
pipenv install
```

### Create the migration folder

```
python migrate.py db init
```

### Making changes to the entity models or adding new ones

```
python migrate.py db migrate
python migrate.py db upgrade 
```

### Start the application

```
python app.py
```