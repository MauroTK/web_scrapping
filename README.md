# Letterboxd Weekly Reviews Scraper

This project scrapes the most popular movie reviews of the week from Letterboxd using Python. It collects information such as movie title, year, reviewer name, review date, rating, review text, likes, and comments. The scraped data is then saved into a CSV file for further analysis or usage.

## Features

- Scrapes the top reviews from Letterboxd's "This Week" popular reviews section.
- Extracts detailed information for each review:
  - **Movie Title**
  - **Year**
  - **Author**
  - **Review Date**
  - **Rating** (converted to numerical values)
  - **Review Text**
  - **Likes**
  - **Comments**
- Outputs the data as a CSV file for easy access.

## Requirements

Before running the script, make sure you have the following Python packages installed:

- `requests` – for making HTTP requests to the Letterboxd website.
- `beautifulsoup4` – for parsing and extracting HTML content.
- `pandas` – for handling and storing the scraped data in a structured format (CSV).

You can install the required packages using `pip`:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

1. Clone this repository or download the script to your local machine.
2. Run the script to start scraping:

```bash
python main.py
```

3. The script will scrape the reviews and save the data into a file named Reviews.csv.

## Script Details

convert_rating(stars: str)
This function converts the star ratings (★ and ½) into numerical values. For example:
"★★★" → 3
"★★★★½" → 4.5

## Web Scraping Logic

The script makes requests to Letterboxd's weekly popular reviews page.
It collects information from the first three pages of reviews.
It extracts details like the movie title, reviewer's name, date of review, star rating, and review text.
All the data is compiled into a list of dictionaries and then saved as a CSV file using pandas.

## Data Output

After running the script, the `Reviews.csv` file will contain a table with the following columns:

| Movie Title           | Year | Author      | Review Date | Rating | Text            | Likes | Comments |
|-----------------------|------|-------------|-------------|--------|-----------------|-------|----------|
| The Shawshank Redemption | 1994 | John Doe    | 2024-11-01  | 5      | Amazing movie!  | 150   | 12       |
| Inception             | 2010 | Jane Smith  | 2024-11-02  | 4.5    | Mind-bending!   | 200   | 30       |
| The Dark Knight       | 2008 | Alex Johnson| 2024-11-02  | 4      | A masterpiece!  | 180   | 20       |

This is a sample representation of how the data will be saved into a CSV file after scraping the top reviews from Letterboxd for the week.

## Notes

- The script scrapes only the top reviews from the "This Week" section of Letterboxd, and is set to scrape the first 3 pages by default.
- If you want to scrape more pages, modify the range(1, 4) loop to your desired page numbers.
- Ensure that you are not violating Letterboxd’s terms of service when running this script. Use this script responsibly.
