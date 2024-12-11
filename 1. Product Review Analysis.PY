# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality."
    "The performance of this product is excellent. Highly recommended!"
    "I had a bad experience with tis product. It didnt meet my expectations."
    "Poor quality product. Wouldnt recommend it to anyone."
    "The product was very average. Nothing extraordinary about it."
]

# List of keywords to highlight
keywords = ["good", "excellemt", "bad", "poor", "average"]

# Process the reviews and highliht keywords
for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
    print(review)


# Task 2:
# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality."
    "The performance of this product is excellent. Highly recommended!"
    "I had a bad experience with tis product. It didnt meet my expectations."
    "Poor quality product. Wouldnt recommend it to anyone."
    "The product was very average. Nothing extraordinary about it."
]

# Positive and negative word list
positve_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "dissapointing", "subpar"]
def sentiment_tally(reviews, positive_words, negative_words):
    total_positive = 0
    total_negative = 0
    for review in reviews:
        # count positive words in review
        for word in positive_words:
            total_positive += review.lower().count(word)
        # count negative words in review
        for word in negative_words:
            total_negative += review.lower().count(word)
    return total_positive, total_negative

# call function get tally
positive_count, negative_count = sentiment_tally(reviews, positve_words, negative_words)

print("Total Positive Words:", positive_count)
print("Total Negative Words", negative_count )

# Task 3:
reviews = [
    "This product is really good. I'm impressed with its quality."
    "The performance of this product is excellent. Highly recommended!"
    "I had a bad experience with tis product. It didnt meet my expectations."
    "Poor quality product. Wouldnt recommend it to anyone."
    "The product was very average. Nothing extraordinary about it."
]

def create_summary(review, max_length=30):
    if len(review) <= max_length:
        return review
    
    summary = review[:max_length]
    
    if not review[max_length].isspace():

        summary = summary.rsplit('', 1)[0]

        return summary + "..."
    
    # Generate and print summaries
    for review in reviews:
        print(create_summary(review))
        




