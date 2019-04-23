# Using-Yelp-to-Improve-Poor-Restaurants

We implemented and developed our review processing algorithm from  vlad sandulescu ‘s algorithm on opinion phrase mining.
The idea is that when reading a review a simple way to extract people’s opinion is to look for nouns and pick the nearest 
adjective around it. We were also extract the compounded nouns. Thereby, it can show the syntactic dependencies between words 
and even predict the overall sentiment of a text. 

The algorithm takes text input to begin the review processing. By tokenizing the sentences it takes each word apart and applies parts of speech tagging for that word. From these tags a basic pattern is formed. First, in the ReviewPhrases class it creates objects for phrases and reviews. In the Pattern class is creates an object for pattern and sets a relation for patterns as key, value pairs. When extracting the basic pattern, 

We use stopwords to clean the patterns so that we are left with only significant patterns
