# Regex
## import re
    pattern re.compile()
    patter.search()
             match()
             findall()

# symbols
    \n \r \t \0 \d \D
    \s(any white character) 
    \S(non-white space character)
    \w word character (a-z,A-Z,0-9)
    \W
    \b - Word Boundary

    Character
        Match - [abc] --  Any Character from a set of given Characters 
        NoMatch - [^abc]    No Character from  a set of given characters 
        Range   [a-z][a-zA-Z][0-9]
        Not from Range [^a-z]
        LettersAndNumbers        [[:alnum:]]
        Letters [[:alpha]] [[:lower/upper:]]
        digits [[:digt:]] [[:xdigit]]
        Ascii [[:ascii]]
        Space/Tab [[:blank:]] /[[:space:]]
        Control Characters [[:cntrl:]]/ [[:punct:]]
        Visible characters [[:graph:]]
    MetaCharacters

        . ^ $ * + ? { } [ ] \ | ( )

## Quantifiers
        * - O or more characters
        + - 1 or more characters
        ? - 0 or 1 chracter
        {3}  exact number of characters
        {3,6} min 3 and max 6
    
        . Any Character 
        ^ Begining of line
        $ end of String/line
        () Group
        | or






    
