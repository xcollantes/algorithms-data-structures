"""
# **Problem: Album Cover Acrostic Generator**

## **Scenario**

You work at a record company where the marketing department wants you to
generate album covers from song lyrics and band names.  The song lyrics should
be aligned **horizontally**, while the band name runs **vertically** as an
**acrostic**.

Your goal is to extract the portion of the lyrics that includes all words
between the first and last letters of the band name found within the lyrics.

## **Example**

### **Input**

``` song_lyrics = "...plays under the moon..." band_name = "sun" ```

### **Output**

```
plays
    under the
 moon
```

### **Explanation**

* The vertical alignment of the letters **S**, **U**, and **N** in **“sun”**
  corresponds to words in the lyrics.
* The words between the first and last matching letters are included without
  breaking any words.
* The lyrics are formatted so that each subsequent letter of the band name
  aligns vertically.

## **Requirements**

1. The cover solution should **begin with the first matching word** and **end
   with the last matching word** from the available lyrics.
2. All words **in between** must be included in the solution.
3. Words must remain **whole** (no word splitting across lines).
4. Only **alphanumeric characters** should be present in the final output.
5. The existing unit test `test_creative_song_lyrics` must pass without
   modification.

## **Guidelines**

* You may add code in any of the following files:

  * `main.py`
  * `helper.py`
  * `test.py`
* Include **in-line documentation and comments** as if you were collaborating on
  a team project.
* Consider how **different inputs and outputs** might affect your code.
* Think carefully about **edge cases**, such as missing letters or special
  characters in lyrics.


## **Constraints**

* The `song_lyrics` string may contain punctuation and spaces.
* The `band_name` will contain only alphabetic characters.
* Case sensitivity should be ignored (e.g., “Sun” and “sun” are equivalent).
* The output must preserve the **horizontal alignment** of lyrics and the
  **vertical alignment** of the band name.

Would you like me to add a **Python function signature and starter code** (like
a LeetCode boilerplate with `def generate_album_cover(song_lyrics,
band_name):`)?
"""


def test_lyrics():
    """pytest lyrics.py"""
    assert lyrics(lyrics="plays under the moon", band_name="sun") == [
        "plays",
        "under the",
        "moon",
    ]


def lyrics(lyrics, band_name):
    """
    "hello plays under the moon dog"
                            w

    "sun"
       c

    line = hello plays line = under line = the moon


    res =
        hello plays under

    """

    c = 0
    line = []
    res = []

    for word in lyrics.split(" "):

        print(f"word: {word}")

        # add rest
        if c == len(band_name):
            print(f"    append ending: {word}")
            res[-1] += " " + word  # add to last element

        else:

            line.append(word)

            if band_name[c] in word:

                # add to line

                res.append(" ".join(line))

                # reset line
                line = []

                # push to res
                c += 1

        print(f"    {res}")

    print(f"res: {res}")
    res = "\n".join(res)
    return res
