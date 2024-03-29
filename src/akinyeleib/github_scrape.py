from bs4 import BeautifulSoup as bs
import requests as rq
from requests.exceptions import ConnectionError


# Function to fetch users

class GitHub:

    '''
    class: GitHub
    
    Reads github account information including: 
    public repositories
    followers
    followings

    Attributes
    ----------
        username : str
            github account username
        repos : list
            public repositories
        details : dict
            all account info
        fullName : str
            stores account holder's name as it is on the account

    Methods
    -------

        getRepos() -> List
        getDetails() -> List
        getUserName() -> List
        getFollowing() -> List
        getFollowers() -> List
        getFollowersCount() -> List
        getFollowingCount() -> List
        getFollowingNotFollowers() -> List
        getFollowersNotFollowing() -> List
        find_difference(self, list1, list2) -> List

    '''

    def __init__(self, username='akinyeleib'):

        '''
        Loads all the necessary methods for the account 
        by calling necessary methods on the object.

        Parameters
        ----------
            username : str, optional
            If the argument "username" is passed, 
            it takes the value, else, the default value is taken!

        '''

        self.username = username.strip()
        self.repos = None
        self.details = None
        self.fullName = None
        
        try:
            res = rq.get(f'https://github.com/{username}')

            soup = bs(res.text, 'lxml')

            item = soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden')
            self.fullName = item.text.strip()
            
            print(f'Hello {self.fullName}')

            # Retrieve status
            status = res.status_code
            if status == 200:
                self.check_repo()
                self.loader()
            elif status == 404:
                print(f'404 bad request\nPage not found!\nAccount not found for user: {username}')
                self.username = None
                return None
        
        except ConnectionError as e:
            print('Connection error...' + str(e))

    
    # Function to fetch users

    def github_follow(self, context):
        try:
            soup = bs(rq.get(f"https://github.com/{self.username}?tab={context}").text, 'lxml')
            items = soup.find_all("span", class_="Link--secondary")
            
            users = []
            for item in items:
                users.append(item.text)
            return users
        
        except ConnectionError as e:
            print('Connection error...' + str(e))
    
    
    # Finding Difference and Intersect

    def find_difference(self, list1, list2):
        result = []
        for name in list1:
            if name not in list2:
                result.append(name)
        return result


    def loader(self):

        self.details = {}
        print(f'Account found for user: {self.username}')
        
        self.details['repos'] = self.repos
        print(f'{self.username} has {len(self.repos)} repositories')
        
        followers = self.github_follow("followers")
        self.details['followers'] = followers

        followers_count = len(followers)
        self.details['followers_count'] = followers_count
        print(f'{self.username} has {followers_count} followers')
        
        following = self.github_follow("following")
        self.details['following'] = following

        following_count = len(following)
        self.details['following_count'] = following_count
        print(f'{self.username} is following {following_count} user(s)')
        
        following_not_followers = self.find_difference(following, followers)
        self.details['following_not_followers'] = following_not_followers

        following_not_followers_count = len(following_not_followers)
        self.details['following_not_followers_count'] = following_not_followers_count
        print(f'{self.username} has {following_not_followers_count} user(s) not following back')
        
        followers_not_following = self.find_difference(followers, following)
        self.details['followers_not_following'] = followers_not_following

        followers_not_following_count = len(followers_not_following)
        self.details['followers_not_following_count'] = followers_not_following_count
        print(f'{self.username} is not following {followers_not_following_count} user(s) back')
        

    def check_repo(self):
        link = f"https://github.com/{self.username}?tab=repositories"
       

        try:
            req = bs(rq.get(link).text, 'lxml')
            items = req.find_all('h3', class_="wb-break-all")
        
            self.repos = []
            for item in items:
                a = item.find('a')
                self.repos.append(a.text.strip())

        except ConnectionError as e:
            print('Connection error...' + str(e))


    # Getters

    def getUserName(self):
        return self.username


    def getRepos(self):
        return self.repos
    

    def getDetails(self):
        return self.details


    def getFollowers(self):
        return self.details['followers']    
    

    def getFollowing(self):
        return self.details['following']
    

    def getFollowersCount(self):
        return self.details['followers_count']
    

    def getFollowingCount(self):
        return self.details['following_count']
    

    def getFollowingNotFollowers(self):
        return self.details['following_not_followers']
    

    def getFollowersNotFollowing(self):
        return self.details['followers_not_following']
    

