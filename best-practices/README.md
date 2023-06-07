1) logging.ipynb contains an example of logging
2) logging.py contains a logging example that writes logs to a file

3) CI/CD test script in .gitlab-ci.yml that runs both unittest and logging:

- a) factorial.py is an example function that also logs to a logging_example_log.txt that is made available as an artifact to CI/CD<br>
- b) factorial_test.py contains unittest for the factorial function
