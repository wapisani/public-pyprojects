# Week 2 - Word Finder
This week the challenge is to make as many words as you can from the phrase "Happy Halloween Scarathloners!". Once again, I will be attempting this challenge using my coding prowess.

### Finding a Digital Dictionary
It wasn't too hard finding a dictionary online that I could download. I found this [GitHub repository](https://github.com/matthewreagan/WebstersEnglishDictionary) that had a JSON file of Webster's Unabridged English Dictionary from 2009. I doubt the English language has added very many words since 2009, but I wanted a dataset as new as possible. Thankfully, this same GitHub repo provides a parsing script for the text file of the dictionary found on the [Gutenberg website](https://www.gutenberg.org/ebooks/29765) (which has been updated since 2009).

### You Gotta Be Swift
The parsing script was written in Swift, Apple's primary programming language for macOS and iOS. I've never written any Swift (yet, I plan to if I ever buy a Mac) nor run any, but I knew it was available for non-Apple platforms. So I found a [guide](https://itsfoss.com/use-swift-linux/) on downloading/installing Swift on Linux (via Windows Subsystem for Linux 2) and downloaded Swift.

I ran into some errors with line 245 in main.swift that took some figuring out (mostly trial-and-erroring since I have no experience with Swift), but I got it figured out. I replaced lines 245 - 248 with the following. I added the .sortedKeys option to sort the JSON file in alphabetical order. The JSON file is composed of a dictionary of words with their definitions.

```swift
try JSONSerialization.writeJSONObject(compiledDictionary,
                                      toStream: outputStream,
                                      options: [JSONSerialization.WritingOptions.prettyPrinted, JSONSerialization.WritingOptions.sortedKeys])
```

Now that I have the up-to-date (as of January 2023) Webster's Unabridged Dictionary as a JSON file I can get going on my Python script.

### That's a lot of points!

There are 102,106 words in the JSON dictionary. How many of those can be made from the letters in this year's phrase? It turns out that 5,795 different words can be made from the letters in the phrase. So that would be 57,950 points!

The words that can be made from the phrase may be seen in the text file called "found_words_webster.txt".

### Wow, some of these words are ancient!

This copy of the Webster's Unabridged Dictionary is from 1913 because that version is in the public domain. So it makes sense that some of the words are out of date now.

### Maybe you should find a more up-to-date dictionary

I went back on the Internet and found an open-source dictionary called [Wordset](https://github.com/wordset/wordset-dictionary) that appears to have been put together from 2015 to 2017. This dictionary is available as 27 different JSON files, one for each letter and one for miscellaneous things like emoji. I concatenated the 26 JSON files, but only included the words to save space. 

### That's STILL a lot of points!

The Wordset dictionary contains 108,124 words (not including the miscellaneous things such as emojis) and my code found that 3,653 words can be formed from the letters in the phrase "Happy Halloween Scarathloners!". So that would be 36,530 points! Not as many as before, but I'd say that this time the results are reflective of our time period (and thus more fair). The list of words may be seen in "found_words_wordset.txt". 

### License

All of my Python code and the text files are licensed under the [MIT License](https://fossa.com/blog/open-source-licenses-101-mit-license/).
