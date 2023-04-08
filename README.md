# project-backend

A simple web app made to welcome users with the use of Flask framework. This is the backend part. Application has been tested with use of Locust.

# how to start

1. Clone the repository.
2. Install the requirements using command: `pip install -r requirements.txt`.
3. Run the app using command: `python main.py`.
4. Use the web browser and paste a link: `http://localhost:5000`.
5. Use below paths:
  - simple welcome to user: `/`.
  - personalized welcome to user: `/hello`.
  
  # locust testing
  
  1. Complete "how to start".
  2. Start local environment. You can use command: `pip install pipenv` and run using: `pipenv shell`.
  3. Start new terminal and use command: `pip install locust`.
  4. Run locust using command: `locust`.
  5. Use the web browser and pase a link: `http://localhost:8089`.
