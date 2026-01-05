# Flask API and JSON Database

We're working with a "toy" API. You don't need to know the code, but if you're curious, well, give it a look-see.

Our routes (an abbreviated URL) look like this:

```
GET /user       -- returns a list of users as JSON
GET /user/12    -- returns a user as JSON
POST /user      -- submit a request with user JSON
PUT /user/12    -- update a user with an id
DELETE /user/12 -- delete a user with an id

GET /bug       -- returns a list of bugs as JSON
GET /bug/3     -- return a bug as JSON
POST /bug      -- submit a request with bug JSON
PUT /bug/13    -- update a bug with an id
DELETE /bug/13 -- delete a bug with an id
```

Our JSON database will look like this:

```json
{
  "user": [
    {
      "name": "Rainer Sarl",
      "email": "rsarl0@mashable.com",
      "id": 1
    },
    {
      "name": "Herve Wooff",
      "email": "hwooff1@unc.edu",
      "id": 2
    },
    {
      "name": "Lynette Couves",
      "email": "hlcouves2@cbsnews.com",
      "id": 3
    },
    {
      "name": "Fairlie Fergyson",
      "email": "ffergyson3@newyorker.com",
      "id": 4
    },
    {
      "name": "Ladonna Wilstead",
      "email": "lwilstead4@newsvine.com",
      "id": 5
    }
  ],
  "bug": [
    {
      "name": "Seven-Spotted Ladybug",
      "order": "Coleoptera",
      "id": 1
    },
    {
      "name": "Harlequin Ladybird",
      "order": "Coleoptera",
      "id": 2
    },
    {
      "name": "Red Wood Ant",
      "order": "Hymenoptera",
      "id": 3
    }
  ]
}
```

But there are no limits to the JSON resources we can create, read, update, and delete. It can be a meteorite fall, a dinosaur, a book, a financial record, etc.

```
GET /:resource         -- returns a list of resources as JSON
GET /:resource/:id     -- return a resource as JSON
POST /:resource        -- submit a request with a JSON resource
PUT /:resource/:id     -- update a resource with an id
DELETE /:resource/:id  -- delete a resource with an id
```

**Beware**: in our JSON resources, some attributes may not line up. There's no _schema_. Say we submit a user resource but it's a book, or a book is a bug, or a bug is a financial record. Our JSON database is not reliable. Use reliable data classes to match with resources.

## Prerequisites

1. Open a terminal.

2. Browse to `dev10-classwork/week-02/assessment/server`.

3. Create a virtual environment:

    ```sh
    server $ python -m venv .
    ```

4. Activate it.

5. Install [Flask](https://pypi.org/project/Flask/).

    ```sh
    (server) server $ pip install Flask
    ```

## Run

We will want to use an independent terminal since we can't run a client and server at the same time.

1. Browse to `dev10-classwork/week-02/assessment/server`.

2. If we haven't already, activate our `(server)` virtual environment.

3. Run it!

    ```sh
    (server) server % python main.py 
    * Serving Flask app 'main'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 667-490-503
    ```

4. At any time, press CTRL+C to shut down the server.