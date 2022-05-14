# restoremkc - Regenerate MegaKat City Blacknet Archives

The ['MegaKat City Blacknet' archive](https://fanlore.org/wiki/MKC_Blacknet) (or
mkcblacknet) was a 'Swat Kats' fanfiction website that operated in the early
2000s. The site is long gone, and while archive.org was able to take [some
snapshots](https://web.archive.org/web/20050206222836/http://swatkats.org/download/index.html),
they aren't easily browsable and many of the links are broken.

That's where this tool comes in. This tool downloads the entire site archive
from 2002, and updates all the HTML and links so it can easily be browsed on
your home computer! You can re-read all the old fics, with their 2000s
era-backgrounds!

## Running the tool

This tool requires python3 (which is preinstalled on Mac and Linux, but Windows
users [will need to download it](https://www.python.org/downloads/)).

*If you're unsure what to download, Python 3.9 is a good bet. Also, make sure to
check the 'Add to Path' option when installing.*

Once you have it, simply download this repo and run:

```
python restoremkc.py
```

Or, if you're on a Mac or Linux system:
```
python3 restoremkc.py
```

This will download all the files, patch them, and place them in a
folder called `mkcblacknet`. From there, you can use python's built
in web-server to view all the files locally! 

To do that, run these two commands once the tool is complete:
```
cd mkcblacknet
python -m http.server
```

(Mac/Linux users will need to run `python3` instead)

## Why?

Why did I build this? I confess, I'm not really a huge Swat Kats fan.

Well... a friend recommended the series to me, and I discovered there was still
a single fanfic website that was operating! It had hundreds of fics, and had
opened in the 90s! And then I read their policies: 'No depictions of gay allowed - 
it angers people and we don't want angry emails.'

I was stunned. While it should have been nothing, the fact that the only Swat
Kats fanfic site still active had a 'we care about homophobes not emailing us
more than we care about queer people existing', in the year 2022, felt like it
was the Swat Kats fandom saying, 'you, as a gay man, don't belong here.'

And then I found about about the old MKC Blacknet archives - there was queer-friendly
fanfic site, but it had been lost to time. So I wanted to make it
available to people, if only to say, hey, we do exist, even if that one site
pretends we don't.