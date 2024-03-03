-- Creating a table named 'countries' to store information about countries

CREATE TABLE countries(
    -- Column to store the two-letter country code
    COUNTRY_ID varchar(2),

    -- Column to store the name of the country (up to 40 characters)
    COUNTRY_NAME varchar(40),

    -- Column to store the region ID with decimal precision of 10, 0
    REGION_ID decimal(10,0)
);