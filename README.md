<h1 align="center">Flight Tracker ✈︎</h1>

<h4 align="center">Get the current location of any plane located on a map</h4>
  <p align="center">
  </p>

# 💬 About:

Using the <a href="https://">OpenSky Network API</a> 

There is one caveat tho, some of PushShift shards (think of them as servers) are sometimes down,
so you might not get the whole data in those cases. However, you're probably getting more than with Reddit's api, so it's worth it 😁  

# ✨ Features:
* 🖼️ Download directly linked images and gifs from any public subreddit.
* 🎞️ Download directly linked videos from any public subreddit.
* 📅 Download files before and/or after a certain date.

# 🔧 Setup:
Install the dependencies:

`python -m pip install -r requirements.txt`

Fill in the `config.ini` file as needed. There you can set:
    
* Subreddit you'll download your media from.
* Destination folder. 
* Posts time frame (optional).


# 🖥️ Usage:
Simply run the file `main.py` and it will start downloading.

 ![run_example](img/00.jpg)

# 📚 Dependencies:
* [**PSAW**](https://github.com/dmarx/psaw): Pushshift.io API Wrapper.
* [**tqdm**](https://github.com/tqdm/tqdm): Progressbar.
* [**aiohttp**](https://github.com/aio-libs/aiohttp): Async http client/server framework.
* [**aiofiles**](https://github.com/Tinche/aiofiles): File support for asyncio.


# 📃 License:
[GNU General Public License v3.0](LICENSE).
