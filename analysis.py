from sys import argv

# take filename as argument
script, filename = argv
file = open(filename)

data = []
reviews = {}

# Create list of lists with each list representing a review. 
for line in file:
    parts = line.replace('"', '')
    new_parts = parts.strip().split(",")
    data.append(new_parts)

negative_useful = 0.0
negative_nonuseful = 0.0
positive_useful = 0.0
positive_nonuseful = 0.0

for review in data:
    if review[1] == '1.0' or review[1] == '2.0':
        negative_useful = negative_useful + float(review[2])
        negative_nonuseful = negative_nonuseful + (float(review[3]) - float(review[2]))
    elif review[1] == '4.0' or review[1] == '5.0':
        positive_useful = positive_useful + float(review[2])
        positive_nonuseful = positive_nonuseful + (float(review[3]) - float(review[2]))

total_negative = negative_useful + negative_nonuseful
total_positive = positive_useful + positive_nonuseful

print "\t\tHelpful\t\tNot Helpful\tTotal Respondents"
print "Negative\t%d (%.2f%%)\t%d (%.2f%%)\t%d (100%%)" % (negative_useful,(negative_useful/total_negative)*100 ,negative_nonuseful,(negative_nonuseful/total_negative)*100,total_negative)
print "Positive\t%d (%.2f%%)\t%d (%.2f%%)\t%d (100%%)" % (positive_useful,(positive_useful/total_positive)*100 ,positive_nonuseful,(positive_nonuseful/total_positive)*100,total_positive)

