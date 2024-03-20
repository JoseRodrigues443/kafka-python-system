# miguel-quix-code-challenge

Implementation of the requirements at https://quix.notion.site/Python-engineer-code-challenge-e9d663af91e14572b5f7aa58707c84c0

Made by miguelrodrigues.org

- [miguel-quix-code-challenge](#miguel-quix-code-challenge)
  - [Running instruction](#running-instruction)
  - [Project Structure](#project-structure)
  - [Screenshots](#screenshots)


## Running instruction

```bash

# start kafka (using docker)




# Run the script to add all the data from CSV to kafka
make demo

# Actual code that executes the challenge
make run

```


## Project Structure

```bash

.
├── LICENSE
├── Makefile
├── Python engineer code challenge.pdf
├── README.md
├── app                             # Core APP
│   ├── __init__.py
│   ├── aggregator.py
│   ├── consts.py
│   ├── consumer.py
│   ├── main.py
│   ├── producer.py
│   └── tests                           # Tests
│       └── aggregator_test.py
├── demo                                # Script that provides all the data the data topic
│   ├── __init__.py
│   ├── generator.py
│   └── online_retail_II.csv
├── docker-compose.yml
└── requirements.txt

3 directories, 16 files


```


## Screenshots

![Running consumer and producer](./demo.png)

