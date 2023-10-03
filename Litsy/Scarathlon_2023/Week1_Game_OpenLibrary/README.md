# Litsy Scarathlon Game: Week 1
"Name as many books as possible that have something in common with either of your team's buddy reads. This can be anything other than the genre. 10 points per answer. Unlimited points available."

On team Bat Brigade our buddy reads were ["Pumpkinheads"](https://www.goodreads.com/book/show/40864790-pumpkinheads) by Rainbow Rowell and Faith Erin Hicks and ["A Dowry of Blood"](https://www.goodreads.com/en/book/show/60521937) by S.T. Gibson.

## The TL;DR Version
I used Open Library and Python to find books related to the buddy reads based on keywords present in both books. The grand total was 635 books! That's 6,350 points! Woo hoo!

## The Approach
I loooooove programming. When I saw this game, I thought "Oooh, I bet I could query an internet book database for keywords related to each book and get tons of results back (points are unlimited after all)". After confirming with my partner, @catsandbooks, and team captain that this approach was "legal" re: the Scarathlon rules, I set about finding a database I could query easily for free. I found the [Open Library Search API](https://openlibrary.org/dev/docs/api/search) to be very easy to use with just a web browser.

First, I looked through "Pumpkinheads" for words or pictures that could reasonably be used as keywords in my queries. I haven't read "A Dowry of Blood" and wasn't going to, so the only keywords I had for that book were "Blood", "Dowry", and "Vampire". The rest from "Pumpkinheads" were Apple Cider, Apples, Campfire, Candy, Caramel Apples, CornMaze, Crow, Fudge, Funnel Cakes, Goat, Golf, Halloween, Hotdog, John Denver, Kettle Corn, Magic, Marshmallow, Mouse, October, Pie, Pony, Pumpkin Patch, Pumpkin, S'mores, Scarecrow, Squirrel, Succotash, and Train.

I queried the Open Library Search API in the browser with each of these keywords. Here's an example query: https://openlibrary.org/search.json?q=apple+cider. After hitting "Enter" I saved the result page as a JSON file, which is a kind of data storage format. In this repository you can see each one of these JSON files that Open Library returned. 

Now that I had my search results, I set about writing a Python script to read the JSON files, explore the data, and count the number of books that matched the keywords. Unfortunately, the query results weren't consistent. Some had a subject field while others didn't. Some results had the keyword in the author's name which is not what I wanted (if the only thing "Pumpkinheads" has in common with another book is that the word "Goat" was in the author's name, then that's not common enough for me). So filtering was necessary.

After my initial filtering, my querying produced about 1,400 books! There were some weird books, though. Like governmental reports on the quality of succotash or vampire sudoku or campfire coloring books. I didn't want those! So I made the decision to filter out all non-fiction books to make things easy. This dropped the total to 646 books. This list was written out to the file called "Scarathlon_PumpkinHeads_Dowry_of_Blood_Game1.txt". 

I went through this file and manually removed any duplicates (though my code removed the easy duplicates). The total dropped slightly to 635 books. This final list was saved to the file called "Scarathlon_PumpkinHeads_Dowry_of_Blood_Game1_FinalList.txt". 


# Conclusion

After all this I found, via Open Library and some Python programming, 635 books with things in common with both "Pumpkinheads" and "A Dowry of Blood". 635 books times 10 points per book is **6,350 points**!

This was a fun challenge! I look forward to more games/challenges where I can apply my programming skills.


## License
The Python script called "Open_Library_Scarathlon_Analysis.py" is licensed under the [MIT License](https://fossa.com/blog/open-source-licenses-101-mit-license/). Please feel free to view, download, modify, and distribute the code to your heart's content. 

Please feel free to check out the lists and the JSON files. You might find an interesting book in the lists! For the funnel cake keyword, I found a book called "The Fatal Funnel Cake: A Freshbaked Mystery" by Livia J. Washburn. I never thought I would find a mystery book about funnel cakes.



