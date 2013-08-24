Simularity
======

Project Goal:

    1. Consume Twitter Sample Stream
    2. Apply some AI/Magic
    3. Create an algorithm + dataset that can predict similar hashtags based on 
       hashtags the algo has seen before.

Pre-Flight Checklist
======

autoenv
---

[kennethreitz/autoenv](https://github.com/kennethreitz/autoenv)

For use with virtualenv, will automatically load the appropriate environment
vars from your .env file (see Twitter API Credentials, below).  Install it
on your system python.

virtualenv
---

I recommend using virtualenv and virtualenv wrapper:

    $ mkvirtualenv simularity

Then in subsequent sessions:

    $ workon simularity


Installing Dependencies
---

The app has been tested against python 2.7.

    $ pip install -r requirements.txt



Twitter API Credentials
---

Go to [https://dev.twitter.com/](https://dev.twitter.com/) and create a
new application and access token.

Plug those values into a file at the top level called `.env` by copying
`.env-example` and replacing the empty strings with the appropriate values.

If you use autoenv, then these values will automatically get loaded into
your environment.  If you're not using autoenv, just use `source .env` at
the beginning of your terminal session.



Train
======

To train the brain, run `python trainer.py`.  This will hit the twitter sample
real time stream and begin inserting lists of hashtags into the brain.


Terminal Usage
======

Right now there's no web service API, so to view the most "similar" hastag
based on the consumed twitter data, run:

    $ python brain somehashtagnamehere

And the app will print out the hashtag.

Test Suite
======

This app uses `nosetests` as the test suite bootstrapper.  To run the tests, run:

    $ nosetests

