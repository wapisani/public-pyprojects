# Week 2 - Word Finder
This week the challenge is to make as many words as you can from the phrase "Happy Halloween Scarathloners!". Once again, I will be attempting this challenge using my coding prowess.

### Finding a Digital Dictionary
It wasn't too hard finding a dictionary online that I could download. I found this [GitHub repository](https://github.com/matthewreagan/WebstersEnglishDictionary) that had a JSON file of Webster's Unabridged English Dictionary from 2009. I doubt the English language has added very many words since 2009, but I wanted a dataset as new as possible. Thankfully, this same GitHub repo provides a parsing script for the text file of the dictionary found on the [Gutenberg website](https://www.gutenberg.org/ebooks/29765).

### You Gotta Be Swift
The parsing script was written in Swift, Apple's primary programming language for mac OS and iOS. I've never written any Swift (yet, I plan to if I ever buy a Mac) nor run any, but I knew it was available for non-Apple platforms. So I found a [guide](https://itsfoss.com/use-swift-linux/) on downloading/installing Swift on Linux (via Windows Subsystem for Linux 2) and downloaded Swift.

I ran into some errors with line 245 in main.swift that took some figuring out (mostly trial-and-erroring since I have no experience with Swift), but I got it figured out. I replaced lines 245 - 248 with the following. I added the .sortedKeys option to sort the JSON file in alphabetical order. The JSON file is composed of words with their definitions.

```swift
try JSONSerialization.writeJSONObject(compiledDictionary,
                                      toStream: outputStream,
                                      options: [JSONSerialization.WritingOptions.prettyPrinted, JSONSerialization.WritingOptions.sortedKeys])
```
