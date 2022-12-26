# SPICED Week06: Extracting, storing, analyzing tweets of @TheDemocrats and @GOP in the run-up to the midterms 2022 using the Python, MongoDB, Postgres and Metabase.

## Project Summary

<img width="624" alt="Bildschirmfoto 2022-12-25 um 21 01 42" src="https://user-images.githubusercontent.com/61935581/209559691-b9aad335-ffde-45af-90d5-29f244fdc068.png">

In this project, I build a data pippeline that collect tweets of @TheDemocrats and @GOP and stores them in a MongoDB. Next, the sentiment of tweets is analyzed using the two Python libraries "vaderSentiment"/"test2emotion" and the results are stored in a Postgres database. Finally, the findings of the analysis are clearly presented with the help of a Metabase dashboard.

Steps to achieve the project goal:
- Install Docker
- Build a data pipeline with docker-compose
- Collect Tweets
- Store Tweets in Mongo DB
- Create an ETL job transporting data from MongoDB to PostgreSQL
- Run sentiment analysis on the tweets
- Display the findings of the analysis with the help of a Metabase dashboard

## Documentation

Structure of the Dockerfile

![Dockerfile](https://user-images.githubusercontent.com/61935581/209560176-9ee88da6-5b68-413d-bafc-be86771a2892.png)

Dashboard on Metabase presenting the results of the sentiment analysis.

![Docker](https://user-images.githubusercontent.com/61935581/209560268-99cb2798-fcb0-4fc1-88fd-589f1a797d64.png)


## Installation of Docker

Go to [Docker homepage](https://docs.docker.com/get-docker/) and download Docker for your operating system.

## Usage

Clone the repository and navigate in your terminal to the cloned folder.
Execute the follwing commands in your terminal:

```bash
docker-compose build
docker-compose up
```

Afterwards, you can log-in to Metabase on your local machine and design the dashboard accoring to your liking.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
