# github-scrape

### About

Scrapes github pages for a specified user,
displays a report about the user's current account status.

The report contains:
- [x] Number of followers
- [x] Number of users being followed
- [x] Number of users following but not following back
- [x] Opposite of '3.'
- [x] Check number of repositories
- [x] List repositories


## Installation
For first time installation:
'''
pip install github-scrape
'''

For recurring installation/update:
'''
pip install github-scrape --upgrade
'''

## Usage

To use the package, you have to import using:
`from akinyeleib import work`

The function needed in the package is 
`work.check()`

You can as well as use alias:
```
from akinyeleib import work as ib
ib.check()
```

The check() which returns a dictionary object
`result = ib.check()`

We can then perform a runtime check on the object:
`print(type(result))`

### Thank you.
