from google_play_scraper import Sort, reviews
import csv
import logging

# app configuration, to be modified to desired setting
lang = "en"
country = "us"
app_id = "nl.rabomobiel"
filter_score_with = None
sort = Sort.MOST_RELEVANT
filename = "gp-review-data.csv"
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
csv_header = ['reviewId', 'userName', 'userImage', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at',
              'replyContent', 'repliedAt']


def write_to_csv(data):
    logging.info(">> Writing to data csv")
    if not data:
        logging.warning("> No data found to write to csv")
        return
    try:
        with open(filename, 'w', encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_header)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        logging.info("<< Finished writing to {} file".format(filename))
    except IOError:
        logging.error("I/O error when writing to csv")


# https://www.youtube.com/watch?v=O1Xh3H1uEYY&list=WL&index=54&t=2651s
def get_gp_reviews():
    logging.info(">> Retrieving GooglePlay reviews")
    result, _ = reviews(app_id, lang=lang, country=country, sort=sort, filter_score_with=filter_score_with)
    logging.info("<< Retrieved GooglePlay reviews")
    return result


if __name__ == '__main__':
    logging.info(">>> Application started")
    retrieved_reviews = get_gp_reviews()
    write_to_csv(retrieved_reviews)
    logging.info("<<< Application finished")
