blacklisted_generators = [
    'latitude',
    'geo_coordinate',
    'longitude',
    'time_delta',
    'date_object',
    'date_time',
    'date_time_between',
    'date_time_ad',
    'date_time_this_decade',
    'date_time_between_dates',
    'time_object',
    'date_time_this_year',
    'date_time_this_century',
    'date_time_this_month',
    'sentences',
    'words',
    'paragraphs',
    'binary',
    'pylist',
    'pyiterable',
    'pyfloat',
    'pystruct',
    'pyint',
    'pyset',
    'pydecimal',
    'pydict',
    'pytuple',
    'pystr',
    'pybool',
    'profile',
]

available_generators = {
    'address': [
        'address',
        'postcode',
        'military_ship',
        'country_code',
        'military_state',
        'postalcode_plus4',
        'country',
        'random_number',
        'random_letter',
        'military_apo',
        'random_digit_or_empty',
        'city_prefix',
        'state_abbr',
        'military_dpo',
        'zipcode_plus4',
        'street_name',
        'random_digit',
        'street_suffix',
        'street_address',
        'zipcode',
        'secondary_address',
        'random_digit_not_null',
        'city',
        'random_int',
        'state',
        'city_suffix',
        'postalcode',
        'building_number'
    ],
    'barcode': [
        'ean13',
        'ean',
        'ean8'
    ],
    'color': [
        'color_name',
        'rgb_color_list',
        'rgb_color',
        'safe_hex_color',
        'hex_color',
        'rgb_css_color',
        'safe_color_name'
    ],
    'company': [
        'company',
        'catch_phrase',
        'company_suffix',
        'bs',
    ],
    'credit_card': [
        'credit_card_provider',
        'credit_card_security_code',
        'credit_card_full',
        'credit_card_number',
        'credit_card_expire'
    ],
    'date_time': [
        'day_of_month',
        'timezone',
        'month',
        'year',
        'day_of_week',
        'unix_time',
        'time',
        'century',
        'am_pm',
        'month_name',
        'iso8601'
    ],
    'file': [
        'file_extension',
        'mime_type',
        'file_path',
        'file_name'
    ],
    'internet': [
        'user_name',
        'email',
        'image_url',
        'ipv4',
        'free_email_domain',
        'tld',
        'domain_name',
        'uri_path',
        'uri_extension',
        'uri',
        'url',
        'ipv6',
        'free_email',
        'domain_word',
        'uri_page',
        'mac_address',
        'company_email',
        'safe_email',
        'slug'
    ],
    'isbn': [
        'isbn10',
        'isbn13'
    ],
    'lorem': [
        'sentence',
        'text',
        'paragraph',
        'word'
    ],
    'misc': [
        'uuid4',
        'sha256',
        'locale',
        'md5',
        'boolean',
        'language_code',
        'sha1',
        'password',
        'ssn',
        'job',
        'currency_code',
        'phone_number'
    ],
    'person': [
        'prefix_male',
        'suffix',
        'prefix_female',
        'name_male',
        'suffix_male',
        'name',
        'first_name',
        'suffix_female',
        'last_name_male',
        'first_name_female',
        'last_name',
        'name_female',
        'prefix',
        'first_name_male',
        'last_name_female'
    ],
    'profile': [
        'simple_profile'
    ],
    'user_agent': [
        'user_agent',
        'safari',
        'firefox',
        'linux_platform_token',
        'mac_platform_token',
        'mac_processor',
        'windows_platform_token',
        'opera',
        'internet_explorer',
        'chrome',
        'linux_processor'
    ]
}

# We only need this for local development.
if __name__ == '__main__':
    for i in blacklisted_generators:
        for k,v in available_generators.items():
            assert not i in v, "Blacklisted generator %s found in available list %s" % (i,k)

