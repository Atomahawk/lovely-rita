column_maps = [{'street': 'Street',
                'city': 'City',
                'state': 'State',
                'ticket_number': 'Ticket Number',
                'ticket_issue_date': 'Ticket Issue Date',
                'ticket_issue_time': 'Ticket Issue Time',
                'violation_external_code': 'Violation External Code',
                'violation_desc_long': 'Violation Description Long',
                'street_no': 'Street Number',
                'street_name': 'Street Name',
                'street_suffix': 'Street Suffix',
                'fine_amount': 'Fine Amount',
                'badge__': 'Badge Number',
                'Unnamed: 13': 'Unnamed: 13',
                '[sequence]': 'Sequence',
                '[summary]': 'Summary',
                '[addressee]': 'Addressee',
                '[delivery_line_1]': 'Delivery Line 1',
                '[delivery_line_2]': 'Delivery Line 2',
                '[city_name]': 'City Name',
                '[state_abbreviation]': 'State Abbreviation',
                '[full_zipcode]': 'Full Zipcode',
                '[notes]': 'Notes',
                '[county_name]': 'County Name',
                '[rdi]': 'RCI',
                '[latitude]': 'Latitude',
                '[longitude]': 'Longitude',
                '[precision]': 'Precision',
                '[dpv_match_code]': 'DPV Match Code',
                '[dpv_footnotes]': 'DPV Footnotes',
                '[footnotes]': 'Footnotes',
                '[county_fips]': 'County FIPS',
                '[record_type]': 'Record Type',
                '[zip_type]': 'Zip Type',
                '[carrier_route]': 'Carrier Route',
                '[congressional_district]': 'Congressional District',
                '[building_default_indicator]': 'Building Default Indicator',
                '[elot_sequence]': 'eLot Sequence',
                '[elot_sort]': 'eLot Sort',
                '[time_zone]': 'Time Zone',
                '[utc_offset]': 'UTC Offset',
                '[dst]': 'DST',
                '[dpv_cmra]': 'DPV Camera',
                '[ews_match]': 'EWS Match',
                '[lacslink_indicator]': 'LACS Link Indicator',
                '[lacslink_code]': 'LACS Link Code',
                '[suitelink_match]': 'Suite Link Match',
                '[dpv_vacant]': 'DPV Vacant',
                '[active]': 'Active',
                '[urbanization]': 'Urbanization',
                '[primary_number]': 'Primary Number',
                '[street_name]': 'Street Name 2',
                '[street_predirection]': 'Street Predirection',
                '[street_postdirection]': 'Street Postdirection',
                '[street_suffix]': 'Street Suffix 2',
                '[secondary_number]': 'Secondary Number',
                '[secondary_designator]': 'Secondary Designator',
                '[extra_secondary_number]': 'Extra Secondary Number',
                '[extra_secondary_designator]': 'Extra Secondary Designator',
                '[pmb_designator]': 'PMB Designator',
                '[pmb_number]': 'PMB Number',
                '[default_city_name]': 'Default City Name',
                '[zipcode]': 'Zipcode',
                '[plus4_code]': 'Plus 4 Code',
                '[delivery_point]': 'Delivery Point',
                '[delivery_point_check_digit]': 'Delivery Point Check Digit',
                '[last_line]': 'Last Line',
                '[delivery_point_barcode]': 'Delivery Point Barcode'},

               {'street': 'Street',
                'city': 'City',
                'state': 'State',
                'Ticket Number': 'Ticket Number',
                'Ticket Issue Date': 'Ticket Issue Date',
                'Ticket Issue Time': 'Ticket Issue Time',
                'Violation External Code': 'Violation External Code',
                'Violation Desc Long': 'Violation Description Long',
                'Street No': 'Street Number',
                'Street Name': 'Street Name',
                'Street Suffix': 'Street Suffix',
                'Fine Amount': 'Fine Amount',
                'Badge #': 'Badge Number',
                'Unnamed: 13': 'Unnamed: 13',
                '[sequence]': 'Sequence',
                '[summary]': 'Summary',
                '[addressee]': 'Addressee',
                '[delivery_line_1]': 'Delivery Line 1',
                '[delivery_line_2]': 'Delivery Line 2',
                '[city_name]': 'City Name',
                '[state_abbreviation]': 'State Abbreviation',
                '[full_zipcode]': 'Full Zipcode',
                '[notes]': 'Notes',
                '[county_name]': 'County Name',
                '[rdi]': 'RCI',
                '[latitude]': 'Latitude',
                '[longitude]': 'Longitude',
                '[precision]': 'Precision',
                '[dpv_match_code]': 'DPV Match Code',
                '[dpv_footnotes]': 'DPV Footnotes',
                '[footnotes]': 'Footnotes',
                '[county_fips]': 'County FIPS',
                '[record_type]': 'Record Type',
                '[zip_type]': 'Zip Type',
                '[carrier_route]': 'Carrier Route',
                '[congressional_district]': 'Congressional District',
                '[building_default_indicator]': 'Building Default Indicator',
                '[elot_sequence]': 'eLot Sequence',
                '[elot_sort]': 'eLot Sort',
                '[time_zone]': 'Time Zone',
                '[utc_offset]': 'UTC Offset',
                '[dst]': 'DST',
                '[dpv_cmra]': 'DPV Camera',
                '[ews_match]': 'EWS Match',
                '[lacslink_indicator]': 'LACS Link Indicator',
                '[lacslink_code]': 'LACS Link Code',
                '[suitelink_match]': 'Suite Link Match',
                '[dpv_vacant]': 'DPV Vacant',
                '[active]': 'Active',
                '[urbanization]': 'Urbanization',
                '[primary_number]': 'Primary Number',
                '[street_name]': 'Street Name 2',
                '[street_predirection]': 'Street Predirection',
                '[street_postdirection]': 'Street Postdirection',
                '[street_suffix]': 'Street Suffix 2',
                '[secondary_number]': 'Secondary Number',
                '[secondary_designator]': 'Secondary Designator',
                '[extra_secondary_number]': 'Extra Secondary Number',
                '[extra_secondary_designator]': 'Extra Secondary Designator',
                '[pmb_designator]': 'PMB Designator',
                '[pmb_number]': 'PMB Number',
                '[default_city_name]': 'Default City Name',
                '[zipcode]': 'Zipcode',
                '[plus4_code]': 'Plus 4 Code',
                '[delivery_point]': 'Delivery Point',
                '[delivery_point_check_digit]': 'Delivery Point Check Digit',
                '[last_line]': 'Last Line',
                '[delivery_point_barcode]': 'Delivery Point Barcode'
               }
              ]

columns_to_drop = ["Addressee",
                   "Delivery Line 2",
                   "EWS Match",
                   "Extra Secondary Number",
                   "PMB Designator",
                   "PMB Number",
                   "Suite Link Match",
                   "Unnamed: 13",
                   "Urbanization"
                   ]
