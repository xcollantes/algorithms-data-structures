"""Example problem:

Assume for a moment that we're a part of a record company and the marketing
department has an idea for a new album cover. They want to mix a subset of the
lyrics from a song with the band name to create an interesting cover.
Specifically, the lyrics should be aligned horizontally with the band name
running vertically.

For example, if the values for part of the song and band are below: song_lyrics
= '...plays under the moon...' band_name = 'sun'

A possible result for a cover would be:

plays
under the
moon

Core Requirements: • The cover solution should begin with the first matching
word and end with the last matching word from the available lyrics • All words
in between should be included in the solution • Words should be kept whole, ie a
word should not be split between two lines • Only alpha-numeric characters
should be present in the solution • The existing unit test
test_creative_song_lyrics should pass unaltered
"""


def test_lyrics():
    """pytest lyrics.py"""
    assert (
        lyrics(lyrics="plays under the moon", band_name="sun")
        == "plays \nunder the \nmoon "
    )


def lyrics(lyrics, band_name):
    """
    "plays under the moon"
                 w

    "sun"
      c

    curstr =
    res =
        plays
        under the
        moon
    """
    lyrics = lyrics.split(" ")

    res = ""

    c = 0
    w = 0

    while c < len(band_name) and w < len(lyrics):

        print(f"c: {band_name[c]} w: {lyrics[w]}")

        if band_name[c] in lyrics[w]:
            if res:
                res += "\n"
            c += 1

        res += lyrics[w] + " "

        w += 1

    print(f"res: {res}")
    return res
