# Update User

---

# This Endpoint Allows You To Update Users As You Wish

# Endpoint: https://apis.kah-moh.com/users/update/{userID}/

# METHOD: PUT

# Data:

- username
- email (must not being existed or taken)
- job_title
- national_id
- password
- is_admin

# NOTES:

## - If The Email Was Already Taken The Process Will Fail

## - If You Desire The User You're Updating To Be And Admin, set is_admin to `true`

# Responses:

## Success: will return a message indicates success

## Failure: will return a message indicates failure
