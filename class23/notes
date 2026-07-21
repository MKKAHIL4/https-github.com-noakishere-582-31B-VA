## Authentication and user accounts in Flask

### Authentication vs Authorization

Authentication means : is the user logged in?

Authorization means: is the user allowed to do an action. (edit, view, etc.)

### Terminology

Password hashing: A one-way representation of a password.(to hide)
-session : Data used to remember between requests
    -a remporary, server-side record of a user interaction with a website.

-protected route: A route that requires Authentication

-Flash message: A temporrary message displayed after an action(usually a request)

-unique constraint: a database rule preventing duplicate values.

-credential: Information used to prove identity.

Request1 : POST/ LOGIN

--> Credentials verified(username, password is verified)
--> useir ID is stored in session 


--> request2: GET/ dashboard
--> Session identifies the member (member associated with the content )
--> currrent_user () from session) contains the member etc, etc,
### passwords and thy they shouldnt be stored directly

When the user registers, if we store their password directly in the database (like Password123 for
example), in case of a database exposure or exploit, every password becomes immediatebly readable.

We want to store a password hash:

i.e .: Password 123 -- > scrypt:3247574279:8.1$ (not real)

A hash is designed to be one-way. The application cannot decrypt it.