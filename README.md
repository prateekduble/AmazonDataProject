AmazonDataProject
=================
This project is trying to understand consumer behavior based on the the helpfulness of the negative and positive reviews for product categories: Utilitarian and Hedonic

1. In order to extract the reviews for Categories such as Music, Books etc with keywords (ex: "fiction") ordered by salesrank (or price(low to high) or inverted price (high to low)), Use the following command:

$ python test.py Books fiction salesrank

This will create a file called, Books_fiction.txt. This data will have 30 products (ordered by salesrank) and all their associated reviews.

2. A sample line of data will look like:
ItemId, review_rating, #people_found_it_useful, #out_of_how_many, reviewer_id, title_of_the_review
"B00CNQ7HAU","2.0","2","4","A3NNLN31LHD8Q7","So disappointing..."

3. The code in analysis.py takes the above data file as argument:

$ python analysis.py Books_fiction.txt

Output:
		Helpful			Not Helpful		Total Respondents
Negative	249899 (72.29%)		95799 (27.71%)		345698 (100%)		
Positive	191214 (65.22%)		101974 (34.78%)		293188 (100%)
