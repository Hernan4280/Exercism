def recite(start_verse, end_verse):
    phrases = [
        ("house that Jack built", ""),
        ("malt", "that lay in"),
        ("rat", "that ate"),
        ("cat", "that killed"),
        ("dog", "that worried"),
        ("cow with the crumpled horn", "that tossed"),
        ("maiden all forlorn", "that milked"),
        ("man all tattered and torn", "that kissed"),
        ("priest all shaven and shorn", "that married"),
        ("rooster that crowed in the morn", "that woke"),
        ("farmer sowing his corn", "that kept"),
        ("horse and the hound and the horn", "that belonged to")
    ]
    
    verses = []
    for i in range(start_verse - 1, end_verse):
        
        verse_parts = [f"This is the {phrases[i][0]}"]
        for j in range(i, 0, -1):
            verse_parts.append(f"{phrases[j][1]} the {phrases[j - 1][0]}")
        
        verses.append(" ".join(verse_parts) + ".")
        
    return verses
