query 1:

SELECT SUM(cumulative_confirmed) as total_cases_worldwide FROM `bigquery-public-data.covid19_open_data.covid19_open_data` where date = '2020-04-15';


query 2:

SELECT count(*) as count_of_states
FROM (
  SELECT
    subregion1_name,
    SUM(cumulative_deceased) as decease_sum
   FROM `bigquery-public-data.covid19_open_data.covid19_open_data` where
   date = '2020-04-10'
   and country_name="United States of America" and subregion1_name is not NULL
   group by subregion1_name
) where decease_sum > 100 ;


query 3:

SELECT
    subregion1_name as state,
    SUM(cumulative_confirmed) as total_confirmed_cases
FROM (
    SELECT
      subregion1_name, cumulative_confirmed
      FROM `bigquery-public-data.covid19_open_data.covid19_open_data` WHERE
      date = '2020-04-10'
      and country_code="US"
      and subregion1_name is not NULL
      )
      group by subregion1_name
      order by total_confirmed_cases DESC;


query 4: Fatality Ratio

select
total_confirmed_cases,
total_deaths,
total_deaths/total_confirmed_cases*100 as case_fatality_ratio from (
  SELECT
    country_name,
    SUM(cumulative_deceased) as total_deaths,
    SUM(cumulative_confirmed) as total_confirmed_cases
    FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE
    date between '2020-04-01' and  '2020-04-30'
    and country_name="Italy"
    group by country_name
)


query 5: Identifying specific day

ELECT country_name, date, cumulative_deceased
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_name="Italy" AND cumulative_deceased > 10000
ORDER BY date ASC


query 6: Finding days with zero net new cases

