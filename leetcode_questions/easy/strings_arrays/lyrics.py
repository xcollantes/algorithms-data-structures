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
        lyrics(lyrics="plays under the moon dog", band_name="sun")
        == "plays\nunder\nthe moon dog"
    )


def lyrics(lyrics, band_name):
    """
    "hello plays under the moon dog"
                            w

    "sun"
       c

    line = hello plays
    line = under
    line = the moon


    res =
        hello plays
        under

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

    # lyrics = lyrics.split(" ")

    # lines = []
    # curline = ""

    # c = 0

    # for word in range(lyrics):

    #     print(f"c: {band_name[c]} w: {word}")

    #     if band_name[c] in word:

    #         # flush cache
    #         lines.append(curline)
    #         curline = ""

    #         c += 1
    #     else:
    #         curline +=

    #         res += word

    # res = "\n".join(lines)
    # print(f"res: {res}")
    # return res


# def lyrics(lyrics, band_name):
#     """
#     Creates an album cover by aligning lyrics horizontally with band name running vertically.
#     Each line of the result contains a word from the lyrics that has a letter from the band name.

#     Args:
#         lyrics: String containing song lyrics
#         band_name: String containing the band name

#     Returns:
#         String with formatted lyrics for the album cover
#     """
#     # Parse the input
#     words = lyrics.split()

#     # Find words that contain each character of the band name
#     matching_indices = []
#     band_idx = 0

#     # For each character in the band name, find the first word that contains it
#     for i, word in enumerate(words):
#         if band_idx < len(band_name) and band_name[band_idx] in word:
#             matching_indices.append(i)
#             band_idx += 1

#             # If we've matched all characters in the band name, we're done
#             if band_idx >= len(band_name):
#                 break

#     # If we didn't match all characters, return empty string
#     if band_idx < len(band_name):
#         return ""

#     # Build the result
#     result = []
#     start_idx = matching_indices[0]
#     end_idx = matching_indices[-1]

#     # For each matching index, create a line that includes all words up to the next matching index
#     for i in range(len(matching_indices)):
#         current_idx = matching_indices[i]

#         # Determine the end of this line
#         next_idx = matching_indices[i + 1] if i + 1 < len(matching_indices) else end_idx + 1

#         # Build the line
#         line = " ".join(words[current_idx:next_idx]) + " "
#         result.append(line)

#     # Join the lines with newlines
#     res = "\n".join(result)
#     print(res)
#     return res
