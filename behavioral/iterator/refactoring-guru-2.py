"""
Iterator is a behavioral design pattern that
allows sequential traversal through a complex
data structure without exposing its internal
details.

Thanks for the Iterator, clients go over elements
of different collections in a similar fashion
using a single iterator interface.
"""
from time import sleep
from typing import List, Dict


class ProfileIteratorInterface:
    """ Defines profile interface """

    def has_next(self) -> bool: raise NotImplementedError()
    def get_next(self) -> "Profile": raise NotImplementedError()
    def reset(self) -> None: raise NotImplementedError()


class FacebookIterator(ProfileIteratorInterface):
    """ Implements iteration over Facebook profiles """

    def __init__(self, facebook: "Facebook", type_: str, email: str) -> None:
        self._facebook = facebook
        self._type = type_
        self._email = email

        self._current_position: int = 0
        self._emails: List[str] = []
        self._profiles: List[Profile] = []

    def lazy_load(self) -> None:
        if not self._emails:
            _emails_from_facebook: List[str] = self._facebook.request_profile_email_friends(self._email, self._type)
            for email in _emails_from_facebook:
                self._emails.append(email)
                self._profiles.append(None)

    def has_next(self) -> bool:
        self.lazy_load()
        return self._current_position < len(self._emails)
    
    def get_next(self) -> "Profile":
        if not self.has_next():
            return None
        
        _friend_email: str = self._emails[self._current_position]
        _friend_profile: Profile = self._profiles[self._current_position]

        if not _friend_profile:
            _friend_profile = self._facebook.request_profile(_friend_email)
            self._profiles[self._current_position] = _friend_profile

        self._current_position += 1
        return _friend_profile

    def reset(self) -> None:
        self._current_position = 0


class LinkedInIterator(ProfileIteratorInterface):
    """ Implements iteration over LinkedIn profiles """

    def __init__(self, linkedin: "LinkedIn", type_: str, email: str) -> None:
        self._linkedin = linkedin
        self._type = type_
        self._email = email

        self._current_position: int = 0
        self._emails: List[str] = []
        self._profiles: List[Profile] = []

    def lazy_load(self) -> None:
        if not self._emails:
            _emails_from_linkedin: List[str] = self._linkedin.request_related_email_contacts(self._email, self._type)
            for email in _emails_from_linkedin:
                self._emails.append(email)
                self._profiles.append(None)

    def has_next(self) -> bool:
        self.lazy_load()
        return self._current_position < len(self._emails)
    
    def get_next(self) -> "Profile":
        if not self.has_next():
            return None
    
        _contact_email: str = self._emails[self._current_position]
        _contact_profile = self._profiles[self._current_position]

        if not _contact_profile:
            _contact_profile: Profile = self._linkedin.request_contact(_contact_email)
            self._profiles[self._current_position] = _contact_profile

        self._current_position += 1
        return _contact_profile
    
    def reset(self) -> None:
        self._current_position = 0


class SocialNetworkInterface:
    """ Defines common social network interface """

    def create_friends_iterator(self, profile_email: str) -> ProfileIteratorInterface: raise NotImplementedError()
    def create_coworkers_iterator(self, profile_email: str) -> ProfileIteratorInterface: raise NotImplementedError()


class Facebook(SocialNetworkInterface):

    def __init__(self, cache: List["Profile"]) -> None:
        if cache:
            self._profiles: List[Profile] = cache
        else:
            self._profiles: List[Profile] = []


    def request_profile(self, friend_email: str) -> "Profile":
        """
        Here would be a POST request to one of the Facebook API endpoints.
        Instead, we emulates long network connection, which you would expect
        in real life...
        """
        self.simulate_network_latency()
        print(f'Facebook: Loading profile {friend_email} over the network...')

        return self.find_profile(friend_email)

    def request_profile_email_friends(self, profile_email: str, contact_type: str) -> List[str]:
        """
        Here we would be a POST request to one of the Facebook API endpoints.
        Instead, we emulate network latency connection, which you would expect
        in real life...
        """
        self.simulate_network_latency()
        print(f'Facebook: Loading "{contact_type}" list of "{profile_email}" over the network...')

        _profile: Profile = self.find_profile(profile_email)
        if _profile:
            return _profile.get_contacts(contact_type)
        return None

    def find_profile(self, friend_email: str) -> "Profile":
        for profile in self._profiles:
            if profile.get_email() == friend_email:
                return profile
        return None

    def simulate_network_latency(self):
        sleep(2.5)

    def create_friends_iterator(self, profile_email: str) -> ProfileIteratorInterface:
        return FacebookIterator(self, 'friends', profile_email)

    def create_coworkers_iterator(self, profile_email: str) -> ProfileIteratorInterface:
        return FacebookIterator(self, 'coworkers', profile_email)


class LinkedIn(SocialNetworkInterface):

    def __init__(self, cache: List["Profile"]) -> None:
        if cache:
            self._contacts: List[Profile] = cache
        else:
            self._contacts: List[Profile] = []

    def request_contact(self, contact_email: str) -> "Profile":
        """
        Here we would be a POST request to one of the LinkedIn API endpoints.
        Instead, we emulates long network connection, which you would expect
        in the real life...
        """
        self.simulate_network_latency()
        print(f'LinkedIn: Loading profile "{contact_email}" over the network...')

        return self.find_contact(contact_email)

    def request_related_email_contacts(self, contact_email: str, contact_type: str) -> List[str]:
        """
        Here we would be a POST request to one of the LinkedIn API endpoints.
        Instead, we emulates long network connection, which you would expect
        in the real life...
        """
        self.simulate_network_latency()
        print(f'LinkedIn: Loading "{contact_type}" list of {contact_email} over the network...')

        _profile: Profile = self.find_contact(contact_email)
        if _profile:
            return _profile.get_contacts(contact_type)
        return None

    def find_contact(self, contact_email: str) -> "Profile":
        for profile in self._contacts:
            if profile.get_email() == contact_email:
                return profile
        return None

    def simulate_network_latency(self) -> None:
        sleep(2.5)

    def create_friends_iterator(self, profile_email: str) -> ProfileIteratorInterface:
        return LinkedInIterator(self, 'friends', profile_email)

    def create_coworkers_iterator(self, profile_email: str) -> ProfileIteratorInterface:
        return LinkedInIterator(self, 'coworkers', profile_email)


class Profile:

    def __init__(self, email: str, name: str, *contacts: str) -> None:
        self._email = email
        self._name = name
        self._contacts: Dict[str, List[str]] = {}

        # Parse contact list from a set of "friend:email@gmail.com" pairs.
        for contact in contacts:
            _parts: str = contact.split(':')
            _contact_type: str = 'friends'

            if len(_parts) == 1:
                _contact_email = _parts[0]
            else:
                _contact_type = _parts[0]
                _contact_email = _parts[1]

            if _contact_type not in self._contacts:
                self._contacts[_contact_type] = []
            
            self._contacts[_contact_type].append(_contact_email)

    def get_email(self) -> str:
        return self._email

    def get_contacts(self, contact_type: str) -> List[str]:
        if contact_type not in self._contacts:
            self._contacts[contact_type] = []

        return self._contacts[contact_type]


class SocialSpammer:
    """
    Message sending app.
    """

    def __init__(self, network: SocialNetworkInterface) -> None:
        self._network = network
        self._profile_iterator: ProfileIteratorInterface = None

    def send_span_to_friends(self, profile_email: str, message: str) -> None:
        print('\n Iterating over friends...\n')
        self._profile_iterator = self._network.create_friends_iterator(profile_email)
        while self._profile_iterator.has_next():
            _profile: Profile = self._profile_iterator.get_next()
            self.send_message(_profile.get_email(), message)

    def send_span_to_coworkers(self, profile_email: str, message: str) -> None:
        print('\n Iterating over coworkers...\n')
        self._profile_iterator = self._network.create_coworkers_iterator(profile_email)
        while self._profile_iterator.has_next():
            _profile: Profile = self._profile_iterator.get_next()
            self.send_message(_profile.get_email(), message)


    def send_message(self, email: str, message: str) -> None:
        print(f'Sent message to: {email}. Message body: {message}')


class Demo:
    """ Demo class. Everything comes together here. """
    
    def run(self) -> None:
        print('Please specify social network to target spam tool (default:Facebook)')
        print('1 - Facebook')
        print('2 - LinkedIn')
        _choice: int = int(input('Please make your choice: '))
        if _choice == 2:
            _network: SocialNetworkInterface = LinkedIn(self.create_test_profiles())
        else:
            _network: SocialNetworkInterface = Facebook(self.create_test_profiles())
        
        _spammer = SocialSpammer(_network)

        _spammer.send_span_to_friends(
            "anna.smith@bing.com",
            "Hey! This is Anna's friend Josh. Can you do me a favor and like this post [link]?"
        )
        _spammer.send_span_to_coworkers(
            "anna.smith@bing.com",
            "Hey! This is Anna's boss Jason. Anna told me you would be interested in [link]."
        )

    def create_test_profiles(self) -> List[Profile]:
        _profile_data: List[Profile] = []
        _profile_data.append(Profile(
            'anna.smith@bing.com',
            'Anna Smith',
            'friends:mad_max@ya.com',
            'friends:catwoman@yahoo.com',
            'coworkers:sam@amazon.com',
        ))
        _profile_data.append(Profile(
            'mad_max@ya.com',
            'Maximilian',
            'friends:anna.smith@bing.com',
            'coworkers:sam@amazon.com',
        ))
        _profile_data.append(Profile(
            'bill@microsoft.eu',
            'Billie',
            'coworkers:avanger@ukr.net',
        ))
        _profile_data.append(Profile(
            'avanger@ukr.net',
            'Jonh Day',
            'coworkers:bill@microsoft.eu',
        ))
        _profile_data.append(Profile(
            'sam@amazon.com',
            'Sam Kitting',
            'coworkers:anna.smith@bing.com',
            'coworkers:mad_max@ya.com',
            'friends:catwoman@yahoo.com',
        ))
        _profile_data.append(Profile(
            'catwoman@yahoo.com',
            'Liza',
            'friends:anna.smith@bing.com',
            'friends:sam@amazon.com',
        ))

        return _profile_data


demo: Demo = Demo()
demo.run()