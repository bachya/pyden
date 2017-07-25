"""
File: trash.py
Author: Aaron Bach
Email: bachya1208@gmail.com
Github: https://github.com/bachya/pyden
"""

# -*- coding: utf-8 -*-
# pylint: disable=redefined-outer-name

import pytest


@pytest.fixture(scope='session')
def coordinates():
    """ Fixture to return a set of coordinates """
    return (40.6892494, -74.0445004)


@pytest.fixture(scope='session')
def geocode_response_200():
    """ Fixture to return a sample of Google's geocoding API JSON """
    return {
        "results": [{
            "address_components": [{
                "long_name": "1",
                "short_name": "1",
                "types": ["street_number"]
            }, {
                "long_name":
                "Liberty Island - Ellis Island",
                "short_name":
                "Liberty Island - Ellis Island",
                "types": ["route"]
            }, {
                "long_name": "Liberty Island",
                "short_name": "Liberty Island",
                "types": ["neighborhood", "political"]
            }, {
                "long_name":
                "Manhattan",
                "short_name":
                "Manhattan",
                "types": ["political", "sublocality", "sublocality_level_1"]
            }, {
                "long_name": "New York",
                "short_name": "New York",
                "types": ["locality", "political"]
            }, {
                "long_name":
                "New York County",
                "short_name":
                "New York County",
                "types": ["administrative_area_level_2", "political"]
            }, {
                "long_name":
                "New York",
                "short_name":
                "NY",
                "types": ["administrative_area_level_1", "political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }, {
                "long_name": "10004",
                "short_name": "10004",
                "types": ["postal_code"]
            }, {
                "long_name": "1418",
                "short_name": "1418",
                "types": ["postal_code_suffix"]
            }],
            "formatted_address":
            "1 Liberty Island - Ellis Island, New York, NY 10004, USA",
            "geometry": {
                "location": {
                    "lat": 40.6898059,
                    "lng": -74.04502269999999
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 40.6911548802915,
                        "lng": -74.04367371970849
                    },
                    "southwest": {
                        "lat": 40.6884569197085,
                        "lng": -74.0463716802915
                    }
                }
            },
            "place_id":
            "ChIJb3tL045QwokRYfNmCnemBzY",
            "types": ["street_address"]
        }, {
            "address_components": [{
                "long_name": "Liberty Island",
                "short_name": "Liberty Island",
                "types": ["neighborhood", "political"]
            }, {
                "long_name":
                "Manhattan",
                "short_name":
                "Manhattan",
                "types": ["political", "sublocality", "sublocality_level_1"]
            }, {
                "long_name": "New York",
                "short_name": "New York",
                "types": ["locality", "political"]
            }, {
                "long_name":
                "New York County",
                "short_name":
                "New York County",
                "types": ["administrative_area_level_2", "political"]
            }, {
                "long_name":
                "New Jersey",
                "short_name":
                "NJ",
                "types": ["administrative_area_level_1", "political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "Liberty Island, New York, NJ, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 40.691185,
                        "lng": -74.0435129
                    },
                    "southwest": {
                        "lat": 40.68854210000001,
                        "lng": -74.0472852
                    }
                },
                "location": {
                    "lat": 40.6900495,
                    "lng": -74.0450675
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 40.69121253029151,
                        "lng": -74.0435129
                    },
                    "southwest": {
                        "lat": 40.68851456970851,
                        "lng": -74.0472852
                    }
                }
            },
            "place_id":
            "ChIJRYGi0o5QwokRLsLNYgBkDgg",
            "types": ["neighborhood", "political"]
        }, {
            "address_components": [{
                "long_name":
                "Manhattan",
                "short_name":
                "Manhattan",
                "types": ["political", "sublocality", "sublocality_level_1"]
            }, {
                "long_name": "New York",
                "short_name": "New York",
                "types": ["locality", "political"]
            }, {
                "long_name":
                "New York County",
                "short_name":
                "New York County",
                "types": ["administrative_area_level_2", "political"]
            }, {
                "long_name":
                "New York",
                "short_name":
                "NY",
                "types": ["administrative_area_level_1", "political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "Manhattan, New York, NY, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 40.882214,
                        "lng": -73.907
                    },
                    "southwest": {
                        "lat": 40.6803955,
                        "lng": -74.047285
                    }
                },
                "location": {
                    "lat": 40.7830603,
                    "lng": -73.9712488
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 40.820045,
                        "lng": -73.90331300000001
                    },
                    "southwest": {
                        "lat": 40.698078,
                        "lng": -74.03514899999999
                    }
                }
            },
            "place_id":
            "ChIJYeZuBI9YwokRjMDs_IEyCwo",
            "types": ["political", "sublocality", "sublocality_level_1"]
        }, {
            "address_components": [{
                "long_name": "New York",
                "short_name": "New York",
                "types": ["locality", "political"]
            }, {
                "long_name":
                "New York",
                "short_name":
                "NY",
                "types": ["administrative_area_level_1", "political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "New York, NY, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 40.9175771,
                        "lng": -73.70027209999999
                    },
                    "southwest": {
                        "lat": 40.4773991,
                        "lng": -74.25908989999999
                    }
                },
                "location": {
                    "lat": 40.7127837,
                    "lng": -74.0059413
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 40.9152555,
                        "lng": -73.70027209999999
                    },
                    "southwest": {
                        "lat": 40.4960439,
                        "lng": -74.25573489999999
                    }
                }
            },
            "place_id":
            "ChIJOwg_06VPwokRYv534QaPC8g",
            "types": ["locality", "political"]
        }, {
            "address_components": [{
                "long_name": "10004",
                "short_name": "10004",
                "types": ["postal_code"]
            }, {
                "long_name":
                "Manhattan",
                "short_name":
                "Manhattan",
                "types": ["political", "sublocality", "sublocality_level_1"]
            }, {
                "long_name": "New York",
                "short_name": "New York",
                "types": ["locality", "political"]
            }, {
                "long_name":
                "New York County",
                "short_name":
                "New York County",
                "types": ["administrative_area_level_2", "political"]
            }, {
                "long_name":
                "New York",
                "short_name":
                "NY",
                "types": ["administrative_area_level_1", "political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "New York, NY 10004, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 40.70684,
                        "lng": -74.0060658
                    },
                    "southwest": {
                        "lat": 40.6885304,
                        "lng": -74.04723799999999
                    }
                },
                "location": {
                    "lat": 40.7038704,
                    "lng": -74.0138541
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 40.70684,
                        "lng": -74.0060658
                    },
                    "southwest": {
                        "lat": 40.6993429,
                        "lng": -74.01805399999999
                    }
                }
            },
            "place_id":
            "ChIJBxh0HZBQwokRQHMru52e-ng",
            "postcode_localities": ["BOWLING GREEN", "New York"],
            "types": ["postal_code"]
        }, {
            "address_components": [{
                "long_name":
                "New York County",
                "short_name":
                "New York County",
                "types": ["administrative_area_level_2", "political"]
            }, {
                "long_name":
                "New York",
                "short_name":
                "NY",
                "types": ["administrative_area_level_1", "political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "New York County, NY, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 40.882214,
                        "lng": -73.907
                    },
                    "southwest": {
                        "lat": 40.6803955,
                        "lng": -74.047285
                    }
                },
                "location": {
                    "lat": 40.7830603,
                    "lng": -73.9712488
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 40.8792779,
                        "lng": -73.907
                    },
                    "southwest": {
                        "lat": 40.6838815,
                        "lng": -74.04723679999999
                    }
                }
            },
            "place_id":
            "ChIJOwE7_GTtwokRFq0uOwLSE9g",
            "types": ["administrative_area_level_2", "political"]
        }, {
            "address_components": [{
                "long_name":
                "New York-Northern New Jersey-Long Island, NY-NJ-PA",
                "short_name":
                "New York-Northern New Jersey-Long Island, NY-NJ-PA",
                "types": ["political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "New York-Northern New Jersey-Long Island, NY-NJ-PA, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 41.6018065,
                        "lng": -71.85621399999999
                    },
                    "southwest": {
                        "lat": 39.49853299999999,
                        "lng": -75.3585939
                    }
                },
                "location": {
                    "lat": 40.9590293,
                    "lng": -74.0300122
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 41.6018065,
                        "lng": -71.85621399999999
                    },
                    "southwest": {
                        "lat": 39.49853299999999,
                        "lng": -75.3585939
                    }
                }
            },
            "place_id":
            "ChIJ3YJV4PRWwokRFFI21ZrHXtQ",
            "types": ["political"]
        }, {
            "address_components": [{
                "long_name": "New York Metropolitan Area",
                "short_name": "New York Metropolitan Area",
                "types": ["political"]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "New York Metropolitan Area, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 42.0809059,
                        "lng": -71.777491
                    },
                    "southwest": {
                        "lat": 39.475198,
                        "lng": -75.3587649
                    }
                },
                "location": {
                    "lat": 40.7127761,
                    "lng": -74.00595439999999
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 42.0809059,
                        "lng": -71.777491
                    },
                    "southwest": {
                        "lat": 39.475198,
                        "lng": -75.3587649
                    }
                }
            },
            "place_id":
            "ChIJ-5Z24NaGwokRiMh4Rj8FNMo",
            "types": ["political"]
        }, {
            "address_components": [{
                "long_name":
                "New York",
                "short_name":
                "NY",
                "types": [
                    "administrative_area_level_1", "establishment",
                    "point_of_interest", "political"
                ]
            }, {
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "New York, USA",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 45.015865,
                        "lng": -71.777491
                    },
                    "southwest": {
                        "lat": 40.4773991,
                        "lng": -79.7625901
                    }
                },
                "location": {
                    "lat": 43.2994285,
                    "lng": -74.21793260000001
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 45.0125923,
                        "lng": -71.8562029
                    },
                    "southwest": {
                        "lat": 40.4961036,
                        "lng": -79.761996
                    }
                }
            },
            "place_id":
            "ChIJqaUj8fBLzEwRZ5UY3sHGz90",
            "types": [
                "administrative_area_level_1", "establishment",
                "point_of_interest", "political"
            ]
        }, {
            "address_components": [{
                "long_name": "United States",
                "short_name": "US",
                "types": ["country", "political"]
            }],
            "formatted_address":
            "United States",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 71.5388001,
                        "lng": -66.885417
                    },
                    "southwest": {
                        "lat": 18.7763,
                        "lng": 170.5957
                    }
                },
                "location": {
                    "lat": 37.09024,
                    "lng": -95.712891
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 49.38,
                        "lng": -66.94
                    },
                    "southwest": {
                        "lat": 25.82,
                        "lng": -124.39
                    }
                }
            },
            "place_id":
            "ChIJCzYy5IS16lQRQrfeQ5K5Oxw",
            "types": ["country", "political"]
        }],
        "status":
        "OK"
    }


@pytest.fixture(scope='session')
def geocode_response_404():
    """ Fixture to return a sample of Google's geocoding API JSON """
    return {"results": [], "status": "OK"}


@pytest.fixture(scope='session')
def geocode_url(coordinates):
    """ Fixture to return the URL used to geocode """
    return 'https://maps.googleapis.com/maps/api/geocode/json?language=' \
            '&latlng={0}&sensor=false'.format(', '.join(map(str, coordinates)))


@pytest.fixture(scope='session')
def place_id():
    """ Fixture to return a Recollect place ID """
    return 'AB047B30-6E8E-11E7-BE70-041F908560DB'


@pytest.fixture(scope='session')
def place_lookup_url(coordinates, service_id):
    """ Fixture to return the URL used to query schedule data """
    lat, long = coordinates
    return 'https://recollect.net/api/lookup/{0},{1}.json?service={2}' \
            '&address=1+Liberty+Island+-+Ellis+Island%2C+New+York%2C+' \
            'NY+10004+US&locale=en-US&postal_code=10004&street_number=1' \
            '&street_name=Liberty%20Island%20-%20Ellis%20Island&subpremise=' \
            '&locality=New%20York' \
            '&territory=NY&country=US'.format(lat, long, service_id)


@pytest.fixture(scope='session')
def place_lookup_response_200(coordinates, place_id):
    """ Fixture to return a successful schedule() response """
    lat, long = coordinates
    return {
        'place': {
            'lat': lat,
            'province': 'colorado',
            'locale': 'en-US',
            'lng': long,
            'unit': '',
            'street': 'main street',
            'house': '123',
            'name': '123 Main Street, Denver',
            'id': place_id,
            'city': 'denver',
            'country': 'usa',
            'source': 'recollect'
        }
    }


@pytest.fixture(scope='session')
def place_lookup_response_404():
    """ Fixture to return a successful schedule() response """
    return {'place': {}}


@pytest.fixture(scope='session')
def schedule_response_200():
    """ Fixture to return a successful schedule() response """
    return """
BEGIN:VCALENDAR
VERSION:2.0
METHOD:PUBLISH
PRODID:Data::ICal 0.22
X-PUBLISHED-TTL:1440
X-WR-CALDESC:Solid Waste
X-WR-CALNAME:8373 East 55th Avenue\, Denver\, CO 80216 US
X-WR-TIMEZONE:America/Denver
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20170710
SUMMARY:Trash and compost (sign-up only)
UID:2017-07-10-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20170717
SUMMARY:Trash\, recycling\, and compost (sign-up only)
UID:2017-07-17-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20170724
SUMMARY:Trash and compost (sign-up only)
UID:2017-07-24-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20170731
SUMMARY:Trash\, extra trash\, recycling\, and compost (sign-up only)
UID:2017-07-31-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20170807
SUMMARY:Trash and compost (sign-up only)
UID:2017-08-07-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20170814
SUMMARY:Trash\, recycling\, and compost (sign-up only)
UID:2017-08-14-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20170821
SUMMARY:Trash and compost (sign-up only)
UID:2017-08-21-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20170828
SUMMARY:Trash\, extra trash\, recycling\, and compost (sign-up only)
UID:2017-08-28-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20170905
SUMMARY:Trash and compost (sign-up only)
UID:2017-09-05-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20170911
SUMMARY:Trash\, recycling\, and compost (sign-up only)
UID:2017-09-11-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20170918
SUMMARY:Trash and compost (sign-up only)
UID:2017-09-18-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20170925
SUMMARY:Trash\, extra trash\, recycling\, and compost (sign-up only)
UID:2017-09-25-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20171002
SUMMARY:Trash and compost (sign-up only)
UID:2017-10-02-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20171009
SUMMARY:Trash\, recycling\, and compost (sign-up only)
UID:2017-10-09-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20171016
SUMMARY:Trash and compost (sign-up only)
UID:2017-10-16-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20171023
SUMMARY:Trash\, extra trash\, recycling\, and compost (sign-up only)
UID:2017-10-23-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20171030
SUMMARY:Trash and compost (sign-up only)
UID:2017-10-30-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20171106
SUMMARY:Trash\, recycling\, and compost (sign-up only)
UID:2017-11-06-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20171113
SUMMARY:Trash and compost (sign-up only)
UID:2017-11-13-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20171120
SUMMARY:Trash\, extra trash\, recycling\, and compost (sign-up only)
UID:2017-11-20-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20171127
SUMMARY:Trash and compost (sign-up only)
UID:2017-11-27-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20171204
SUMMARY:Trash\, recycling\, and compost (sign-up only)
UID:2017-12-04-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20171211
SUMMARY:Trash and compost (sign-up only)
UID:2017-12-11-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash\, extra trash\, recycling\, and compost (sign-up only)
DTSTART;VALUE=DATE:20171218
SUMMARY:Trash\, extra trash\, recycling\, and compost (sign-up only)
UID:2017-12-18-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Trash and compost (sign-up only)
DTSTART;VALUE=DATE:20171226
SUMMARY:Trash and compost (sign-up only)
UID:2017-12-26-Denver-waste-@recollect.net
END:VEVENT
BEGIN:VEVENT
DESCRIPTION:Extra trash
DTSTART;VALUE=DATE:20180116
SUMMARY:Extra trash
UID:2018-01-16-Denver-waste-@recollect.net
END:VEVENT
END:VCALENDAR
	"""


@pytest.fixture(scope='session')
def schedule_response_200_json():
    """ Fixture to return a successful schedule() response """
    return {
        '2017-07-24': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-07-31': {
            'compost': True,
            'extra_trash': True,
            'recycling': True,
            'trash': True
        },
        '2017-08-07': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-08-14': {
            'compost': True,
            'extra_trash': False,
            'recycling': True,
            'trash': True
        },
        '2017-08-21': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-08-28': {
            'compost': True,
            'extra_trash': True,
            'recycling': True,
            'trash': True
        },
        '2017-09-05': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-09-11': {
            'compost': True,
            'extra_trash': False,
            'recycling': True,
            'trash': True
        },
        '2017-09-18': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-09-25': {
            'compost': True,
            'extra_trash': True,
            'recycling': True,
            'trash': True
        },
        '2017-10-02': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-10-09': {
            'compost': True,
            'extra_trash': False,
            'recycling': True,
            'trash': True
        },
        '2017-10-16': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-10-23': {
            'compost': True,
            'extra_trash': True,
            'recycling': True,
            'trash': True
        },
        '2017-10-30': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-11-06': {
            'compost': True,
            'extra_trash': False,
            'recycling': True,
            'trash': True
        },
        '2017-11-13': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-11-20': {
            'compost': True,
            'extra_trash': True,
            'recycling': True,
            'trash': True
        },
        '2017-11-27': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-12-04': {
            'compost': True,
            'extra_trash': False,
            'recycling': True,
            'trash': True
        },
        '2017-12-11': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2017-12-18': {
            'compost': True,
            'extra_trash': True,
            'recycling': True,
            'trash': True
        },
        '2017-12-26': {
            'compost': True,
            'extra_trash': False,
            'recycling': False,
            'trash': True
        },
        '2018-01-16': {
            'compost': False,
            'extra_trash': True,
            'recycling': False,
            'trash': True
        }
    }


@pytest.fixture(scope='session')
def schedule_url(place_id, service_id):
    """ Fixture to return the URL used to query schedule data """
    return 'https://recollect.net/api/places/{0}/services/{1}/' \
            'events.en-US.ics'.format(place_id, service_id)


@pytest.fixture(scope='session')
def service_id():
    """ Fixture to return a Recollect service ID """
    return 248
