# Project 2

A simple Flask app with Behave tests for: static routes, dynamic routes, and a basic utility

### Pre-reqs: 
   - [docker](https://docs.docker.com/install/)

### Running [`Flask`](https://flask.palletsprojects.com/):
   - `docker build -t p2 ./projects/project2`
   - `docker run -it -p 5555:5000 p2`
   - Navigate to http://localhost:5555/

### Running [`behave`](https://behave.readthedocs.io/en/latest/):
   - `docker run -it p2 behave`

### Example Output
![Screen Shot 2020-04-26 at 7 07 51 PM](https://user-images.githubusercontent.com/5629547/80322205-78b1ae80-87f1-11ea-8461-6dae4eee53d7.png)
