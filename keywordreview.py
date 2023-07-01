import csv
import re

keywords = ['Jockey', 'jockey', 'Undergarments','undergarments','Exclusice Store','exclusive store','Best Products','best products','Women Store','Kids Wear','kids wear','women store']  # List of keywords to count

with open('/home/mind/Pictures/tisareview2.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    keyword_counts = {keyword: 0 for keyword in keywords}  # Initialize count for each keyword

    for row in csv_reader:
        review = row['Review']  # Assuming the review text is in the 'Review' column
        review = re.sub('[^a-zA-Z]', ' ', review)  # Remove non-alphabetic characters
        review = review.lower()  # Convert to lowercase

        for keyword in keywords:
            count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', review))
            keyword_counts[keyword] += count

# Print the keyword counts
for keyword, count in keyword_counts.items():
    print(f'{keyword}: {count}')
