Ganesan Narayanan
grn2112
Final

To setup the Flask server, I first took a look at the app.py python file. The homepage was already given, and so I modified the home route to render the index.html
template. I then added another route for my first linked webpage called classes. And finally for the second webpage, I added another route called states. These would
each render a similarly named html file. I then worked to actually create these html files. For index.html, I added my name, bolding it using the bold tag, 
a picture of myself using the img tag, my school year, and my major, all in plain text. I then included links that would redirect to the other two routes that I created. 
Finally, I added a hyperlink to my favorite news source. The classes page lists the classes that I took this semester, and then a few sentences detailing my favorite class in 
plain text. The states page includes a list of the all the states that I've visited in the US in plain text along with the state flag for that state using the img tag.
The pictures I included in the homepage and the states page were stored in a static folder under a subfolder images, and route was used in
the html files. 
This concludes the Flask server final project. 
