# Create User

---

# This Endpoint Allows You To Create Users As You Wish, Also Allows You To Create Admin Users!

# Endpoint: http://apis.kah-moh.com/users/create/

# METHOD: POST

# Data:

- username
- email (must not being existed or taken)
- job_title
- national_id
- password
- is_admin

# NOTES:

## - If The Email Was Already Taken The Process Will Fail

## - If You Desire The User You're Creating To Be And Admin, set is_admin to `true`

# Responses:

## Success: will return a message indicates success

## Failure: will return a message indicates failure
