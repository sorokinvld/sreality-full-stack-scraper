# Python dev task
I used **scrapy framework** to scrape the first 500 items (title, image url) from *sreality.cz* (flats, sell) and saved it in the **PostgreSQL** database. 
Implemented a simple HTTP server in Python using **Flask** and shown these 500 items on a simple pages with pagination (title and image) and put everything to single **docker-compose** command so that you can just run `docker-compose up` in the Github repository and see the scraped ads on http://127.0.0.1:8080 (Flask backend) page, and http://localhost:3000 (Nextjs with TS frontend).
