<h1 align="center">Flight Tracker ✈︎</h1>

<h4 align="center">Get the current location of any plane located on a map</h4>
  <p align="center">
  </p>

# 💬 About:

Every 10 seconds a call is made to the <a href="https://">OpenSky Network API</a> to retrive to longitude and latitude of the plane you are tracking. It then uses folium to plot those points on a map. 

# 🔧 Setup:
Install the dependencies:

`python -m pip install -r requirements.txt`

# 🖥️ Usage:
Simply run the file `run.py` and the website and traker will start.

 ![run_example](img/00.jpg)

# 📚 Dependencies:
* [**PSAW**](https://github.com/dmarx/psaw): Pushshift.io API Wrapper.
* [**tqdm**](https://github.com/tqdm/tqdm): Progressbar.
* [**aiohttp**](https://github.com/aio-libs/aiohttp): Async http client/server framework.
* [**aiofiles**](https://github.com/Tinche/aiofiles): File support for asyncio.


# 📃 License:
[GNU General Public License v3.0](LICENSE).
