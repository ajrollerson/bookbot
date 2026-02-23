Bookbot.

‘Bookbot’ is a python-centric programme that counts the words and characters in text files. This was a guided project hosted by boot.dev.

Features:
•	 Character count (Unicode-supported).
•	 Word count (whitespace-delimited languages).
•    Estimated reading time based on user-supplied or default words-per-minute, with basic error handling (personal addition).
•	 Case-insensitive processing.
•	 Command-line interface.

 Language handling.
•	Bookbot can correctly parse the number of characters and words in any text. 
•	When tested with other languages, it can also correctly count the number of characters.

Limitations.
•	Bookbot can correctly separate ‘characters’ with no fuss in any language, but ignores the nuances in languages such as Chinese (simplified) and Japanese, where a single character can also be a word.
•	Word-count doesn’t apply well to languages like Japanese or Hindi, where white space is typically used between whole sentences instead of words.
•	Bookbot does not currently include a language detection feature, so it treats all text as English-centric.
Possible future improvements.
•	Adding language modules, which can parse texts from certain languages appropriately, like Chinese, Japanese, Hindi, etc…, which can identify ‘words’ more accurately.  

Usage:
• Navigate to the ‘bookbot’ directory.
• Run the programme with ‘python3 main.py <file_path> [wpm]’.
• Note: if no valid WPM argument is provided, a default value of 250 will be used.
• Current books can be found in ‘books’, while test documents for other languages can be found in ‘testbooks’.

Examples:
‘python3 main.py books/prideandprejudice.txt’
‘python3 main.py testbooks/examplejapanese.txt’

Key lessons/insights:
•	Learnt that code and functions should be piped/imported in a single direction, not imported reciprocally, creating circular dependencies.
•	Finally clarified my understanding regarding function calling and returns: in the sense that the ‘returns make information available to the ‘caller’ of the function, means the code is the caller.
•	That modularity is more useful for scalability, as it will enable features to be developed more quickly, rather than having to rewrite and restructure code each time.
•	Developed a better understanding of handling Unicode text.
•   Developed familiarity with Python’s 'sys' module for command-line argument handling.

