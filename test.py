import pyrebase

config = {
    "apiKey": "AIzaSyAPdBkq1pMQ8VY3H1NxXzFIWVQ4WGXwp24",
    "authDomain": "expensetracker-6da8c.firebaseapp.com",
    "projectId": "expensetracker-6da8c",
    "storageBucket": "expensetracker-6da8c.appspot.com",
    "messagingSenderId": "902060864180",
    "appId": "1:902060864180:web:e536e5b1ea5ce4dc9edde1",
    "databaseURL": "https://expensetracker-6da8c-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
data={
    'name':'Abhinav Krishna',
    'age':21,
    'Phone':9494100944
}
db.push(data)

