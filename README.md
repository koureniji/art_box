# klasse_box

klasse_box reads source.json containing artists, styles, moods, and "Zuerauer Aphorisms" in german and english. On <spacebar> press it generates a new DALL-E 2 picture based on the database.

## TODO
  - add DOCUMENTATION!!
  - Display() // App()
  - paper implementation
  - button implementation
  - gpt abstraction of "text" for prompt
  

## How prompt generation works

klasse_box takes a random aphorism w/ random artist, tech & mood from source.json and combines it into a DALL-E prompt. e.g.:
    
    tech: pixel-art
    artist: Victor Vasarely
    mood: depressed
    text: A belief is like a guillotine, just as heavy, just as light.
    
    -> prompt: "A pixel-art in depressed style of Victor Vasarely depicting: "A belief is like a guillotine, just as heavy, just as light.""
 
 OR:
    
    tech: ... painting
    artist: ... Claude Monet
    mood: ... satanic
    text: ... When one has once accepted and absorbed Evil, it no longer demands to be believed.
    
    -> prompt: "A painting in satanic style of Claude Monet depicting: "When one has once accepted and absorbed Evil, it no longer demands to be believed.""
