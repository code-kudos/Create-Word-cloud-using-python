# Hi, I'm code kudos.
## Create a Word Cloud using numpy & wordcloud library in python
### Hope you like it!!!!
#### To see more like this Subscribe to 
##### Youtube: @codekudos
###### Instagram: @codekudos
####### Twitter: @code_kudos

import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

text = open('case.txt', mode='r', encoding='utf-8').read()
sw = STOPWORDS
mask = np.array(Image.open('sh.png'))


wc = WordCloud(
    background_color='white',
    height=600,
    width=450,
    stopwords=sw,
    mask=mask
)

wc.generate(text)

wc.to_file('output.png')