# Imports
import requests

from contextlib import closing

from time import time


# Author and licensing
__Author__      =       "b-mcg"
__Email__       =       "bmcg0890@gmail.com"
__License__     =       """
Copyright (C) 2014-2016  b-mcg   <bmcg0890@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

# Version number
VERSION         =       'v0.0.1'




class Py3status(object):
    """
    Uses requests module to
    fetch IPv4 address from
    https://ipv4.icanhazip.com
    and outputs it to i3bar.

    """
    def __init__(self):
        """
        Sets url and ip attributes.

        """
        self.url        =       'https://ipv4.icanhazip.com/'

        # Send GET request to icanhazip and close the connection after ip attribute is set
        # SSL verification is set to False because the cert is for www.icanhazip.com
        try:

            with closing(requests.get(self.url, verify=False)) as res:
                self.ip         =       res.content.strip()
                self.success    =       True

        except:
            self.success        =       False

    def public(self, i3status_output_json, i3status_config):
        """
        Sets necessary response
        key/value pairs and returns
        them along with its position
        in i3bar.

        """
        if not self.success:
            response        =       {   'full_text'     :   'pubIP: None',
                                        'name'          :   'public',
                                    }
            if i3status_config['colors']:
                response['colors']      =       i3status_config['color_bad']

            return (6, response)

        else:
        # Set cache timeout seeing as how your public IP is unlikely to change much
            CACHE_TIMEOUT   =       600

            # Bulid response dictionary
            response        =       {   'full_text'     :   'pubIP: {0}'.format(self.ip), 
                                        'name'          :   'public',
                                        'cached_until'  :   time() + CACHE_TIMEOUT
                                    }

            if i3status_config['colors']:
                response['colors']      =       i3status_config['color_good']



            return (6, response)
