import pandas as pd
import numpy as np
fn = {}

def __increment_0_to_2(studydata, column, context):
    """Please increment codes of 0, 1, and 2, but leave code 4 as it is."""
    return column.replace({0:1,1:2,2:3}).astype('Int64')

fn["asr1"]=__increment_0_to_2
fn["asr2"]=__increment_0_to_2
fn["asr3"]=__increment_0_to_2
fn["asr4"]=__increment_0_to_2
fn["asr5"]=__increment_0_to_2
fn["asr6"]=__increment_0_to_2
fn["asr7"]=__increment_0_to_2
fn["asr8"]=__increment_0_to_2
fn["asr9"]=__increment_0_to_2
fn["asr10"]=__increment_0_to_2
fn["asr11"]=__increment_0_to_2
fn["asr12"]=__increment_0_to_2
fn["asr13"]=__increment_0_to_2
fn["asr14"]=__increment_0_to_2
fn["asr15"]=__increment_0_to_2
fn["asr16"]=__increment_0_to_2
fn["asr17"]=__increment_0_to_2
fn["asr18"]=__increment_0_to_2
fn["asr19"]=__increment_0_to_2
fn["asr20"]=__increment_0_to_2
fn["asr21"]=__increment_0_to_2
fn["asr22"]=__increment_0_to_2

"""Please rename this column 'asr4_5' to avoid a naming conflict in our database.  Please increment your 0::2 scale to a 1::3 scale."""
fn["asr23"]=__increment_0_to_2

"""Please rename this column 'asr4_6' to avoid a naming conflict in our database.Please increment your 0::2 scale to a 1::3 scale."""
fn["asr24"]=__increment_0_to_2

"""Please rename this column 'asr5_1' to avoid a naming conflict in our database.Please increment your 0::2 scale to a 1::3 scale."""
fn["asr25"]=__increment_0_to_2

fn["asr26"]=__increment_0_to_2
fn["asr27"]=__increment_0_to_2
fn["asr28"]=__increment_0_to_2
fn["asr29"]=__increment_0_to_2
fn["asr30"]=__increment_0_to_2
fn["asr31"]=__increment_0_to_2
fn["asr32"]=__increment_0_to_2
fn["asr33"]=__increment_0_to_2
fn["asr34"]=__increment_0_to_2
fn["asr35"]=__increment_0_to_2
fn["asr36"]=__increment_0_to_2
fn["asr37"]=__increment_0_to_2

"""Please rename this column 'asr7_2' to avoid a naming conflict in our database.  Please increment your 0::2 scale to a 1::3 scale."""
fn["asr38"]=__increment_0_to_2

fn["asr39"]=__increment_0_to_2
fn["asr40"]=__increment_0_to_2
fn["asr41"]=__increment_0_to_2
fn["asr42"]=__increment_0_to_2
fn["asr43"]=__increment_0_to_2
fn["asr44"]=__increment_0_to_2
fn["asr45"]=__increment_0_to_2
fn["asr46"]=__increment_0_to_2
fn["asr47"]=__increment_0_to_2
fn["asr48"]=__increment_0_to_2
fn["asr49"]=__increment_0_to_2
fn["asr50"]=__increment_0_to_2
fn["asr51"]=__increment_0_to_2
fn["asr52"]=__increment_0_to_2
fn["asr53"]=__increment_0_to_2
fn["asr54"]=__increment_0_to_2
fn["asr55"]=__increment_0_to_2
fn["asr56a"]=__increment_0_to_2
fn["asr56b"]=__increment_0_to_2
fn["asr56c"]=__increment_0_to_2
fn["asr56d"]=__increment_0_to_2
fn["asr56e"]=__increment_0_to_2
fn["asr56f"]=__increment_0_to_2
fn["asr56g"]=__increment_0_to_2
fn["asr56h"]=__increment_0_to_2
fn["asr56i"]=__increment_0_to_2
fn["asr57"]=__increment_0_to_2
fn["asr58"]=__increment_0_to_2
fn["asr59"]=__increment_0_to_2
fn["asr60"]=__increment_0_to_2
fn["asr61"]=__increment_0_to_2
fn["asr62"]=__increment_0_to_2
fn["asr63"]=__increment_0_to_2
fn["asr64"]=__increment_0_to_2
fn["asr65"]=__increment_0_to_2
fn["asr66"]=__increment_0_to_2
fn["asr67"]=__increment_0_to_2
fn["asr68"]=__increment_0_to_2
fn["asr69"]=__increment_0_to_2
fn["asr70"]=__increment_0_to_2
fn["asr71"]=__increment_0_to_2
fn["asr72"]=__increment_0_to_2
fn["asr73"]=__increment_0_to_2
fn["asr74"]=__increment_0_to_2
fn["asr75"]=__increment_0_to_2
fn["asr76"]=__increment_0_to_2
fn["asr77"]=__increment_0_to_2
fn["asr78"]=__increment_0_to_2
fn["asr79"]=__increment_0_to_2
fn["asr80"]=__increment_0_to_2
fn["asr81"]=__increment_0_to_2
fn["asr82"]=__increment_0_to_2
fn["asr83"]=__increment_0_to_2
fn["asr84"]=__increment_0_to_2
fn["asr85"]=__increment_0_to_2
fn["asr86"]=__increment_0_to_2
fn["asr87"]=__increment_0_to_2
fn["asr88"]=__increment_0_to_2
fn["asr89"]=__increment_0_to_2
fn["asr90"]=__increment_0_to_2
fn["asr91"]=__increment_0_to_2
fn["asr92"]=__increment_0_to_2
fn["asr93"]=__increment_0_to_2
fn["asr94"]=__increment_0_to_2
fn["asr95"]=__increment_0_to_2
fn["asr96"]=__increment_0_to_2
fn["asr97"]=__increment_0_to_2
fn["asr98"]=__increment_0_to_2
fn["asr99"]=__increment_0_to_2
fn["asr100"]=__increment_0_to_2
fn["asr101"]=__increment_0_to_2
fn["asr102"]=__increment_0_to_2
fn["asr103"]=__increment_0_to_2
fn["asr104"]=__increment_0_to_2
fn["asr105"]=__increment_0_to_2
fn["asr106"]=__increment_0_to_2
fn["asr107"]=__increment_0_to_2
fn["asr108"]=__increment_0_to_2
fn["asr109"]=__increment_0_to_2
fn["asr110"]=__increment_0_to_2
fn["asr111"]=__increment_0_to_2
fn["asr112"]=__increment_0_to_2
fn["asr113"]=__increment_0_to_2
fn["asr114"]=__increment_0_to_2
fn["asr115"]=__increment_0_to_2
fn["asr116"]=__increment_0_to_2
fn["asr117"]=__increment_0_to_2
fn["asr118"]=__increment_0_to_2
fn["asr119"]=__increment_0_to_2
fn["asr120"]=__increment_0_to_2
fn["asr121"]=__increment_0_to_2
fn["asr122"]=__increment_0_to_2
fn["asr123"]=__increment_0_to_2

def height(studydata, column, context):
    """Please convert heights to inches."""
    pass
fn["height"]=height

def colorvsn1(studydata, column, context):
    """Please convert numeric codes of 0 and 99 to the text strings they represent."""
    studydata.colorvsn1 = studydata.colorvsn1.mask(studydata.colorvsn1 == 0, 'No').mask(studydata.colorvsn1 > 90, "Don't Know")
fn["colorvsn1"]=colorvsn1

def sub_adopt_1unit(studydata, column, context):
    """Age at adoption is a free-text field. Please concatenate responses from 'sub_adopt_1' and 'sub_adopt_1unit' in the 'sub_adopt_1' column."""
    pass
fn["sub_adopt_1unit"]=sub_adopt_1unit

def sub_country(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    studydata['country_string']=studydata.sub_country.replace({840: 'United States' , 4: 'Afghanistan' , 248: 'Aland Islands' , 8: 'Albania' , 12: 'Algeria' , 16: 'American Samoa' , 20: 'Andorra' , 24: 'Angola' , 660: 'Anguilla' , 10: 'Antarctica' , 28: 'Antigua and Barbuda' , 32: 'Argentina' , 51: 'Armenia' , 533: 'Aruba' , 36: 'Australia' , 40: 'Austria' , 31: 'Azerbaijan' , 44: 'Bahamas' , 48: 'Bahrain' , 50: 'Bangladesh' , 52: 'Barbados' , 112: 'Belarus' , 56: 'Belgium' , 84: 'Belize' , 204: 'Benin' , 60: 'Bermuda' , 64: 'Bhutan' , 68: 'Plurinational State of Bolivia' , 535: 'Bonaire Sint Eustatius and Saba' , 70: 'Bosnia and Herzegovina' , 72: 'Botswana' , 74: 'Bouvet Island' , 76: 'Brazil' , 86: 'British Indian Ocean Territory' , 96: 'Brunei Darussalam' , 100: 'Bulgaria' , 854: 'Burkina Faso' , 108: 'Burundi' , 116: 'Cambodia' , 120: 'Cameroon' , 124: 'Canada' , 132: 'Cape Verde' , 136: 'Cayman Islands' , 140: 'Central African Republic' , 148: 'Chad' , 152: 'Chile' , 156: 'China' , 162: 'Christmas Island' , 166: 'Cocos (Keeling) Islands' , 170: 'Colombia' , 174: 'Comoros' , 178: 'Congo' , 180: 'the Democratic Republic of the Congo' , 184: 'Cook Islands' , 188: 'Costa Rica' , 384: 'Cote dIvoire' , 191: 'Croatia' , 192: 'Cuba' , 531: 'Curacao' , 196: 'Cyprus' , 203: 'Czech Republic' , 208: 'Denmark' , 262: 'Djibouti' , 212: 'Dominica' , 214: 'Dominican Republic' , 218: 'Ecuador' , 818: 'Egypt' , 222: 'El Salvador' , 226: 'Equatorial Guinea' , 232: 'Eritrea' , 233: 'Estonia' , 231: 'Ethiopia' , 238: 'Falkland Islands (Malvinas)' , 234: 'Faroe Islands' , 242: 'Fiji' , 246: 'Finland' , 250: 'France' , 254: 'French Guiana' , 258: 'French Polynesia' , 260: 'French Southern Territories' , 266: 'Gabon' , 270: 'Gambia' , 268: 'Georgia' , 276: 'Germany' , 288: 'Ghana' , 292: 'Gibraltar' , 300: 'Greece' , 304: 'Greenland' , 308: 'Grenada' , 312: 'Guadeloupe' , 316: 'Guam' , 320: 'Guatemala' , 831: 'Guernsey' , 324: 'Guinea' , 624: 'Guinea-Bissau' , 328: 'Guyana' , 332: 'Haiti' , 334: 'Heard Island and McDonald Islands' , 336: 'Holy See (Vatican City State)' , 340: 'Honduras' , 344: 'Hong Kong' , 348: 'Hungary' , 352: 'Iceland' , 356: 'India' , 360: 'Indonesia' , 364: 'Islamic Republic of Iran' , 368: 'Iraq' , 372: 'Ireland' , 833: 'Isle of Man' , 376: 'Israel' , 380: 'Italy' , 388: 'Jamaica' , 392: 'Japan' , 832: 'Jersey' , 400: 'Jordan' , 398: 'Kazakhstan' , 404: 'Kenya' , 296: 'Kiribati' , 408:  'Democratic Peoples Republic of Korea' , 410 : 'Republic of Korea' , 414: 'Kuwait' , 417: 'Kyrgyzstan' , 418: 'Lao Peoples Democratic Republic' , 428: 'Latvia' , 422: 'Lebanon' , 426: 'Lesotho' , 430: 'Liberia' , 434: 'Libya' , 438: 'Liechtenstein' , 440: 'Lithuania' , 442: 'Luxembourg' , 446: 'Macao' , 807: 'the former Yugoslav Republic of Macedonia' , 450: 'Madagascar' , 454: 'Malawi' , 458: 'Malaysia' , 462: 'Maldives' , 466: 'Mali' , 470: 'Malta' , 584: 'Marshall Islands' , 474: 'Martinique' , 478: 'Mauritania' , 480: 'Mauritius' , 175: 'Mayotte' , 484: 'Mexico' , 583: 'Federated States of Micronesia' , 498: 'Republic of Maldova' , 492: 'Monaco' , 496: 'Mongolia' , 499: 'Montenegro' , 500: 'Montserrat' , 504: 'Morocco' , 508: 'Mozambique' , 104: 'Myanmar' , 516: 'Namibia' , 520: 'Nauru' , 524: 'Nepal' , 528: 'Netherlands' , 540: 'New Caledonia' , 554: 'New Zealand' , 558: 'Nicaragua' , 562: 'Niger' , 566: 'Nigeria' , 570: 'Niue' , 574: 'Norfolk Island' , 580: 'Northern Mariana Islands' , 578: 'Norway' , 512: 'Oman' , 586: 'Pakistan' , 585: 'Palau' , 275: 'Occupied Palestinian Territory' , 591: 'Panama' , 598: 'Papua New Guinea' , 600: 'Paraguay' , 604: 'Peru' , 608: 'Philippines' , 612: 'Pitcairn' , 616: 'Poland' , 620: 'Portugal' , 630: 'Puerto Rico' , 634: 'Qatar' , 638: 'Reunion' , 642: 'Romania' , 643: 'Russian Federation' , 646: 'Rwanda' , 652: 'Saint Barthelemy' , 654: 'Saint Helena Ascension and Tristan da Cunha' , 659: 'Saint Kitts and Nevis' , 662: 'Saint Lucia' , 663: 'Saint Martin (French part)' , 666: 'Saint Pierre and Miquelon' , 670: 'Saint Vincent and the Grenadines' , 882: 'Samoa' , 674: 'San Marino' , 678: 'Sao Tome and Principe' , 682: 'Saudi Arabia' , 686: 'Senegal' , 688: 'Serbia' , 690: 'Seychelles' , 694: 'Sierra Leone' , 702: 'Singapore' , 534: 'Sint Maarten (Dutch part)' , 703: 'Slovakia' , 705: 'Slovenia' , 90: 'Solomon Islands' , 706: 'Somalia' , 710: 'South Africa' , 239: 'South Georgia and the South Sandwich Islands' , 728: 'South Sudan' , 724: 'Spain' , 144: 'Sri Lanka' , 729: 'Sudan' , 740: 'Suriname' , 744: 'Svalbard and Jan Mayen' , 748: 'Swaziland' , 752: 'Sweden' , 756: 'Switzerland' , 760: 'Syrian Arab Republic' , 158: 'Taiwan Province of China' , 762: 'Tajikistan' , 834: 'United Republic of Tanzania' , 764: 'Thailand' , 626: 'Timor-Leste' , 768: 'Togo' , 772: 'Tokelau' , 776: 'Tonga' , 780: 'Trinidad and Tobago' , 788: 'Tunisia' , 792: 'Turkey' , 795: 'Turkmenistan' , 796: 'Turks and Caicos Islands' , 798: 'Tuvalu' , 800: 'Uganda' , 804: 'Ukraine' , 784: 'United Arab Emirates' , 826: 'United Kingdom' , 581: 'United States Minor Outlying Islands' , 858: 'Uruguay' , 860: 'Uzbekistan' , 548: 'Vanuatu' , 862: 'Bolivarian Republic of Venezuela' , 704: 'Viet Nam' , 92: 'British Virgin Islands' , 850:  'U.S. Virgin Islands' , 876: 'Wallis and Futuna' , 732: 'Western Sahara' , 887: 'Yemen' , 263: 'Zimbabwe' , 99: 'Dont Know'})
    studydata['sub_country']=studydata.country_string
fn["sub_country"]=sub_country

def sub_gender_different(studydata, column, context):
    """Gender identity is a free-text field. Please concatenate responses from 'sub_gender' and 'sub_gender_different' in the 'sub_gender' column."""
    pass
fn["sub_gender_different"]=sub_gender_different

def sub_marriage(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    studydata['sub_marriage']=studydata.sub_marriage.astype(str).replace({'1' : 'MARRIED' , '2' : 'WIDOWED'  , '3' : 'DIVORCED', '4': 'SEPARATED', '5': 'NEVER MARRIED','6':'LIVING WITH PARTNER','7':'REFUSED','9':'DONT KNOW'})
fn["sub_marriage"]=sub_marriage

def sub_grade(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    studydata['sub_grade']=studydata.sub_grade.astype(str).replace({'0' : 'KINDERGARTEN' , '1' : '1ST GRADE' , '2' : '2ND GRADE' , '3' : '3RD GRADE' , '4' : '4TH GRADE' , '5' : '5TH GRADE' , '6' : '6TH GRADE' , '7' : '7TH GRADE' , '8' : '8TH GRADE' , '9' : '9TH GRADE' , '10' : '10TH GRADE' , '11' : '11TH GRADE' , '12' : '12TH GRADE NO DIPLOMA' , '13' : 'HIGH SCHOOL GRADUATE' , '14' : 'GED OR EQUIVALENT' , '15' : 'SOME COLLEGE NO DEGREE' , '16' : 'ASSOCIATE DEGREE: OCCUPATIONAL TECHNICAL OR VOCATIONAL PROGRAM' , '17' : 'ASSOCIATE DEGREE: ACADEMIC PROGRAM' , '18' : 'BACHELORS DEGREE (EXAMPLE: BA AB BS BBA)' , '19' : 'MASTERS DEGREE (EXAMPLE: MA MS MEng MEd MBA)' , '20' : 'PROFESSIONAL SCHOOL DEGREE (EXAMPLE: MD DDS DVM JD)' , '21' : 'DOCTORAL DEGREE (EXAMPLE:PhD EdD)' , '77' : 'REFUSED' , '99' : 'DONT KNOW'})
fn["sub_grade"]=sub_grade

def sub_job(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    studydata['sub_job']=studydata.sub_job.astype(str).replace({'1': 'WORKING NOW', '2': 'ONLY TEMPORARILY LAID OFF', '2.1': 'SICK LEAVE', '2.2': 'MATERNITY LEAVE', '3.1': 'UNEMPLOYED LOOKING FOR WORK','3.2' : 'UNEMPLOYED NOT LOOKING FOR WORK', '4': 'RETIRED', '5': 'DISABLED PERMANENTLY OR TEMPORARILY', '6' : 'TAKING CARE OF CHILDREN AND/OR RAISING CHILDREN AND/OR CARING FOR AGING PARENTS' , '7': 'STUDENT', '8' : 'OTHER: '})
fn["sub_job"]=sub_job

def sub_job8_1(studydata, column, context):
    """Because 'sub_job' is a free-text field, please concatenate subjects' specified answers with 'sub_job' answers."""
    studydata['sub_job']=studydata.sub_job+studydata.sub_job8_1
fn["sub_job8_1"]=sub_job8_1

def sub_income_num(studydata, column, context):
    """Please us 98 as the missing code, rather than 999999."""
    studydata.loc[studydata.sub_income_num.astype(str).str.contains('99'),'sub_income_num']='98'
fn["sub_income_num"]=sub_income_num

def sub_bio_f_country(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    studydata['sub_bio_f_country']=studydata.sub_bio_f_country.astype(str).replace({'840' : 'United States' , '4' : 'Afghanistan' , '248' : 'Aland Islands' , '8' : 'Albania' , '12' : 'Algeria' , '16' : 'American Samoa' , '20' : 'Andorra' , '24' : 'Angola' , '660' : 'Anguilla' , '10' : 'Antarctica' , '28' : 'Antigua and Barbuda' , '32' : 'Argentina' , '51' : 'Armenia' , '533' : 'Aruba' , '36' : 'Australia' , '40' : 'Austria' , '31' : 'Azerbaijan' , '44' : 'Bahamas' , '48' : 'Bahrain' , '50' : 'Bangladesh' , '52' : 'Barbados' , '112' : 'Belarus' , '56' : 'Belgium' , '84' : 'Belize' , '204' : 'Benin' , '60' : 'Bermuda' , '64' : 'Bhutan' , '68' : 'Plurinational State of Bolivia' , '535' : 'Bonaire Sint Eustatius and Saba' , '70' : 'Bosnia and Herzegovina' , '72' : 'Botswana' , '74' : 'Bouvet Island' , '76' : 'Brazil' , '86' : 'British Indian Ocean Territory' , '96' : 'Brunei Darussalam' , '100' : 'Bulgaria' , '854' : 'Burkina Faso' , '108' : 'Burundi' , '116' : 'Cambodia' , '120' : 'Cameroon' , '124' : 'Canada' , '132' : 'Cape Verde' , '136' : 'Cayman Islands' , '140' : 'Central African Republic' , '148' : 'Chad' , '152' : 'Chile' , '156' : 'China' , '162' : 'Christmas Island' , '166' : 'Cocos (Keeling) Islands' , '170' : 'Colombia' , '174' : 'Comoros' , '178' : 'Congo' , '180' : 'the Democratic Republic of the Congo' , '184' : 'Cook Islands' , '188' : 'Costa Rica' , '384' : 'Cote dIvoire' , '191' : 'Croatia' , '192' : 'Cuba' , '531' : 'Curacao' , '196' : 'Cyprus' , '203' : 'Czech Republic' , '208' : 'Denmark' , '262' : 'Djibouti' , '212' : 'Dominica' , '214' : 'Dominican Republic' , '218' : 'Ecuador' , '818' : 'Egypt' , '222' : 'El Salvador' , '226' : 'Equatorial Guinea' , '232' : 'Eritrea' , '233' : 'Estonia' , '231' : 'Ethiopia' , '238' : 'Falkland Islands (Malvinas)' , '234' : 'Faroe Islands' , '242' : 'Fiji' , '246' : 'Finland' , '250' : 'France' , '254' : 'French Guiana' , '258' : 'French Polynesia' , '260' : 'French Southern Territories' , '266' : 'Gabon' , '270' : 'Gambia' , '268' : 'Georgia' , '276' : 'Germany' , '288' : 'Ghana' , '292' : 'Gibraltar' , '300' : 'Greece' , '304' : 'Greenland' , '308' : 'Grenada' , '312' : 'Guadeloupe' , '316' : 'Guam' , '320' : 'Guatemala' , '831' : 'Guernsey' , '324' : 'Guinea' , '624' : 'Guinea-Bissau' , '328' : 'Guyana' , '332' : 'Haiti' , '334' : 'Heard Island and McDonald Islands' , '336' : 'Holy See (Vatican City State)' , '340' : 'Honduras' , '344' : 'Hong Kong' , '348' : 'Hungary' , '352' : 'Iceland' , '356' : 'India' , '360' : 'Indonesia' , '364' : 'Islamic Republic of Iran' , '368' : 'Iraq' , '372' : 'Ireland' , '833' : 'Isle of Man' , '376' : 'Israel' , '380' : 'Italy' , '388' : 'Jamaica' , '392' : 'Japan' , '832' : 'Jersey' , '400' : 'Jordan' , '398' : 'Kazakhstan' , '404' : 'Kenya' , '296' : 'Kiribati' , '408' :  'Democratic Peoples Republic of Korea' , '410'  : 'Republic of Korea' , '414' : 'Kuwait' , '417' : 'Kyrgyzstan' , '418' : 'Lao Peoples Democratic Republic' , '428' : 'Latvia' , '422' : 'Lebanon' , '426' : 'Lesotho' , '430' : 'Liberia' , '434' : 'Libya' , '438' : 'Liechtenstein' , '440' : 'Lithuania' , '442' : 'Luxembourg' , '446' : 'Macao' , '807' : 'the former Yugoslav Republic of Macedonia' , '450' : 'Madagascar' , '454' : 'Malawi' , '458' : 'Malaysia' , '462' : 'Maldives' , '466' : 'Mali' , '470' : 'Malta' , '584' : 'Marshall Islands' , '474' : 'Martinique' , '478' : 'Mauritania' , '480' : 'Mauritius' , '175' : 'Mayotte' , '484' : 'Mexico' , '583' : 'Federated States of Micronesia' , '498' : 'Republic of Maldova' , '492' : 'Monaco' , '496' : 'Mongolia' , '499' : 'Montenegro' , '500' : 'Montserrat' , '504' : 'Morocco' , '508' : 'Mozambique' , '104' : 'Myanmar' , '516' : 'Namibia' , '520' : 'Nauru' , '524' : 'Nepal' , '528' : 'Netherlands' , '540' : 'New Caledonia' , '554' : 'New Zealand' , '558' : 'Nicaragua' , '562' : 'Niger' , '566' : 'Nigeria' , '570' : 'Niue' , '574' : 'Norfolk Island' , '580' : 'Northern Mariana Islands' , '578' : 'Norway' , '512' : 'Oman' , '586' : 'Pakistan' , '585' : 'Palau' , '275' : 'Occupied Palestinian Territory' , '591' : 'Panama' , '598' : 'Papua New Guinea' , '600' : 'Paraguay' , '604' : 'Peru' , '608' : 'Philippines' , '612' : 'Pitcairn' , '616' : 'Poland' , '620' : 'Portugal' , '630' : 'Puerto Rico' , '634' : 'Qatar' , '638' : 'Reunion' , '642' : 'Romania' , '643' : 'Russian Federation' , '646' : 'Rwanda' , '652' : 'Saint Barthelemy' , '654' : 'Saint Helena Ascension and Tristan da Cunha' , '659' : 'Saint Kitts and Nevis' , '662' : 'Saint Lucia' , '663' : 'Saint Martin (French part)' , '666' : 'Saint Pierre and Miquelon' , '670' : 'Saint Vincent and the Grenadines' , '882' : 'Samoa' , '674' : 'San Marino' , '678' : 'Sao Tome and Principe' , '682' : 'Saudi Arabia' , '686' : 'Senegal' , '688' : 'Serbia' , '690' : 'Seychelles' , '694' : 'Sierra Leone' , '702' : 'Singapore' , '534' : 'Sint Maarten (Dutch part)' , '703' : 'Slovakia' , '705' : 'Slovenia' , '90' : 'Solomon Islands' , '706' : 'Somalia' , '710' : 'South Africa' , '239' : 'South Georgia and the South Sandwich Islands' , '728' : 'South Sudan' , '724' : 'Spain' , '144' : 'Sri Lanka' , '729' : 'Sudan' , '740' : 'Suriname' , '744' : 'Svalbard and Jan Mayen' , '748' : 'Swaziland' , '752' : 'Sweden' , '756' : 'Switzerland' , '760' : 'Syrian Arab Republic' , '158' : 'Taiwan Province of China' , '762' : 'Tajikistan' , '834' : 'United Republic of Tanzania' , '764' : 'Thailand' , '626' : 'Timor-Leste' , '768' : 'Togo' , '772' : 'Tokelau' , '776' : 'Tonga' , '780' : 'Trinidad and Tobago' , '788' : 'Tunisia' , '792' : 'Turkey' , '795' : 'Turkmenistan' , '796' : 'Turks and Caicos Islands' , '798' : 'Tuvalu' , '800' : 'Uganda' , '804' : 'Ukraine' , '784' : 'United Arab Emirates' , '826' : 'United Kingdom' , '581' : 'United States Minor Outlying Islands' , '858' : 'Uruguay' , '860' : 'Uzbekistan' , '548' : 'Vanuatu' , '862' : 'Bolivarian Republic of Venezuela' , '704' : 'Viet Nam' , '92' : 'British Virgin Islands' , '850' :  'U.S. Virgin Islands' , '876' : 'Wallis and Futuna' , '732' : 'Western Sahara' , '887' : 'Yemen' , '263' : 'Zimbabwe' , '99' : 'Dont Know'})
fn["sub_bio_f_country"]=sub_bio_f_country

def sub_bio_m_county(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    studydata['sub_bio_m_county']=studydata.sub_bio_m_county.astype(str).replace({'840' : 'United States' , '4' : 'Afghanistan' , '248' : 'Aland Islands' , '8' : 'Albania' , '12' : 'Algeria' , '16' : 'American Samoa' , '20' : 'Andorra' , '24' : 'Angola' , '660' : 'Anguilla' , '10' : 'Antarctica' , '28' : 'Antigua and Barbuda' , '32' : 'Argentina' , '51' : 'Armenia' , '533' : 'Aruba' , '36' : 'Australia' , '40' : 'Austria' , '31' : 'Azerbaijan' , '44' : 'Bahamas' , '48' : 'Bahrain' , '50' : 'Bangladesh' , '52' : 'Barbados' , '112' : 'Belarus' , '56' : 'Belgium' , '84' : 'Belize' , '204' : 'Benin' , '60' : 'Bermuda' , '64' : 'Bhutan' , '68' : 'Plurinational State of Bolivia' , '535' : 'Bonaire Sint Eustatius and Saba' , '70' : 'Bosnia and Herzegovina' , '72' : 'Botswana' , '74' : 'Bouvet Island' , '76' : 'Brazil' , '86' : 'British Indian Ocean Territory' , '96' : 'Brunei Darussalam' , '100' : 'Bulgaria' , '854' : 'Burkina Faso' , '108' : 'Burundi' , '116' : 'Cambodia' , '120' : 'Cameroon' , '124' : 'Canada' , '132' : 'Cape Verde' , '136' : 'Cayman Islands' , '140' : 'Central African Republic' , '148' : 'Chad' , '152' : 'Chile' , '156' : 'China' , '162' : 'Christmas Island' , '166' : 'Cocos (Keeling) Islands' , '170' : 'Colombia' , '174' : 'Comoros' , '178' : 'Congo' , '180' : 'the Democratic Republic of the Congo' , '184' : 'Cook Islands' , '188' : 'Costa Rica' , '384' : 'Cote dIvoire' , '191' : 'Croatia' , '192' : 'Cuba' , '531' : 'Curacao' , '196' : 'Cyprus' , '203' : 'Czech Republic' , '208' : 'Denmark' , '262' : 'Djibouti' , '212' : 'Dominica' , '214' : 'Dominican Republic' , '218' : 'Ecuador' , '818' : 'Egypt' , '222' : 'El Salvador' , '226' : 'Equatorial Guinea' , '232' : 'Eritrea' , '233' : 'Estonia' , '231' : 'Ethiopia' , '238' : 'Falkland Islands (Malvinas)' , '234' : 'Faroe Islands' , '242' : 'Fiji' , '246' : 'Finland' , '250' : 'France' , '254' : 'French Guiana' , '258' : 'French Polynesia' , '260' : 'French Southern Territories' , '266' : 'Gabon' , '270' : 'Gambia' , '268' : 'Georgia' , '276' : 'Germany' , '288' : 'Ghana' , '292' : 'Gibraltar' , '300' : 'Greece' , '304' : 'Greenland' , '308' : 'Grenada' , '312' : 'Guadeloupe' , '316' : 'Guam' , '320' : 'Guatemala' , '831' : 'Guernsey' , '324' : 'Guinea' , '624' : 'Guinea-Bissau' , '328' : 'Guyana' , '332' : 'Haiti' , '334' : 'Heard Island and McDonald Islands' , '336' : 'Holy See (Vatican City State)' , '340' : 'Honduras' , '344' : 'Hong Kong' , '348' : 'Hungary' , '352' : 'Iceland' , '356' : 'India' , '360' : 'Indonesia' , '364' : 'Islamic Republic of Iran' , '368' : 'Iraq' , '372' : 'Ireland' , '833' : 'Isle of Man' , '376' : 'Israel' , '380' : 'Italy' , '388' : 'Jamaica' , '392' : 'Japan' , '832' : 'Jersey' , '400' : 'Jordan' , '398' : 'Kazakhstan' , '404' : 'Kenya' , '296' : 'Kiribati' , '408' :  'Democratic Peoples Republic of Korea' , '410'  : 'Republic of Korea' , '414' : 'Kuwait' , '417' : 'Kyrgyzstan' , '418' : 'Lao Peoples Democratic Republic' , '428' : 'Latvia' , '422' : 'Lebanon' , '426' : 'Lesotho' , '430' : 'Liberia' , '434' : 'Libya' , '438' : 'Liechtenstein' , '440' : 'Lithuania' , '442' : 'Luxembourg' , '446' : 'Macao' , '807' : 'the former Yugoslav Republic of Macedonia' , '450' : 'Madagascar' , '454' : 'Malawi' , '458' : 'Malaysia' , '462' : 'Maldives' , '466' : 'Mali' , '470' : 'Malta' , '584' : 'Marshall Islands' , '474' : 'Martinique' , '478' : 'Mauritania' , '480' : 'Mauritius' , '175' : 'Mayotte' , '484' : 'Mexico' , '583' : 'Federated States of Micronesia' , '498' : 'Republic of Maldova' , '492' : 'Monaco' , '496' : 'Mongolia' , '499' : 'Montenegro' , '500' : 'Montserrat' , '504' : 'Morocco' , '508' : 'Mozambique' , '104' : 'Myanmar' , '516' : 'Namibia' , '520' : 'Nauru' , '524' : 'Nepal' , '528' : 'Netherlands' , '540' : 'New Caledonia' , '554' : 'New Zealand' , '558' : 'Nicaragua' , '562' : 'Niger' , '566' : 'Nigeria' , '570' : 'Niue' , '574' : 'Norfolk Island' , '580' : 'Northern Mariana Islands' , '578' : 'Norway' , '512' : 'Oman' , '586' : 'Pakistan' , '585' : 'Palau' , '275' : 'Occupied Palestinian Territory' , '591' : 'Panama' , '598' : 'Papua New Guinea' , '600' : 'Paraguay' , '604' : 'Peru' , '608' : 'Philippines' , '612' : 'Pitcairn' , '616' : 'Poland' , '620' : 'Portugal' , '630' : 'Puerto Rico' , '634' : 'Qatar' , '638' : 'Reunion' , '642' : 'Romania' , '643' : 'Russian Federation' , '646' : 'Rwanda' , '652' : 'Saint Barthelemy' , '654' : 'Saint Helena Ascension and Tristan da Cunha' , '659' : 'Saint Kitts and Nevis' , '662' : 'Saint Lucia' , '663' : 'Saint Martin (French part)' , '666' : 'Saint Pierre and Miquelon' , '670' : 'Saint Vincent and the Grenadines' , '882' : 'Samoa' , '674' : 'San Marino' , '678' : 'Sao Tome and Principe' , '682' : 'Saudi Arabia' , '686' : 'Senegal' , '688' : 'Serbia' , '690' : 'Seychelles' , '694' : 'Sierra Leone' , '702' : 'Singapore' , '534' : 'Sint Maarten (Dutch part)' , '703' : 'Slovakia' , '705' : 'Slovenia' , '90' : 'Solomon Islands' , '706' : 'Somalia' , '710' : 'South Africa' , '239' : 'South Georgia and the South Sandwich Islands' , '728' : 'South Sudan' , '724' : 'Spain' , '144' : 'Sri Lanka' , '729' : 'Sudan' , '740' : 'Suriname' , '744' : 'Svalbard and Jan Mayen' , '748' : 'Swaziland' , '752' : 'Sweden' , '756' : 'Switzerland' , '760' : 'Syrian Arab Republic' , '158' : 'Taiwan Province of China' , '762' : 'Tajikistan' , '834' : 'United Republic of Tanzania' , '764' : 'Thailand' , '626' : 'Timor-Leste' , '768' : 'Togo' , '772' : 'Tokelau' , '776' : 'Tonga' , '780' : 'Trinidad and Tobago' , '788' : 'Tunisia' , '792' : 'Turkey' , '795' : 'Turkmenistan' , '796' : 'Turks and Caicos Islands' , '798' : 'Tuvalu' , '800' : 'Uganda' , '804' : 'Ukraine' , '784' : 'United Arab Emirates' , '826' : 'United Kingdom' , '581' : 'United States Minor Outlying Islands' , '858' : 'Uruguay' , '860' : 'Uzbekistan' , '548' : 'Vanuatu' , '862' : 'Bolivarian Republic of Venezuela' , '704' : 'Viet Nam' , '92' : 'British Virgin Islands' , '850' :  'U.S. Virgin Islands' , '876' : 'Wallis and Futuna' , '732' : 'Western Sahara' , '887' : 'Yemen' , '263' : 'Zimbabwe' , '99' : 'Dont Know'})
fn["sub_bio_m_county"]=sub_bio_m_county

def sub_mgrade(studydata, column, context):
    """Please recode 13 as 14 (for "High school graduate"), 14 as 13 (for "GED or equivalent"), 15 as 16 (for "Some college, no degree"), 16 as 17 (for "Associate degree: occupational/technical/vocational program"), 17 as 18 (for "Associate degree: academic program"), 18 as 20 (for "Bachelor degree (e.g., BA, AB, BS, BBA)"), 19 as 22 (for "Master's degree (e.g., MA, MS, MEng, MEd, MBA)"), 20 as 23 (for "Professional school degree (e.g., MD, DDS, DVM, JD)"), and 21 as 24 (for "Doctoral degree (e.g., PhD, EdD)")."""
    studydata['sub_mgradeswitch']=studydata.sub_mgrade.astype(str).replace({'13':'14','14':'13','15':'16','16':'17','17':'18','18':'20','19':'22','20':'23','21':'24'})
    studydata['sub_mgrade']=studydata.sub_mgradeswitch
fn["sub_mgrade"]=sub_mgrade

def sub_fgrade(studydata, column, context):
    """Please recode 13 as 14 (for "High school graduate"), 14 as 13 (for "GED or equivalent"), 15 as 16 (for "Some college, no degree"), 16 as 17 (for "Associate degree: occupational/technical/vocational program"), 17 as 18 (for "Associate degree: academic program"), 18 as 20 (for "Bachelor degree (e.g., BA, AB, BS, BBA)"), 19 as 22 (for "Master's degree (e.g., MA, MS, MEng, MEd, MBA)"), 20 as 23 (for "Professional school degree (e.g., MD, DDS, DVM, JD)"), and 21 as 24 (for "Doctoral degree (e.g., PhD, EdD)")."""
    studydata['sub_fgradeswitch']=studydata.sub_fgrade.astype(str).replace({'13':'14','14':'13','15':'16','16':'17','17':'18','18':'20','19':'22','20':'23','21':'24'})
    studydata['sub_fgrade']=studydata.sub_fgradeswitch
fn["sub_fgrade"]=sub_fgrade

def dummy_var14(studydata, column, context):
    """Please specify a time range of "Past 4 weeks" for all records."""
    print('performed dummy_var14')
    studydata['version_form']='Past 4 weeks'
fn["dummy_var14"]=dummy_var14

def mctq_free9(studydata, column, context):
    """Please combine mctq_free9 and mctq_free10 under one column (either name would be fine). Please also convert mctq_free9's numeric codes to the text strings they represent."""
    studydata['mctq_free9']=studydata.mctq_free9.astype(str)
    studydata['mctq_free9']=studydata.mctq_free9.str.replace('1','Familymembers/pet(s)')
    studydata['mctq_free9']=studydata.mctq_free9.str.replace('2','Hobbies')
    studydata['mctq_free9']=studydata.mctq_free9.str.replace('3','Other: ')
fn["mctq_free9"]=mctq_free9

def mctq_free10(studydata, column, context):
    """Please combine mctq_free9 and mctq_free10 under one column (either name would be fine). Please also convert mctq_free9's numeric codes to the text strings they represent."""
    studydata.mctq_free10=studydata.mctq_free9+studydata.mctq_free10
fn["mctq_free10"]=mctq_free10

def neo1(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo1=pd.to_numeric(studydata.neo1,errors='coerce')-1
    studydata.neo1=neo1.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo1"]=neo1

def neo2(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo2=pd.to_numeric(studydata.neo2,errors='coerce')-1
    studydata.neo2=neo2.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo2"]=neo2

def neo3(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale, reverse-coding where the manual calls for it, and recalculating scores accordingly."""
    neo3=4-(pd.to_numeric(studydata.neo3,errors='coerce')-1)
    studydata.neo3=neo3.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo3"]=neo3

def neo4(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo4=pd.to_numeric(studydata.neo4,errors='coerce')-1
    studydata.neo4=neo4.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo4"]=neo4

def neo5(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo5=pd.to_numeric(studydata.neo5,errors='coerce')-1
    studydata.neo5=neo5.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo5"]=neo5

def neo6(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo6=pd.to_numeric(studydata.neo6,errors='coerce')-1
    studydata.neo6=neo6.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo6"]=neo6

def neo7(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo7=pd.to_numeric(studydata.neo7,errors='coerce')-1
    studydata.neo7=neo7.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo7"]=neo7

def neo8(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale, reverse-coding where the manual calls for it, and recalculating scores accordingly."""
    neo8=4-(pd.to_numeric(studydata.neo8,errors='coerce')-1)
    studydata.neo8=neo8.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo8"]=neo8

def neo9(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo9=pd.to_numeric(studydata.neo9,errors='coerce')-1
    studydata.neo9=neo9.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo9"]=neo9

def neo10(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo10=pd.to_numeric(studydata.neo10,errors='coerce')-1
    studydata.neo10=neo10.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo10"]=neo10

def neo11(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo11=pd.to_numeric(studydata.neo11,errors='coerce')-1
    studydata.neo11=neo11.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo11"]=neo11

def neo12(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo12=pd.to_numeric(studydata.neo12,errors='coerce')-1
    studydata.neo12=neo12.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo12"]=neo12

def neo13(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo13=pd.to_numeric(studydata.neo13,errors='coerce')-1
    studydata.neo13=neo13.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo13"]=neo13

def neo14(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo14=pd.to_numeric(studydata.neo14,errors='coerce')-1
    studydata.neo14=neo14.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo14"]=neo14

def neo15(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo15=pd.to_numeric(studydata.neo15,errors='coerce')-1
    studydata.neo15=neo15.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo15"]=neo15

def neo16(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo16=pd.to_numeric(studydata.neo16,errors='coerce')-1
    studydata.neo16=neo16.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo16"]=neo16

def neo17(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo17=pd.to_numeric(studydata.neo17,errors='coerce')-1
    studydata.neo17=neo17.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo17"]=neo17

def neo18(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo18=pd.to_numeric(studydata.neo18,errors='coerce')-1
    studydata.neo18=neo18.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo18"]=neo18

def neo19(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo19=pd.to_numeric(studydata.neo19,errors='coerce')-1
    studydata.neo19=neo19.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo19"]=neo19

def neo20(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo20=pd.to_numeric(studydata.neo20,errors='coerce')-1
    studydata.neo20=neo20.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo20"]=neo20

def neo21(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo21=pd.to_numeric(studydata.neo21,errors='coerce')-1
    studydata.neo21=neo21.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo21"]=neo21

def neo22(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo22=pd.to_numeric(studydata.neo22,errors='coerce')-1
    studydata.neo22=neo22.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo22"]=neo22

def neo23(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo23=pd.to_numeric(studydata.neo23,errors='coerce')-1
    studydata.neo23=neo23.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo23"]=neo23

def neo24(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo24=pd.to_numeric(studydata.neo24,errors='coerce')-1
    studydata.neo24=neo24.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo24"]=neo24

def neo25(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo25=pd.to_numeric(studydata.neo25,errors='coerce')-1
    studydata.neo25=neo25.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo25"]=neo25

def neo26(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo26=pd.to_numeric(studydata.neo26,errors='coerce')-1
    studydata.neo26=neo26.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo26"]=neo26

def neo27(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo27=pd.to_numeric(studydata.neo27,errors='coerce')-1
    studydata.neo27=neo27.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo27"]=neo27

def neo28(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo28=pd.to_numeric(studydata.neo28,errors='coerce')-1
    studydata.neo28=neo28.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo28"]=neo28

def neo29(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale, reverse-coding where the manual calls for it, and recalculating scores accordingly."""
    neo29=4-(pd.to_numeric(studydata.neo29,errors='coerce')-1)
    studydata.neo29=neo29.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo29"]=neo29

def neo30(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo30=pd.to_numeric(studydata.neo30,errors='coerce')-1
    studydata.neo30=neo30.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo30"]=neo30

def neo31(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo31=pd.to_numeric(studydata.neo31,errors='coerce')-1
    studydata.neo31=neo31.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo31"]=neo31

def neo32(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo32=pd.to_numeric(studydata.neo32,errors='coerce')-1
    studydata.neo32=neo32.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo32"]=neo32

def neo33(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo33=pd.to_numeric(studydata.neo33,errors='coerce')-1
    studydata.neo33=neo33.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo33"]=neo33

def neo34(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo34=pd.to_numeric(studydata.neo34,errors='coerce')-1
    studydata.neo34=neo34.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo34"]=neo34

def neo35(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo35=pd.to_numeric(studydata.neo35,errors='coerce')-1
    studydata.neo35=neo35.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo35"]=neo35

def neo36(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo36=pd.to_numeric(studydata.neo36,errors='coerce')-1
    studydata.neo36=neo36.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo36"]=neo36

def neo37(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo37=pd.to_numeric(studydata.neo37,errors='coerce')-1
    studydata.neo37=neo37.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo37"]=neo37

def neo38(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale, reverse-coding where the manual calls for it, and recalculating scores accordingly."""
    neo38=4-(pd.to_numeric(studydata.neo38,errors='coerce')-1)
    studydata.neo38=neo38.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo38"]=neo38

def neo39(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo39=pd.to_numeric(studydata.neo39,errors='coerce')-1
    studydata.neo39=neo39.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo39"]=neo39

def neo40(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo40=pd.to_numeric(studydata.neo40,errors='coerce')-1
    studydata.neo40=neo40.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo40"]=neo40

def neo41(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo41=pd.to_numeric(studydata.neo41,errors='coerce')-1
    studydata.neo41=neo41.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo41"]=neo41

def neo42(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo42=pd.to_numeric(studydata.neo42,errors='coerce')-1
    studydata.neo42=neo42.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo42"]=neo42

def neo43(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo43=pd.to_numeric(studydata.neo43,errors='coerce')-1
    studydata.neo43=neo43.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo43"]=neo43

def neo44(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo44=pd.to_numeric(studydata.neo44,errors='coerce')-1
    studydata.neo44=neo44.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo44"]=neo44

def neo45(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo45=pd.to_numeric(studydata.neo45,errors='coerce')-1
    studydata.neo45=neo45.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo45"]=neo45

def neo46(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo46=pd.to_numeric(studydata.neo46,errors='coerce')-1
    studydata.neo46=neo46.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo46"]=neo46

def neo47(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo47=pd.to_numeric(studydata.neo47,errors='coerce')-1
    studydata.neo47=neo47.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo47"]=neo47

def neo48(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo48=pd.to_numeric(studydata.neo48,errors='coerce')-1
    studydata.neo48=neo48.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo48"]=neo48

def neo49(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo49=pd.to_numeric(studydata.neo49,errors='coerce')-1
    studydata.neo49=neo49.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo49"]=neo49

def neo50(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo50=pd.to_numeric(studydata.neo50,errors='coerce')-1
    studydata.neo50=neo50.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo50"]=neo50

def neo51(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo51=pd.to_numeric(studydata.neo51,errors='coerce')-1
    studydata.neo51=neo51.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo51"]=neo51

def neo52(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo52=pd.to_numeric(studydata.neo52,errors='coerce')-1
    studydata.neo52=neo52.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo52"]=neo52

def neo53(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo53=pd.to_numeric(studydata.neo53,errors='coerce')-1
    studydata.neo53=neo53.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo53"]=neo53

def neo54(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo54=pd.to_numeric(studydata.neo54,errors='coerce')-1
    studydata.neo54=neo54.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo54"]=neo54

def neo55(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo55=pd.to_numeric(studydata.neo55,errors='coerce')-1
    studydata.neo55=neo55.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo55"]=neo55

def neo56(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo56=pd.to_numeric(studydata.neo56,errors='coerce')-1
    studydata.neo56=neo56.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo56"]=neo56

def neo57(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo57=pd.to_numeric(studydata.neo57,errors='coerce')-1
    studydata.neo57=neo57.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo57"]=neo57

def neo58(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo58=pd.to_numeric(studydata.neo58,errors='coerce')-1
    studydata.neo58=neo58.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo58"]=neo58

def neo59(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo59=pd.to_numeric(studydata.neo59,errors='coerce')-1
    studydata.neo59=neo59.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo59"]=neo59

def neo60(studydata, column, context):
    """Please decrement your 1::5 scale to a 0::4 scale"""
    neo60=pd.to_numeric(studydata.neo60,errors='coerce')-1
    studydata.neo60=neo60.fillna(-99).astype(int).astype(str).str.replace('-99','')
fn["neo60"]=neo60

def dummy_var15(studydata, column, context):
    """Please use the 'version_form' column to label all rows "S7up Self Report"."""
    studydata['version_form']='S7up Self Report'
fn["dummy_var15"]=dummy_var15

def ale1(studydata, column, context):
    """ """
    pass
fn["ale1"]=ale1


fn["ale1_2"]=__increment_0_to_2
fn["ale2_2"]=__increment_0_to_2
fn["ale3_2"]=__increment_0_to_2
fn["ale4_2"]=__increment_0_to_2
fn["ale5_2"]=__increment_0_to_2
fn["ale6_2"]=__increment_0_to_2
fn["ale7_2"]=__increment_0_to_2
fn["ale8_2"]=__increment_0_to_2
fn["ale9_2"]=__increment_0_to_2
fn["ale10_2"]=__increment_0_to_2
fn["ale11_2"]=__increment_0_to_2
fn["ale12_2"]=__increment_0_to_2
fn["ale13_2"]=__increment_0_to_2
fn["ale14_2"]=__increment_0_to_2
fn["ale15_2"]=__increment_0_to_2
fn["ale16_2"]=__increment_0_to_2
fn["ale17_2"]=__increment_0_to_2
fn["ale18_2"]=__increment_0_to_2
fn["ale19_2"]=__increment_0_to_2
fn["ale20_2"]=__increment_0_to_2
fn["ale21_2"]=__increment_0_to_2
fn["ale22_2"]=__increment_0_to_2
fn["ale23_2"]=__increment_0_to_2
fn["ale24_2"]=__increment_0_to_2
fn["ale25_2"]=__increment_0_to_2

def dummy_var16(studydata, column, context):
    """Please use the 'version_form' column to label each row "Past year"."""
    studydata['version_form']='Past year'
fn["dummy_var16"]=dummy_var16

def nida_y_tobaco3(studydata, column, context):
    """Please recode 999 as 97."""
    return column.replace({999: 97})
fn["nida_y_tobaco3"]=nida_y_tobaco3

def nida_y_tobaco6b(studydata, column, context):
    """Please recode 3 as 2 and 6 as 3."""
    return column.replace({3: 2, 6: 3})
fn["nida_y_tobaco6b"]=nida_y_tobaco6b

def nida_y_tobaco7(studydata, column, context):
    """Please recode 1 as 2, 2 as 3, and 6 as 4."""
    return column.replace({
        1: 2,
        2: 3,
        6: 4,
    })
fn["nida_y_tobaco7"]=nida_y_tobaco7

def __recode_1_2_as_yes_no(studydata, column, context):
    """Please recode 1 as Yes and 2 as No."""
    return column.replace({
        1: 'Yes',
        2: 'No',
    })

fn["nida_y_drug1"]=__recode_1_2_as_yes_no
fn["nida_y_drug2"]=__recode_1_2_as_yes_no
fn["nida_y_drug3"]=__recode_1_2_as_yes_no
fn["nida_y_drug4"]=__recode_1_2_as_yes_no
fn["nida_y_drug5"]=__recode_1_2_as_yes_no
fn["nida_y_drug6"]=__recode_1_2_as_yes_no
fn["nida_y_drug7"]=__recode_1_2_as_yes_no
fn["nida_y_drug8"]=__recode_1_2_as_yes_no
fn["nida_y_drug9"]=__recode_1_2_as_yes_no
fn["nida_y_drug10"]=__recode_1_2_as_yes_no

def pds_sub_score(studydata, column, context):
    """Please split this column into two separate columns. Male participants' data can go to 'pds_pv_boy_tanner'. Female participants' data belong in 'pds_pv_girl_tanner'."""
    studydata['pds_pv_girl_tanner'] = column.where(studydata.gender=='F')
    studydata['pds_pv_boy_tanner'] = column.where(studydata.gender=='M')
fn["pds_sub_score"]=pds_sub_score

def mstrl_sub1a(studydata, column, context):
    """Please change numeric codes to the text strings they represent."""
    studydata.loc[studydata.mstrl_sub1a=='1','mstrl_sub1a']='Hypothyroidism'
    studydata.loc[studydata.mstrl_sub1a=='2','mstrl_sub1a']='No hypothyroidism'
fn["mstrl_sub1a"]=mstrl_sub1a

def mstrl_sub1b(studydata, column, context):
    """Please change numeric codes to the text strings they represent."""
    studydata.loc[studydata.mstrl_sub1b=='1','mstrl_sub1b']='Hyperthyroidism'
    studydata.loc[studydata.mstrl_sub1b=='2','mstrl_sub1b']='No hyperthyroidism'
fn["mstrl_sub1b"]=mstrl_sub1b

def __prepend_age_at_onset(studydata, column, context):
    """Please prepend "Age at onset: " to ages."""
    return column.mask(column.notna(), 'Age at onset: ' + column.astype(str))

fn["mstrl_sub1c_age"]=__prepend_age_at_onset

def dummy_var13(studydata, column, context):
    """Please indicate "Short Form" for each row using the column 'version_form'."""
    studydata['version_form']='Short Form'
fn["dummy_var13"]=dummy_var13

def dummy_var17(studydata, column, context):
    """Please indicate "Parent" for each row using the column 'version_form'."""
    studydata['version_form']='Parent'
fn["dummy_var17"]=dummy_var17

def srsa_total_raw(studydata, column, context):
    """Please split total raw scores by sex. Females' scores can go in 'female_rawscoreall'. Males' scores can go in 'male_rawscoreall'."""
    studydata['female_rawscoreall']=studydata.srsa_total_raw
    studydata.loc[studydata.gender!='F','female_rawscoreall']=''
fn["srsa_total_raw"]=srsa_total_raw

def dummy18(studydata, column, context):
    """Please split total raw scores by sex. Females' scores can go in 'female_rawscoreall'. Males' scores can go in 'male_rawscoreall'."""
    studydata['male_rawscoreall']=studydata.srsa_total_raw
    studydata.loc[studydata.gender!='M','male_rawscoreall']=''
fn["dummy18"]=dummy18

def srsa_total_tscore(studydata, column, context):
    """Please split total T-scores by sex. Males' scores can go in 'male_tscoreall'. Females' scores can go in 'female_tscoreall'."""
    studydata['male_tscoreall']=studydata.srsa_total_tscore
    studydata.loc[studydata.gender!='M','male_tscoreall']=''
fn["srsa_total_tscore"]=srsa_total_tscore

def dummy19(studydata, column, context):
    """Please split total T-scores by sex. Males' scores can go in 'male_tscoreall'. Females' scores can go in 'female_tscoreall'."""
    studydata['female_tscoreall']=studydata.srsa_total_tscore
    studydata.loc[studydata.gender!='F','female_tscoreall']=''
fn["dummy19"]=dummy19

def dummy_var1(studydata, column, context):
    """Please use the 'version_form' column to specify a time range of the "Self report, Past 6 months" for each row of data."""
    studydata['version_form']='Self report, Past 6 months'
fn["dummy_var1"]=dummy_var1

def dummy_var2(studydata, column, context):
    """Please fill all cells with 999 for this column, unless the respondent is known."""
    studydata['respond']='3'
fn["dummy_var2"]=dummy_var2

def dummy_var3(studydata, column, context):
    """Please fill all cells with 999 for this column, unless the respondent is known."""
    studydata['respond_detail']='999'
fn["dummy_var3"]=dummy_var3

def dummy_var4(studydata, column, context):
    """Please specify a cohort/group/diagnosis for participants in this column. If this is not applicable, then please fill each cell with 999."""
    studydata['phenotype']='999'
fn["dummy_var4"]=dummy_var4

def cbq2(studydata, column, context):
    """Please rename this column 'cbq31' to avoid a naming conflict."""
    pass
fn["cbq2"]=cbq2

def cbq9(studydata, column, context):
    """Please rename this column 'cbq11' to avoid a naming conflict."""
    pass
fn["cbq9"]=cbq9

def cbq10(studydata, column, context):
    """Please rename this column 'cbq09' to avoid a naming conflict."""
    pass
fn["cbq10"]=cbq10

def cbq11(studydata, column, context):
    """Please rename this column 'cbq_17' to avoid a naming conflict."""
    pass
fn["cbq11"]=cbq11

def cbq12(studydata, column, context):
    """Please rename this column 'cbq49' to avoid a naming conflict."""
    pass
fn["cbq12"]=cbq12

def cbq14(studydata, column, context):
    """Please rename this column 'cbq77' to avoid a naming conflict."""
    pass
fn["cbq14"]=cbq14

def cbq15(studydata, column, context):
    """Please rename this column 'cbq71' to avoid a naming conflict."""
    pass
fn["cbq15"]=cbq15

def cbq16(studydata, column, context):
    """Please rename this column 'cbq62' to avoid a naming conflict."""
    pass
fn["cbq16"]=cbq16

def cbq17(studydata, column, context):
    """Please rename this column 'cbq127' to avoid a naming conflict."""
    pass
fn["cbq17"]=cbq17

def cbq18(studydata, column, context):
    """Please rename this column 'cbq69' to avoid a naming conflict."""
    pass
fn["cbq18"]=cbq18

def cbq21(studydata, column, context):
    """Please rename this column 'cbq03' to avoid a naming conflict."""
    pass
fn["cbq21"]=cbq21

def cbq23(studydata, column, context):
    """Please rename this column 'cbq65' to avoid a naming conflict."""
    pass
fn["cbq23"]=cbq23

def cbq24(studydata, column, context):
    """Please rename this column 'cbq54' to avoid a naming conflict."""
    pass
fn["cbq24"]=cbq24

def cbq25(studydata, column, context):
    """Please rename this column 'cbq84' to avoid a naming conflict."""
    pass
fn["cbq25"]=cbq25

def cbq26(studydata, column, context):
    """Please rename this column 'cbq34' to avoid a naming conflict."""
    pass
fn["cbq26"]=cbq26

def cbq27(studydata, column, context):
    """Please rename this column 'cbq191' to avoid a naming conflict."""
    pass
fn["cbq27"]=cbq27

def cbq28(studydata, column, context):
    """Please rename this column 'cbq028' to avoid a naming conflict."""
    pass
fn["cbq28"]=cbq28

def cbq30(studydata, column, context):
    """Please rename this column 'cbq170' to avoid a naming conflict."""
    pass
fn["cbq30"]=cbq30

def cbq31(studydata, column, context):
    """Please rename this column 'cbq147' to avoid a naming conflict."""
    pass
fn["cbq31"]=cbq31

def cbq32(studydata, column, context):
    """Please rename this column 'cbq39' to avoid a naming conflict."""
    pass
fn["cbq32"]=cbq32

def cbq33(studydata, column, context):
    """Please rename this column 'cbq_94' to avoid a naming conflict."""
    pass
fn["cbq33"]=cbq33

def cbq34(studydata, column, context):
    """Please rename this column 'cbq168' to avoid a naming conflict."""
    pass
fn["cbq34"]=cbq34

def cbq35(studydata, column, context):
    """Please rename this column 'cbq33' to avoid a naming conflict."""
    pass
fn["cbq35"]=cbq35

def p_c_gender(studydata, column, context):
    """Please decrement values 1::6 to 0::5. Values of 7 and 8 can remain the same."""
    pass
fn["p_c_gender"]=p_c_gender

def p_c_country(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_c_country"]=p_c_country

def p_gender(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_gender"]=p_gender

def p_gender_different(studydata, column, context):
    """Please combine these responses with those from 'p_gender' in a single column with either name."""
    pass
fn["p_gender_different"]=p_gender_different

def p_race(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_race"]=p_race

def p_country(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_country"]=p_country

def p_bio_f_country(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_bio_f_country"]=p_bio_f_country

def p_bio_m_county(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_bio_m_county"]=p_bio_m_county

def p_marriage(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_marriage"]=p_marriage

def p_grade(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_grade"]=p_grade

def p_job(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["p_job"]=p_job

def ptner_grade(studydata, column, context):
    """Please convert numeric codes to the text strings they represent."""
    pass
fn["ptner_grade"]=ptner_grade

def family_income(studydata, column, context):
    """Please convert the code of 999999 to -999999, as 999999 could be an actual value."""
    pass
fn["family_income"]=family_income

def psqi10(studydata, column, context):
    """Please rename this column 'parent_sleep20'."""
    pass
fn["psqi10"]=psqi10

def psqi3(studydata, column, context):
    """Please rename this column 'psqip3'."""
    pass
fn["psqi3"]=psqi3

def psqi4(studydata, column, context):
    """Please rename this column 'psqip4'."""
    pass
fn["psqi4"]=psqi4

def psqi5a(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5a"]=psqi5a

def psqi5b(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5b"]=psqi5b

def psqi5c(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5c"]=psqi5c

def psqi5d(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5d"]=psqi5d

def psqi5e(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5e"]=psqi5e

def psqi5f(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5f"]=psqi5f

def psqi5g(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5g"]=psqi5g

def psqi5h(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5h"]=psqi5h

def psqi5i(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale."""
    pass
fn["psqi5i"]=psqi5i

def psqi5j_2(studydata, column, context):
    """Please increment your 0::3 scale to a 1::4 scale and rename this column 'psqi6b_5'."""
    pass
fn["psqi5j_2"]=psqi5j_2

def devhx_8_prescript_med(studydata, column, context):
    """Please recode 0 as 999 (for "Don't Know")."""
    pass
fn["devhx_8_prescript_med"]=devhx_8_prescript_med

def devhx_9_prescript_med(studydata, column, context):
    """Please recode 0 as 999 (for "Don't Know")."""
    pass
fn["devhx_9_prescript_med"]=devhx_9_prescript_med

def pds_p_g5a(studydata, column, context):
    """Please recode 1 as 2 (for "No")."""
    pass
fn["pds_p_g5a"]=pds_p_g5a

def pds_p_mss_bcontrol(studydata, column, context):
    """Please recode 2 as 0 (for "No")."""
    pass
fn["pds_p_mss_bcontrol"]=pds_p_mss_bcontrol

def pds_p_score(studydata, column, context):
    """Please split this field between 'pds_pv_boy_tanner' for boys and 'pds_pv_girl_tanner' for girls."""
    pass
fn["pds_p_score"]=pds_p_score

def mstrl_p1a(studydata, column, context):
    """Please convert these numeric codes to the text strings they represent."""
    pass
fn["mstrl_p1a"]=mstrl_p1a

def mstrl_p1b(studydata, column, context):
    """Please convert these numeric codes to the text strings they represent."""
    pass
fn["mstrl_p1b"]=mstrl_p1b

def __prepend_onset(studydata, column, context):
    """Please prepend "Onset: " to ages."""
    return column.mask(column.notna(), 'Onset: ' + column.astype(str))

fn["mstrl_p1c_age"]=__prepend_onset

def upps_p1(studydata, column, context):
    """Please rename this column 'phenx_upps_p_1' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p1"]=upps_p1

def upps_p2(studydata, column, context):
    """Please rename this column 'phenx_upps_p_2' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p2"]=upps_p2

def upps_p3(studydata, column, context):
    """Please rename this column 'upps_p4' to avoid a naming conflict. """
    pass
fn["upps_p3"]=upps_p3

def upps_p4(studydata, column, context):
    """Please rename this column 'phenx_upps_p_4' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p4"]=upps_p4

def upps_p5(studydata, column, context):
    """Please rename this column 'upps_p14' to avoid a naming conflict. """
    pass
fn["upps_p5"]=upps_p5

def upps_p6(studydata, column, context):
    """Please rename this column 'upps_p16' to avoid a naming conflict. """
    pass
fn["upps_p6"]=upps_p6

def upps_p7(studydata, column, context):
    """Please rename this column 'phenx_upps_p_7' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p7"]=upps_p7

def upps_p8(studydata, column, context):
    """Please rename this column 'upps_p18' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p8"]=upps_p8

def upps_p9(studydata, column, context):
    """Please rename this column 'upps_p19' to avoid a naming conflict. """
    pass
fn["upps_p9"]=upps_p9

def upps_p10(studydata, column, context):
    """Please rename this column 'upps_p21' to avoid a naming conflict. """
    pass
fn["upps_p10"]=upps_p10

def upps_p11(studydata, column, context):
    """Please rename this column 'phenx_upps_p_11' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p11"]=upps_p11

def upps_p12(studydata, column, context):
    """Please rename this column 'upps_p23' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p12"]=upps_p12

def upps_p13(studydata, column, context):
    """Please rename this column 'phenx_upps_p_13' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p13"]=upps_p13

def upps_p14(studydata, column, context):
    """Please rename this column 'phenx_upps_p_14' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p14"]=upps_p14

def upps_p15(studydata, column, context):
    """Please rename this column 'upps_p27' to avoid a naming conflict. """
    pass
fn["upps_p15"]=upps_p15

def upps_p16(studydata, column, context):
    """Please rename this column 'upps_p28' to avoid a naming conflict. """
    pass
fn["upps_p16"]=upps_p16

def upps_p17(studydata, column, context):
    """Please rename this column 'phenx_upps_p_17' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p17"]=upps_p17

def upps_p18(studydata, column, context):
    """Please rename this column 'phenx_upps_p_18' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p18"]=upps_p18

def upps_p19(studydata, column, context):
    """Please rename this column 'upps_p32' to avoid a naming conflict. """
    pass
fn["upps_p19"]=upps_p19

def upps_p20(studydata, column, context):
    """Please rename this column 'phenx_upps_p_20' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p20"]=upps_p20

def upps_p21(studydata, column, context):
    """Please rename this column 'phenx_upps_p_21' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p21"]=upps_p21

def upps_p22(studydata, column, context):
    """Please rename this column 'upps_p37' to avoid a naming conflict. """
    pass
fn["upps_p22"]=upps_p22

def upps_p23(studydata, column, context):
    """Please rename this column 'upps_p38' to avoid a naming conflict. """
    pass
fn["upps_p23"]=upps_p23

def upps_p24(studydata, column, context):
    """Please rename this column 'upps_p42' to avoid a naming conflict. """
    pass
fn["upps_p24"]=upps_p24

def upps_p25(studydata, column, context):
    """Please rename this column 'upps_p43' to avoid a naming conflict. """
    pass
fn["upps_p25"]=upps_p25

def upps_p26(studydata, column, context):
    """Please rename this column 'phenx_upps_p_26' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p26"]=upps_p26

def upps_p27(studydata, column, context):
    """Please rename this column 'phenx_upps_p_27' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p27"]=upps_p27

def upps_p28(studydata, column, context):
    """Please rename this column 'phenx_upps_p_28' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p28"]=upps_p28

def upps_p29(studydata, column, context):
    """Please rename this column 'phenx_upps_p_29' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p29"]=upps_p29

def upps_p30(studydata, column, context):
    """Please rename this column 'phenx_upps_p_30' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p30"]=upps_p30

def upps_p31(studydata, column, context):
    """Please rename this column 'phenx_upps_p_31' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p31"]=upps_p31

def upps_p32(studydata, column, context):
    """Please rename this column 'phenx_upps_p_32' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p32"]=upps_p32

def upps_p33(studydata, column, context):
    """Please rename this column 'phenx_upps_p_33' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p33"]=upps_p33

def upps_p34(studydata, column, context):
    """Please rename this column 'phenx_upps_p_34' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p34"]=upps_p34

def upps_p35(studydata, column, context):
    """Please rename this column 'phenx_upps_p_35' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p35"]=upps_p35

def upps_p36(studydata, column, context):
    """Please rename this column 'phenx_upps_p_36' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p36"]=upps_p36

def upps_p37(studydata, column, context):
    """Please rename this column 'phenx_upps_p_37' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p37"]=upps_p37

def upps_p38(studydata, column, context):
    """Please rename this column 'phenx_upps_p_38' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p38"]=upps_p38

def upps_p39(studydata, column, context):
    """Please rename this column 'phenx_upps_p_39' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p39"]=upps_p39

def upps_p40(studydata, column, context):
    """Please rename this column 'phenx_upps_p_40' to avoid a naming conflict. Also, please reverse code this column."""
    pass
fn["upps_p40"]=upps_p40

def medhx_1a(studydata, column, context):
    """Please keep data for these columns in their own rows, with 'version_form' labeling them "Past Year"."""
    pass
fn["medhx_1a"]=medhx_1a

def medhx_1a_other(studydata, column, context):
    """Please keep data for these columns in their own rows, with 'version_form' labeling them "Past Year"."""
    pass
fn["medhx_1a_other"]=medhx_1a_other

def medhx_6a_notes(studydata, column, context):
    """Please append " times" to each number."""
    pass
fn["medhx_6a_notes"]=medhx_6a_notes

def bld_core_d2p(studydata, column, context):
    """Please split this column into 'bld_core_d2ph' for hours and 'bld_core_d2pm' for minutes."""
    pass
fn["bld_core_d2p"]=bld_core_d2p

def bld_core_d2p(studydata, column, context):
    """Please split this column into 'bld_core_d2ph' for hours and 'bld_core_d2pm' for minutes."""
    pass
fn["bld_core_d2p"]=bld_core_d2p

def hba1c(studydata, column, context):
    """When the quantity was not sufficient, please leave the cells blank rather than use a missing code."""
    pass
fn["hba1c"]=hba1c

