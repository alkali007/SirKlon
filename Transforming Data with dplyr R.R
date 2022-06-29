glimpse() # To know how many column are there

counties %>%
  # Select the columns
  select(state,county,population,poverty)
  
counties_selected <- counties %>%
  select(state, county, population, private_work, public_work, self_employed)

counties_selected %>%
  # Add a verb to sort in descending order of public_work
  arrange(desc(public_work))

counties_selected <- counties %>%
  select(state, county, population)

counties_selected %>%
  # Filter for counties with a population above 1000000
  filter(population> 1000000, state =="California")
  
counties_selected <- counties %>%
  select(state, county, population, private_work, public_work, self_employed)

# Filter for Texas and more than 10000 people; sort in descending order of private_work
counties_selected %>%
  # Filter for Texas and more than 10000 people
  filter(state =="Texas", population> 10000) %>%
  # Sort in descending order of private_work
  arrange(desc(private_work))
  
counties_selected <- counties %>%
  select(state, county, population, public_work)

counties_selected %>%
  mutate(public_workers = public_work * population / 100) %>%
  # Sort in descending order of the public_workers column
  arrange(desc(public_workers))
  
counties_selected <- counties %>%
  # Select the columns state, county, population, men, and women
  select (state, county, population, men, women)

counties_selected %>%
  # Calculate proportion_women as the fraction of the population made up of women
  mutate(proportion_women = women/population)
  
counties %>%
  # Select the five columns 
  select(state, county, population,men,women) %>%
  # Add the proportion_men variable
  mutate(proportion_men = men/population) %>%
  # Filter for population of at least 10,000
  filter(population >=10000) %>%
  # Arrange proportion of men in descending order 
  arrange(desc(proportion_men))
