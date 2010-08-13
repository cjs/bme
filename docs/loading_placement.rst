Loading Placement Data
----------------------

* You need the placement csv file exported from the filemaker database:

  Example:

  "2010","13416","Celestial Bodies","7:30 & Detroit","www.campcelestialbodies.org","30 to 39","100 x 150","Celestial Bodies is a straight-friendly camp hosting a large and comfortable [underground] lounge for shade, drinks, music and entertainment. Don you favorite SuperHero playa wear and join us for an afternoon Tea Dance, Classical Chill each morning, and check out our other events and activities.","Steve R","Drew","San Francisco","CA","United States of America","campcelestialbodies@yahoo.com"

* Format is:

 * year - need to look up year id before updating
 * bm_fm_id - filemaker ID
 * name
 * location_string - also parse and look for times to put in time_address
 * url
 * *ignore*
 * *ignore*
 * description
 * *ignore* - First and middle names of contact
 * *ignore* - Last name of contact
 * hometown - city - concatenate with next field
 * hometown - state - maybe concatenate with next field if not USA
 * hometown - country
 * contact_email

* Use "./manage.py bme_load_placement *filename*" to load the data.

